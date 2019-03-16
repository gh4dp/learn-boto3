import AWSServiceDetails
import pprintpp

class AWSServices:
    """Capture all services and details

        Has a dictionary
    """
    def __init__(self):
        """ Holds a dictionary of all services, and dictionary of all regions per service
            dictionary of all services:
                key of dictionary: name of the service
                value being: a dictionary of regions
            dictionary of all regions:
                key of dictionary: name of the region
                value being: a dictionary of details per region
        """
        self.aws_services = {}

    def add_service(self, serv_code, service_desc,  kwdict):
        if serv_code not in self.aws_services.keys():
            print('Key not found, adding')
        else:
            print('Key found, overwritting')
        new_list = list()
        new_list.append(service_desc)
        new_list.append(kwdict)
        self.aws_services[serv_code] = new_list

    def list_service(self, serv_code):
        if serv_code in self.aws_services.keys():
            print(serv_code)
            pprintpp.pprint(self.aws_services[serv_code])

    def list_services_all(self):
        for aKey in self.aws_services.keys():
            print(aKey)
            pprintpp.pprint(self.aws_services[aKey])
