import LbwAaL
import ConnectAWS
import QueryHTML
import consolemenu
import AWSServices, AWSServiceDetails
import pprintpp
import bs4
import MissingTagException
from consolemenu.items import *


class Driver:
    """Learn boto3 driver = main class"""

    def __init__(self):
        """All classes initialized and called from here"""
        # Empty objects declared first
        self.logger = LbwAaL.LbwAaL()
        self.awsservices = AWSServices.AWSServices(self.logger)

        self.qHTML = QueryHTML.QueryHTML(self.logger,None)
        self.get_services_n_regions()
        #self.connectaws = ConnectAWS.ConnectAWS(self.logger, 'dpdrpkri01')
        #self.connectaws.connect()

    def menu(self):
        # Create the menu
        main_menu = ConsoleMenu("Learn Boto3","Main Menu")
        S3menu = MenuItem("S3 Functions")
        RDSmenu = MenuItem("RDS Functions")
        EC2menu = MenuItem("EC2 Functions")

        # Once we're done creating them, we just add the items to the menu
        menu.append_item(S3menu)
        menu.append_item(RDSmenu)
        menu.append_item(EC2menu)

        # Finally, we call show to show the menu and allow the user to interact
        menu.show()

    def get_services_n_regions_via_re(self):
        self.qHTML.set_url('https://docs.aws.amazon.com/general/latest/gr/rande.html')
        self.qHTML.get_url()
        if self.qHTML.soup is None:
            return
        else:
            match_srvc = re.compile('<h2 id="(?P<srvc_code>.*)">(?P<srvc_name>.*)</h2>')

    def get_services_n_regions(self):
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
                #pprintpp.pprint(table_headers)

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
                print('-' * 40 + str(a_srvc['id']) + ' ' + str(len(datarow_list)))
                #pprintpp.pprint(datarow_list)
                for datarow_index_id, a_row in enumerate(datarow_list, start=1):
                    region_dict = dict()   # get a new dict for a new region
                    region_code=''
                    #pprintpp.pprint(table_soup_trs[datarow_index_id].findAll('td'))
                    table_soup_tds = table_soup_trs[datarow_index_id].findAll('td')
                    #pprintpp.pprint(table_soup_tds)
                    for col_index, a_header in enumerate(table_headers):
                        if a_header == "Region":
                            region_code = table_soup_tds[region_index].contents[0]  # or col_index both same
                        else:
                            try:
                                region_dict[a_header] = table_soup_tds[col_index].contents[0]
                            except IndexError:
                                region_dict[a_header] = None
                    # a row processed, a new region is processed.
                    regions_dict[region_code] = region_dict     # assign region_dict to region_code

                # all rows processed for a service, assign regions_dict
                self.awsservices.add_service(serv_code = a_srvc['id'],
                                              service_desc = a_srvc.contents[0],
                                              kwdict = regions_dict)
        self.awsservices.get_regions_for_service('s3')
if __name__=="__main__":
    driver = Driver()
    #driver.menu()
