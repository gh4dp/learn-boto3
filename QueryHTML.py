import requests, bs4, pprintpp, re


class QueryHTML:
    """Provide URL first and create an HTML object, then query for specific tags as you please."""

    def __init__(self, url):
        self.URL = url
        self.html_obj = None
        self.soup = None
        self.parser = None

    def get_url(self):
        self.html_obj = requests.get(self.URL)
        #pprintpp.pprint(self.html_obj.content)
        #print('Pause...')
        self.soup = bs4.BeautifulSoup(self.html_obj.content, features="lxml")
        #pprintpp.pprint(self.soup)
        #print('Ends')

    def get_tag_data(self, tag_pattern):
        # test_pat='<dt>[.*]<b>(.*)</b></span></dt>'
        # test_pat2='<dd><p>[.*]</p><p>[.*]</p><p>Required: Yes</p></dd>'
        data_term = '<dt>.*<b>(.*)</b></span></dt>'
        required_tags = self.soup.find_all(re.compile(tag_pattern))
        for a_req_tag in required_tags:
            pprintpp.pprint(a_req_tag)
            print(a_req_tag.previous_sibling)
            print(a_req_tag.next_sibling)
        print('Ends')

    def get_required_params(self):
        if self.soup is None:
            return
        else:
            bdts = self.soup.find_all('dt')
            bdds = self.soup.find_all('dd')
            indexid = 0
            pattern = re.compile(r'.*Required:\W(?P<req_yn>\w\w\w?)\W.*')
            for bdt in bdts:
                try:
                    ifmatched = pattern.search(bdds[indexid].text)
                    if 'Yes' in ifmatched.group(0).rstrip():
                        print(bdt.text.lstrip().rstrip(), ifmatched.group(0).rstrip())
                except Exception:
                    continue
                indexid = indexid + 1
