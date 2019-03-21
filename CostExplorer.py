import ConnectAWS
import LbwAaL
import pprintpp
import datetime
from datetime import timedelta
import pandas as pd
from consolemenu import SelectionMenu
import consolemenu
import tabulate

class CostExplorer:
    """Provides cost details"""

    def __init__(self, loggerobj: LbwAaL, sessionobj: ConnectAWS):
        self.logMe = loggerobj.logger
        self.client = sessionobj.Session.client('ce',region_name='us-west-2')
        self.response = None
        self.selected_menu = None

    def show_menu(self):
        list_ops=['Get Cost Usage', 'Show_cost_by_month_table', 'show_cost_by_service']
        self.selected_menu = consolemenu.SelectionMenu.get_selection(list_ops)
        while (self.selected_menu != len(list_ops)):
            if self.selected_menu == 0:
                self.getcostandusage()
            elif self.selected_menu == 1:
                self.show_cost_by_month_table()
            elif self.selected_menu == 2:
                self.show_cost_by_service()
            else:
                print('Exiting...')
                break
            input("Press Enter to continue...")
            self.selected_menu = consolemenu.SelectionMenu.get_selection(list_ops)

    def getcostandusage(self):
        """Provide time period as start,end date dictionary or will default to 1900 to 2500"""
        dt2 = datetime.datetime.today()
        timed1 = timedelta(days=365)
        dt1 = dt2 - timed1

        time_period = dict()
        time_period['Start'] = dt1.strftime("%Y-%m-%d")
        time_period['End'] = dt2.strftime("%Y-%m-%d")
        group_by = [{"Type": "DIMENSION", "Key": "SERVICE"}, ]

        pprintpp.pprint(time_period)
        data_list = list()
        data_list_header = ['Index', 'Start Date', 'End Date','Amount USD']
        self.response = self.client.get_cost_and_usage(TimePeriod=time_period, Granularity='MONTHLY',
                                                       Metrics=[
                                                           'UnblendedCost',
                                                       ],
                                                       GroupBy=group_by)
        for indexid, a_dict in enumerate(self.response['ResultsByTime'], start=1):
            try:
                if '.' in a_dict['Total']['UnblendedCost']['Amount']:
                    amount = float(a_dict['Total']['UnblendedCost']['Amount'])
                else:
                    amount = int(a_dict['Total']['UnblendedCost']['Amount'])
                data_list.append([
                    indexid,
                    a_dict['TimePeriod']['Start'],
                    a_dict['TimePeriod']['End'],
                    a_dict['Total']['UnblendedCost']['Amount']
                ])
            except Exception as e:
                print(str(e))
        print(tabulate.tabulate(data_list, data_list_header))
    def show_cost_by_month_table(self):
        if (self.response == None):
            self.getcostandusage()
        new_dict = self.response['ResultsByTime']
        pprintpp.pprint(new_dict)

    def show_cost_by_service(self):
        if (self.response == None):
            self.getcostandusage()

        print()
        print('.'*20 + 'AWS Cost report by service' + '.'*20)
        print()
        self.logMe.info('')
        self.logMe.info('.'*20 + 'AWS Cost report by service' + '.'*20)
        self.logMe.info('')

        new_dict = self.response['ResultsByTime']
        show_dict_from = new_dict[len(new_dict)-1]['Groups']
        make_a_list = list()
        make_a_list_header = ['Index', 'AWS Service', 'Cost-USD']
        for indexid, an_item in enumerate(show_dict_from, start=1):
            # print('{:<5} {:<60} {:<10}'.format(str(indexid), str(an_item['Keys']),
            #                                    str(an_item['Metrics']['UnblendedCost']['Amount'])))
            make_a_list.append([str(indexid), str(an_item['Keys']),str(an_item['Metrics']['UnblendedCost']['Amount'])])
        print(tabulate.tabulate(make_a_list, make_a_list_header))

        self.logMe.info(tabulate.tabulate(make_a_list, make_a_list_header))
        self.logMe.info('.'*30 + 'Done' +'.'*30)
