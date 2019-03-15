import AWSServiceDetails


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


    def add_service(self, region_name, region, endpoint, protocols):
        self.servicedetails[region] = AWSServiceDetails(region_name, region, endpoint, protocols)


    def list_service(self):
        pass