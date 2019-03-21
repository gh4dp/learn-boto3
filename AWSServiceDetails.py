class AWSServiceDetails:
    """Holds detail about a perticular service"""

    def __init__(self, region_key, **kwargs):
        self.region = region_key
        self.region_name = kwargs['regionname']
        self.endpoint = kwargs['endpoint']
        self.protocols = kwargs['protocols']

