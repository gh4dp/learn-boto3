import LbwAaL
import AWSServices, AWSServiceDetails
import pprintpp
import bs4
import ConnectAWS
import QueryHTML
import CostUsageReporting
import AWSServices, AWSServiceDetails
import MissingTagException
import CostExplorer
import S3Clinet
import EC2Client
import consolemenu
from consolemenu.items import *

#aws_region_codes = list()


class Driver:
    """Learn boto3 driver = main class"""

    def __init__(self):
        """All classes initialized and called from here"""
        # Empty objects declared first
        self.logger = LbwAaL.LbwAaL()
        self.awsservices = AWSServices.AWSServices(self.logger)

        self.connectaws = ConnectAWS.ConnectAWS(self.logger, 'dpdrpkri01')
        self.connectaws.connect()

        # Get regions & services, Ideally we should do this at some interval
        # and save it on the File System to just reload from a file.
        self.qHTML = QueryHTML.QueryHTML(self.logger,None)
        self.get_services_n_regions()

        #Clients
        self.s3client = S3Clinet.S3Client(self.logger, self.connectaws)
        self.ceclient = CostExplorer.CostExplorer(self.logger, self.connectaws)
        self.cusclient = CostUsageReporting.CostUsageReporting(self.logger, self.connectaws)
        self.ec2client = EC2Client.EC2Client(self.logger, self.connectaws, self.awsservices)
        self.rdsclient = self.s3client # just playing


    def menu(self):
        main_menu_items = ["S3 Functions",
                           "Cost Explorer Functions",
                           "Cost Usage Reporting Functions",
                           "EC2 Functions",
                           "RDS Functions"]

        main_menu_selection = consolemenu.SelectionMenu.get_selection(main_menu_items)
        while main_menu_selection != len(main_menu_items):
            print('You selected :' + str(main_menu_items[main_menu_selection]))
            if main_menu_selection == 0:
                self.s3client.show_menu()
            elif main_menu_selection == 1:
                self.ceclient.show_menu()
            elif main_menu_selection == 2:
                pass
            elif main_menu_selection == 3:
                self.ec2client.show_menu()
            elif main_menu_selection == 4:
                pass
            else:
                print ('Exiting now...')
                break
            main_menu_selection = consolemenu.SelectionMenu.get_selection(main_menu_items)


    def get_services_n_regions_via_re(self):
        self.qHTML.set_url('https://docs.aws.amazon.com/general/latest/gr/rande.html')
        self.qHTML.get_url()
        if self.qHTML.soup is None:
            return
        else:
            match_srvc = re.compile('<h2 id="(?P<srvc_code>.*)">(?P<srvc_name>.*)</h2>')

    def get_services_n_regions(self):
        global aws_region_codes
        self.qHTML.set_url('https://docs.aws.amazon.com/general/latest/gr/rande.html')
        self.qHTML.get_url()
        if self.qHTML.soup is None:
            return
        else:
            all_services = self.qHTML.soup.find_all('h2')
            all_serv_regs = self.qHTML.soup.find_all('div', {'class', 'table'})
            datarow_index_id = 0
            for a_srvc, a_srvc_reg in zip(all_services, all_serv_regs):
                table_soup_trs = a_srvc_reg.findAll('tr')
                regions_dict = dict()
                table_soup_ths = table_soup_trs[0].findAll('th')
                table_headers = [ row.contents[0].replace(' ','') for row in table_soup_trs[0].findAll('th')]

                #find region index key -
                region_index = 0
                for a_header in table_headers:
                    if a_header == "Region":
                        break
                    else:
                        region_index = region_index + 1

                # index_id indicates table row index, first row = dict keys, rest values
                regions_dict = dict()  # get a new dict for a all regions
                datarow_list = table_soup_trs[1:]
                #print('-' * 40 + str(a_srvc['id']) + ' ' + str(len(datarow_list)))
                for datarow_index_id, a_row in enumerate(datarow_list, start=1):
                    region_dict = dict()   # get a new dict for a new region
                    region_code=''
                    table_soup_tds = table_soup_trs[datarow_index_id].findAll('td')
                    for col_index, a_header in enumerate(table_headers):
                        if a_header == "Region":
                            region_code = table_soup_tds[region_index].contents[0].strip()  # or col_index both same
                        else:
                            try:
                                region_dict[a_header] = table_soup_tds[col_index].contents[0]
                            except IndexError:
                                region_dict[a_header] = None
                    # a row processed, a new region is processed.
                    regions_dict[region_code] = region_dict     # assign region_dict to region_code
                    if len(region_code) > 0:
                        #aws_region_codes.append(region_code)
                        self.awsservices.aws_region_codes.add(region_code)

                    # all rows processed for a service, assign regions_dict
                self.awsservices.add_service(serv_code = a_srvc['id'],
                                              service_desc = a_srvc.contents[0],
                                              kwdict = regions_dict)

        pprintpp.pprint(self.awsservices.aws_region_codes)

    def get_costusagereporting(self):
        #cur_session = CostUsageReporting.CostUsageReporting(self.logger, self.connectaws)
        self.cusclient.get_cur_report()

    def cost_report(self):
        self.ceclient.getcostandusage()

    def get_s3_buckets(self):
        self.s3client.get_s3_buckets()

if __name__=="__main__":
    driver = Driver()
    #driver.cost_report()
    driver.menu()
