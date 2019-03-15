import LbwAaL
import ConnectAWS
import QueryHTML
import consolemenu
import AWSServices, AWSServiceDetails
import pprintpp
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
        self.aws_services = {}

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

    def get_services_n_regions(self):
        self.qHTML.set_url('https://docs.aws.amazon.com/general/latest/gr/rande.html')
        self.qHTML.get_url()
        if self.qHTML.soup is None:
            return
        else:
            #<h2 id="appdiscserv_region">AWS Application Discovery Service</h2>
            #pat_serviceHeader = '<h2 id="(?P<srvc_code>[a-zA-Z_]*)">(?P<srvc_name>.*)</h2>'

            #mainContent=soup.find_all('div',attrs={'id','main-content'})
            #rs_allTags = self.qHTML.soup.find_all(True)
            rs_allTags = self.qHTML.soup.find("div", {"id": "main-content"})
            prevTagIndex=0  # -1 enumerate start=1:
            NextTagIndex = 2  # +1 enumerate start=1:
            for i, tag_aTag in enumerate(rs_allTags, start=1):
                #pprintpp.pprint(tag_aTag)
                #print('Pause...')
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




if __name__=="__main__":
    driver = Driver()
    #driver.menu()
