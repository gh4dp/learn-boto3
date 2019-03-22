import pprintpp
import LbwAaL
import boto3
import ConnectAWS
import consolemenu
import driver
import AWSServices


class AWSLambda:
    """Get and manage S3 from here"""

    def __init__(self, loggerobj: LbwAaL, sessionobj: ConnectAWS, awsservices: AWSServices):
        self.logMe = loggerobj.logger
        self.client = sessionobj.Session.client('lambda', region_name='us-east-1')
        self.awsservices = awsservices
        self.exclude_regions = awsservices.exclude_regions

    def show_menu(self):
        list_ops = ['list functions']
        self.selected_menu = consolemenu.SelectionMenu.get_selection(list_ops)
        while self.selected_menu != len(list_ops):
            if self.selected_menu == 0:
                self.get_lambda_functions()
            else:
                print('Exiting...')
                break
            input("Press Enter to continue...")
            self.selected_menu = consolemenu.SelectionMenu.get_selection(list_ops)

    def get_lambda_functions(self):
        lambdas = None
        sorted_regions = list(self.awsservices.aws_region_codes)
        sorted_regions.sort()
        for a_region in sorted_regions:
            if a_region in self.exclude_regions:
                continue
            print('Going in region: ' + a_region)
            try:
                self.client = boto3.client('lambda', region_name=a_region)
                if self.client is None:
                    print('Can not connect to: ' + a_region)
                    return
                else:
                    lambdas = self.client.list_functions()
                    for each_lambda in lambdas:
                        pprintpp.pprint(each_lambda['Functions'])
            except Exception as e:
                pprintpp.pprint(str(e))


"""
'string indices must be integers'
Going in region: us-gov-east-1
'An error occurred (UnrecognizedClientException) when calling the ListFunctions operation: The security token included in the request is invalid.'
Going in region: us-gov-west-1
'An error occurred (UnrecognizedClientException) when calling the ListFunctions operation: The security token included in the request is invalid.'
Going in region: us-west-1
'string indices must be integers'
Going in region: us-west-2
'string indices must be integers'
P
"""