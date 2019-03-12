import boto3
import pprintpp, secrets, datetime
import QueryHTML


class ConnectAWS:
    """ Provide a profile name in the instance creation and connect to aws.

        For now, we start with connection to the aws.
        We will add some more generic code about aws into this same class.
        This was the future version of the class may not be strictly about connecting to aws.
    """
    def __init__(self, profname: str):
        """ Specified type for refence using annotations profn ame: str """
        self.profName = profname
        self.connection = None
        self.randomstr = secrets.token_hex(8)

    def connect(self):
        try:
            self.connection = boto3.session.Session(profile_name=self.profName)
            # NOTE 1, all attrib + methods seen here "self.connection."
            print('************** connected!')
        except Exception:
            print('Not connected')
            pass

    def get_regions(self):
        """Let's get all the regions within AWS"""
        # NOTE 2, and nothing here "self.connection."
        # sess = boto3.session.Session(profile_name=self.profName)
        sess = self.connection
        allregions = sess.get_available_regions(service_name='ec2', allow_non_regional=True)
        pprintpp.pprint(allregions)

    def get_s3_buckets(self):
        pass

    def create_rds(self):
        aConnection = boto3.session.Session(profile_name=self.profName, region_name='us-east-1')
        cRDS=aConnection.client('rds')

        print('self.randomstr: ', self.randomstr)
        resp = cRDS.create_db_instance(
                DBInstanceIdentifier='dpdrpkri0120190307',
                DBInstanceClass='db.t2.micro',
                Engine='mysql',
                MasterUsername='dpdrpkri01u',
                MasterUserPassword='dpdrpkri01'+self.randomstr,
                AllocatedStorage=20
            )
        pprintpp(resp)


if __name__ == "__main__":
    #aconn = ConnectAWS('dpdrpkri01')
    #aconn.connect()
    #aconn.get_regions()
    #aconn.create_rds()
    q_html = QueryHTML.QueryHTML('https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html')
    q_html.get_url()
    q_html.get_tag_data("Required: Yes")


