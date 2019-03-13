import LbwAaL
import ConnectAWS
import QueryHTML
import consolemenu
from consolemenu.items import *


class Driver:
    """Learn boto3 driver = main class"""

    def __init__(self):
        """All classes initialized and called from here"""
        self.logger = LbwAaL.LbwAaL()
        self.connectaws = ConnectAWS.ConnectAWS(self.logger, 'dpdrpkri01')
        self.connectaws.connect()
        self.get_services_n_regions()

    def menu(self):
        # Create the menu
        main_menu = ConsoleMenu("Learn Boto3","Main Menu")
        S3menu = MenuItem("S3 Functions")
        RDSmenu = MenuItem("RDS Functions")
        EC2menu = MenuItem("EC2 Functions")

        # Once we're done creating them, we just add the items to the menu
        menu.append_item(S3menu)
        menu.append_item(RDSmenu)
        menu.append_item(EC2menu)

        # Finally, we call show to show the menu and allow the user to interact
        menu.show()



if __name__=="__main__":
    driver = Driver()
    #driver.menu()
