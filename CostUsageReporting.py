import pprintpp
import LbwAaL
import driver
import boto3
import secrets
import ConnectAWS

class CostUsageReporting:
    """Get and manage S3 from here"""

    def __init__(self, loggerobj: LbwAaL, sessionobj: ConnectAWS):
        self.logMe = loggerobj.logger
        self.client = sessionobj.Session.client('cur')

    def get_cur_report(self):
        next_token = str(secrets.token_hex(8))
        report = self.client.describe_report_definitions (
            MaxResults = 5,
            NextToken = next_token
        )

        paginator = self.client.get_paginator('describe_report_definitions')
        print('next_token : ' + next_token )
        pprintpp.pprint(report)
        pprintpp.pprint(paginator.__dict__)