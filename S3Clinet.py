import pprintpp
import LbwAaL
import driver
import boto3
import ConnectAWS



class S3Client:
    """Get and manage S3 from here"""
    def __init__(self, loggerobj: LbwAaL, sessionobj: ConnectAWS):
        self.logMe = loggerobj.logger
        self.client = sessionobj.Session.client('s3')

    def get_s3_buckets(self):
        if not self.client:
            self.logMe('Not connected to S3')
        else:
            for a_region in driver.aws_region_codes:
                self.logMe.info(a_region)
                pprintpp.pprint(a_region)


    #gawarsing, parwar
