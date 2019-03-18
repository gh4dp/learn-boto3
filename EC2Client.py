import pprintpp
import LbwAaL
import driver
import boto3


class EC2Client:
    """Get and manage S3 from here"""

    def __init__(self, loggerobj: LbwAaL):
        self.logMe = loggerobj.logger

    def get_ec2_instances(self):
        for a_region in driver.aws_region_codes:
            pass
    # gawarsing, parwar, Flower, Dhana-2-bunch
