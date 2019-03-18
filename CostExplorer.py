import ConnectAWS
import LbwAaL
import pprintpp

class CostExplorer:
    """Provides cost details"""

    def __init__(self, loggerobj: LbwAaL, sessionobj: ConnectAWS):
        self.logMe = loggerobj.logger
        self.client = sessionobj.Session.client('ce')
        self.response = None

    def getcostandusage(self):
        """Provide time period as start,end date dictionary or will default to 1900 to 2500"""
        kwargs = dict()
        if len(kwargs) == 0:
            a_dict = dict()
            a_dict['start'] = '2000-01-01'
            a_dict['end'] = '2100-01-01'
        self.response = self.client.get_cost_and_usage(kwargs = dict)
        pprintpp.pprint(self.response)
