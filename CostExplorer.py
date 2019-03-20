import ConnectAWS
import LbwAaL
import pprintpp
import datetime
from datetime import timedelta
import pandas as pd

class CostExplorer:
    """Provides cost details"""

    def __init__(self, loggerobj: LbwAaL, sessionobj: ConnectAWS):
        self.logMe = loggerobj.logger
        self.client = sessionobj.Session.client('ce')
        self.response = None

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
        self.response = self.client.get_cost_and_usage(TimePeriod=time_period, Granularity='MONTHLY',
                                                       Metrics=[
                                                           'UnblendedCost',
                                                       ],
                                                       GroupBy=group_by)
        self.show_cost_by_service()

    def show_cost_by_month_table(self):
        new_dict = self.response['ResultsByTime']
        pprintpp.pprint(new_dict)

    def show_cost_by_service(self):
        print()
        print()
        print('.'*20 + 'AWS Cost report by service' + '.'*20)
        self.logMe.info('.'*20 + 'AWS Cost report by service' + '.'*20)
        new_dict = self.response['ResultsByTime']
        pd_df = pd.DataFrame(new_dict[len(new_dict)-1]['Groups'])
        print(pd_df)
        self.logMe.info(pd_df)
        print('.' * 50)
        print('.'*30 + 'Done' +'.'*30)
        self.logMe.info('.'*30 + 'Done' +'.'*30)
