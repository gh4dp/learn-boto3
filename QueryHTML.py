import urllib3, bs4, pprintpp, re

class QueryHTML:
    """Provide URL first and create an HTML object, then query for specific tags as you please."""

    def __init__(self, url):
        self.URL = url
        self.http = None
        self.html_obj = None
        self.soup = None
        self.parser = None

    def get_url(self):
        urllib3.disable_warnings()
        self.http = urllib3.PoolManager()
        self.html_obj = self.http.request('GET', self.URL)
        pprintpp.pprint(self.html_obj)
        print('Pause...')
        self.soup = bs4.BeautifulSoup(self.html_obj, features="lxml")
        pprintpp.pprint(self.soup.data)
        print('Ends')

    def get_tag_data(self, tag_pattern):
        #test_pat='<dt>[.*]<b>(.*)</b></span></dt>'
        #test_pat2='<dd><p>[.*]</p><p>[.*]</p><p>Required: Yes</p></dd>'
        required_tags = self.soup.find_all(re.compile(tag_pattern))
        for a_req_tag in required_tags:
            pprintpp.pprint(a_req_tag)
            print(a_req_tag.previous_sibling)
            print(a_req_tag.next_sibling)
        print('Ends')