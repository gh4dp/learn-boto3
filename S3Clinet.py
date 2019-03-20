import pprintpp
import LbwAaL
import driver
import boto3
import ConnectAWS
import consolemenu


class S3Client:
    """Get and manage S3 from here"""
    def __init__(self, loggerobj: LbwAaL, sessionobj: ConnectAWS):
        self.logMe = loggerobj.logger
        self.client = sessionobj.Session.client('s3',region_name='us-west-2')

    def show_menu(self):
        list_ops=['Get list of buckets']
        self.selected_menu = consolemenu.SelectionMenu.get_selection(list_ops)
        while self.selected_menu != len(list_ops):
            if self.selected_menu == 0:
                self.get_s3_buckets()
            else:
                print('Exiting...')
                break
            input("Press Enter to continue...")
            self.selected_menu = consolemenu.SelectionMenu.get_selection(list_ops)

    def get_s3_buckets(self):
        if not self.client:
            self.logMe('Not connected to S3')
        else:
            # pd_list_of_dict = list()
            # pd_list_of_dict.append({'Bucket': None, 'Location': None, })
            owners_buckets = self.client.list_buckets()
            pprintpp.pprint(owners_buckets['Owner'])
            self.logMe.info(owners_buckets['Owner'])
            for indexid, a_bucket in enumerate(owners_buckets['Buckets']):
                self.logMe.info(str(a_bucket))
                pprintpp.pprint(a_bucket)
                input("Press Enter to continue...")
                #print('{:<30} {:<15}'.format(a_bucket, str(self.client.get_bucket_location(Bucket = a_bucket))))
