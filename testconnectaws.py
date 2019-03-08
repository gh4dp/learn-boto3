import boto3
import pprintpp

class ConnectAWS:
    """ Provide a profile name in the instance creation and connect to aws.

        For now, we start with connection to the aws.
        We will add some more generic code about aws into this same class.
        This was the future version of the class may not be strictly about connecting to aws.
    """
    def __init__(self, profname: str):
        """ Specified type for refence using annotations profname: str """
        self.profName = profname
        self.connection = None

    def connect(self):
        try:
            self.connection = boto3.Session(profile_name=self.profName)
            print('************** connected!')
        except Exception:
            print('Not connected')
            pass

    def get_regions(self):
        """Let's get all the regions within AWS"""
        sess = boto3.session.Session()
        allregions = sess.get_available_regions(service_name='ec2', allow_non_regional=True)
        pprintpp.pprint(allregions)


if __name__ == "__main__":
    aconn = ConnectAWS('dpdrpkri01')
    aconn.connect()
    aconn.get_regions()
