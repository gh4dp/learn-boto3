import boto3
import QueryHTML
import LbwAaL


class ConnectAWS:
    """ Provide a profile name in the instance creation and connect to aws.
        import pprintpp, secrets, datetime

        For now, we start with connection to the aws.
        We will add some more generic code about aws into this same class.
        This was the future version of the class may not be strictly about connecting to aws.
    """
    def __init__(self, aLogger: LbwAaL, profname: str):
        """ Specified type for refence using annotations profn ame: str

        :param aLogger: of class LbwAaL
        :param profname: str - tells which profile to use to connect to AWS
        """
        self.profName = profname
        self.connection = None
        self.allregions = None
        #self.randomstr = secrets.token_hex(8)
        self.logme = aLogger.logger


    def connect(self):
        try:
            self.connection = boto3.session.Session(profile_name=self.profName)
            self.logme.info('Connected using: '+self.profName)
        except Exception:
            print('Not connected')
            pass

    # def get_regions(self):
    #     """Lists and captures all aws regions
    #         Region is required in many aws api calls
    #         so we fetch and capture them at once
    #     """
    #     sess = self.connection
    #     self.allregions = sess.get_available_regions(service_name='ec2', allow_non_regional=True)
    #     for i, a_reg in enumerate(self.allregions, start=1):
    #         self.logme.info('AWS region found: ' + str(i) + ' : ' + a_reg)
    #     pprintpp.pprint(self.allregions)

