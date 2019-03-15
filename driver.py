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
        self.logger = LbwAaL.LbwAaL()
        self.qHTML = QueryHTML.QueryHTML(self.logger,None)
        self.get_services_n_regions()
        self.connectaws = ConnectAWS.ConnectAWS(self.logger, 'dpdrpkri01')
        self.connectaws.connect()
        self.aws_services = AWSServices.AWSServices()

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
            index_id = 0
            for a_srvc, a_srvc_reg in zip(all_services, all_serv_regs):
                #a_srvc_reg = all_serv_regs[0]
                #pprintpp.pprint(a_srvc_reg)
                table_soup_trs = a_srvc_reg.findAll('tr')
                #pprintpp.pprint(table_soup_trs[0])
                regions_dict = dict()
                # for a_row in  table_soup_trs[0]:
                #     pprintpp.pprint('Type of t row: ' + str(type(table_soup_trs[0])))
                #     pprintpp.pprint('row: ' + a_row)

                #row 0 provides header, which will be keys to dict
                table_soup_ths = table_soup_trs[0].findAll('th')
                #pprintpp.pprint('Type of table_soup_ths: '+str(type(table_soup_ths)))
                #Very Valueable pprintpp.pprint([row.__dict__ for row in table_soup_trs[0].findAll('th')])
                table_headers = [ row.contents[0].replace(' ','') for row in table_soup_trs[0].findAll('th')]
                pprintpp.pprint(table_headers)

                #find region index key -
                region_index = 0
                for a_header in table_headers:
                    if a_header == "Region":
                        break
                    else:
                        region_index = region_index + 1

                # index_id indicates table row index, first row = dict keys, rest values
                regions_dict = dict()  # get a new dict for a all regions
                for index_id, a_row in enumerate(table_soup_trs, start=1):
                    region_dict = dict()   # get a new dict for a new region
                    region_code=''
                    table_soup_tds = table_soup_trs[index_id].findAll('td')
                    for col_index, a_header in enumerate(table_headers):
                        if a_header == "Region":
                            region_code = table_soup_tds[region_index].contents[0]  # or col_index both same
                        else:
                            region_dict[a_header] = table_soup_tds[col_index].contents[0]
                    # a row processed, a new region is processed.
                    regions_dict[region_code] = region_dict     # assign region_dict to region_code

                # all rows processed for a service, assign regions_dict
                self.aws_services.add_service(a_srvc, regions_dict)



                print('Pause.............')
                """

                for index_id, table_soup_tr in enumerate(table_soup_trs, start=1):
                    

                table_soup_trs = table_soup.find_all('tr')
                for a_table_soup_tr in table_soup_trs:

                all_r = all_serv_regs[4].find_all('tr')
                cols_of_row = a_row.find_all('td')
                for id3, aCol in enumerate(cols_of_row):
                    if id3 == region_key_index:
                        region_key_name = aCol.text.strip()
                        continue
                    else:
                        cols_list.append(aCol.text.strip())
                        dict_of_region[all_keys[indexid]] = aCol.text.strip()
                        indexid = indexid + 1
                self.awsservices_details_dict[region_key_name] = AWSServiceDetails(region_key_name, dict_of_region)
                index_id = index_id + 1

            #<h2 id="appdiscserv_region">AWS Application Discovery Service</h2>
            #pat_serviceHeader = '<h2 id="(?P<srvc_code>[a-zA-Z_]*)">(?P<srvc_name>.*)</h2>'

            #mainContent=soup.find_all('div',attrs={'id','main-content'})
            #div_main_content = self.qHTML.soup.find("div", {"id": "main-content"})
            #div_main_content = self.qHTML.soup.find("li", "listitem")
            #rs_allTags = div_main_content.find_all(True)

            rs_allTags = self.qHTML.soup.find_all(True)
            print('len rs_allTags : ' + str(len(rs_allTags)))
            prevTagIndex=0  # -1 enumerate start=1:
            NextTagIndex = 2  # +1 enumerate start=1:

            # import requests, pprintpp, bs4, re
            # html_obj = open('Sample.html', 'r', encoding='utf-8')
            # soup = bs4.BeautifulSoup(html_obj, features="lxml")
            all_services = soup.find_all('h2')
            all_serv_regs = soup.find_all('div', {'class', 'table'})
            for a_srvc, a_srv_regions in zip( all_services, all_serv_regs):
                pprintpp.pprint(indexid)
                pprintpp.pprint(aT.contents)
                service_name = tag_aTag.name  # Key of the class






            for indexId, tag_aTag in enumerate(rs_allTags, start=1):
                if isinstance(tag_aTag, bs4.element.Tag):
                    pprintpp.pprint(tag_aTag.decode())
                    try:
                        pprintpp.pprint("Tag Id: {0} name: {1} contents: {2} ".format(tag_aTag['id'], tag_aTag.name,
                                                                                      tag_aTag.contents))
                    except Exception:
                        pass
            #for tag_aTag in rs_allTags:
                # if isinstance(tag_aTag, bs4.element.NavigableString):
                #     continue
                for x1 in range(10):
                    print()
                #pprintpp.pprint("Tag Id: {0} name: {1} contents: {2} ".format(tag_aTag['id'], tag_aTag.name, tag_aTag.contents))
                #print('IndexId: ' + str(indexId) + '; Type of tag_aTag ' + str(type(tag_aTag)) + ' Pause...', )
                if '_region' in tag_aTag['id']:
                    service_name = tag_aTag.name  # Key of the class
                    if not (service_name in self.aws_services.keys()):
                        self.aws_services[service_name] = AWSServices()
                    self.awsservices_dict = dict()
                    self.awsservices_details_dict = dict()
                    table_of_regions = rs_allTags[NextTagIndex].find('table')

                    # get the keys from the header
                    # These keys include: RegionName Region	Endpoint Protocol
                    # Region is our key for dictionary
                    region_key_index = 0
                    all_keys = []
                    row_of_keys = table_of_regions.find_all('th')
                    for id2, a_key in enumerate(row_of_keys):
                        all_keys.append(a_key.replace(' ',''))
                        if a_key == 'Region':
                            region_key_index = id2
                    rows_of_regions = table_of_regions.find_all('tr')

                    cols_list = []
                    indexid = 0
                    dict_of_regions = dict()
                    region_key_name = None
                    for a_row in rows_of_regions:
                        # Each row gives us a new region and so new dict
                        dict_of_region = dict()

                        cols_of_row = a_row.find_all('td')
                        for id3, aCol in enumerate(cols_of_row):
                            if id3 == region_key_index:
                                region_key_name = aCol.text.strip()
                                continue
                            else:
                                cols_list.append(aCol.text.strip())
                                dict_of_region[all_keys[indexid]] = aCol.text.strip()
                                indexid = indexid + 1
                        self.awsservices_details_dict[region_key_name] = AWSServiceDetails(region_key_name, dict_of_region)
                    dict_of_regions[region_key_name] = region_key_name
                    """



if __name__=="__main__":
    driver = Driver()
    #driver.menu()
