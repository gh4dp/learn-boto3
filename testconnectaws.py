import boto3


class ConnectAWS:
    def __init__(self, profname):
        self.profName = profname
        self.connection = None

    def connect(self):
        try:
            self.connection = boto3.Session(profile_name=self.profName)
            print('************** connected!')
        except:
            print('Not connected')
            pass


if __name__ == "__main__":
    aconn = ConnectAWS('dpdrpkri01')
    aconn.connect()
