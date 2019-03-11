import urllib3, bs4, pprintpp, AdvancedHTMLParser

class QueryHTML:
    """Provide URL first and create an HTML object, then query for specific tags as you please."""

    def __init__(self, url):
        self.URL = url
        self.http = None
        self.html_obj =None
        self.b4soup=None
        self.parsered_tree = None
        self.parser = AdvancedHTMLParser.AdvancedHTMLParser()

    def get_url(self):
        self.http = urllib3.poolmanager()
        self.html_obj = self.http.request('GET',self.URL)
        self.parsered_tree = self.parser.parseStr(self.html_obj)

    def getTagData(self,tag_pattern):
        for anode in self.parsered_tree.getAllNodes()
            pprintpp.pprint(anode)