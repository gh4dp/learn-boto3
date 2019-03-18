import pprintpp
import LbwAaL
import driver
import boto3


class S3Client:
    """Get and manage S3 from here"""

    def __init__(self, loggerobj: LbwAaL):
        self.logMe = loggerobj.logger

    def get_s3_buckets(self):
        for a_region in driver.aws_region_codes:
            pass
    #gawarsing, parwar
