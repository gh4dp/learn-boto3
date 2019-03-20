import pprintpp
import LbwAaL
import boto3
import ConnectAWS
import consolemenu
import driver
import AWSServices

class EC2Client:
    """Get and manage S3 from here"""

    def __init__(self, loggerobj: LbwAaL, sessionobj: ConnectAWS, awsservices: AWSServices):
        self.logMe = loggerobj.logger
        self.client = sessionobj.Session.client('ec2',region_name='us-west-2')
        self.response = None
        self.selected_menu = None
        self.awsservices = awsservices
        self.exclude_regions = set()
        self.exclude_regions.add('ap-northeast-1')
        self.exclude_regions.add('ap-northeast-2')
        self.exclude_regions.add('ap-northeast-3')
        self.exclude_regions.add('ap-south-1')
        self.exclude_regions.add('ap-southeast-1')
        self.exclude_regions.add('ap-southeast-2')
        self.exclude_regions.add('ca-central-1')
        self.exclude_regions.add('cn-north-1')
        self.exclude_regions.add('cn-northwest-1')

    def show_menu(self):
        list_ops=['Get EC2 instances']
        self.selected_menu = consolemenu.SelectionMenu.get_selection(list_ops)
        while self.selected_menu != len(list_ops):
            if self.selected_menu == 0:
                self.get_ec2_instances()
            else:
                print('Exiting...')
                break
            input("Press Enter to continue...")
            self.selected_menu = consolemenu.SelectionMenu.get_selection(list_ops)


    def get_ec2_instances(self):
        pprintpp.pprint(self.awsservices.aws_region_codes)
        sorted_regions=list(self.awsservices.aws_region_codes)
        sorted_regions.sort()
        for a_region in sorted_regions:
            if a_region in self.exclude_regions:
                continue
            print('Going in region: ' + a_region)
            try:
                self.client = boto3.client('ec2', region_name=a_region)
                ec2_instances = self.client.describe_instances()
                for an_ec2_instance in ec2_instances['Reservations'][0]['Instances']:
                    print('\tInstanceId:{:<30}'.format(an_ec2_instance['InstanceId']))
                    print('\tInstanceType:{:<50}'.format(an_ec2_instance['InstanceType']))
                    print('\tKeyName:{:<30}'.format(an_ec2_instance['KeyName']))
                    print('\tTags:{:<50}'.format(str(an_ec2_instance['Tags'])))
                    print('\tPublicIpAddress:{:<30}'.format(an_ec2_instance['PublicIpAddress']))
                    print('\tPublicDnsName:{:<60}'.format(an_ec2_instance['PublicDnsName']))
                    print('\tPrivateIpAddress:{:<30}'.format(an_ec2_instance['PrivateIpAddress']))
                    # w1=an_ec2_instance['InstanceId'],
                    # w2=an_ec2_instance['InstanceType'],
                    # w3=an_ec2_instance['KeyName'],
                    # w4=an_ec2_instance['PublicIpAddress'],
                    # w5=an_ec2_instance['PublicDnsName'],
                    # w6=an_ec2_instance['PrivateIpAddress'],
                    # w7=str(an_ec2_instance['Tags'])
                    # print('{:<11} {:<13} {:<8} {:<15} {:<30} {:<15} {<30}'.format(c['InstanceId'],
                    #                                                        c['InstanceType'],
                    #                                                        c['KeyName']
                    #                                                        )
                    #       )
                    # print('{:<15} {:<30} {:<15} {<30}'.format(
                    #                                                       c['PublicIpAddress'],
                    #                                                       c['PublicDnsName'],
                    #                                                       c['PrivateIpAddress'],
                    #                                                       str(c['Tags'])
                    #                                                       )
                    #       )
                    #
                    # print('{<30}'.format(str(c['Tags'])))


                    # print('{:<11} {:<13} {:<8} {:<15} {:<30} {:<15} {<30}'.format(c['InstanceId'],
                    #                                                        c['InstanceType'],
                    #                                                        c['KeyName'],
                    #                                                        c['PublicIpAddress'],
                    #                                                        c['PublicDnsName'],
                    #                                                        c['PrivateIpAddress'],
                    #                                                        str(c['Tags'])
                    #                                                        )
                    #       )
                    #pprintpp.pprint(an_ec2_instance )
            except Exception:
                pass
