import AWSServiceDetails
import pprintpp
import LbwAaL

class AWSServices:
    """Capture all services and details

        Has a dictionary
    """
    def __init__(self, loggerObj: LbwAaL):
        """ Holds a dictionary of all services, and dictionary of all regions per service
            dictionary of all services:
                key of dictionary: name of the service
                value being: a dictionary of regions
            dictionary of all regions:
                key of dictionary: name of the region
                value being: a dictionary of details per region
        """
        self.aws_services = {}
        self.log_me = loggerObj.logger
        self.aws_region_codes = set()

    def add_service(self, serv_code, service_desc,  kwdict):
        new_list = list()
        new_list.append(service_desc)
        new_list.append(kwdict)
        self.aws_services[serv_code] = new_list
        log_str = str( [ serv_code, service_desc, str(new_list[0]), str(new_list[1]) ] )
        self.log_me.info( log_str )

    def list_services_all(self):
        for aKey in self.aws_services.keys():
            self.list_service(aKey)

    def list_service(self, serv_code):
        for aKey in self.aws_services.keys():
            #print(str(type(aKey)) + aKey)
            pass
        pprintpp.pprint(self.aws_services.keys())
        search_serv_code = serv_code + "_region"
        if search_serv_code  in self.aws_services.keys():
            #print(search_serv_code)
            #pprintpp.pprint(self.aws_services[search_serv_code ])
            log_str = str([search_serv_code, str(self.aws_services[search_serv_code][0]), str(self.aws_services[search_serv_code][1])])
            self.log_me.info( log_str )

    def list_service_keys(self):
        self.log_me.info('Listing all service keys.......................................')
        for aKey in self.aws_services.keys():
            #print(aKey)
            self.log_me.info( aKey )

    def get_regions_for_service(self, serv_code):
        search_serv_code = serv_code + "_region"
        if search_serv_code in self.aws_services.keys():
            #print(search_serv_code)
            #pprintpp.pprint(self.aws_services[search_serv_code])
            regions_dict = self.aws_services[search_serv_code][1]   # 0: serv desc, 1: regions dict
            for a_region in regions_dict:
                print("{:<25} {:<40}".format(a_region, regions_dict[a_region]['RegionName']))
