import requests, bs4, pprintpp, re
import LbwAaL


class QueryHTML:
    """Provide URL first and create an HTML object, then query for specific tags as you please."""

    def __init__(self, loggerObj: LbwAaL, url):
        """Initialize and set some important vars

        :param loggerObj: of class  LbwAaL, helpful for loggging
        :param url: The URL to fetch and query

        sets internal page_info to Page-name from the url
        """
        self.URL = url
        self.html_obj = None
        self.soup = None
        self.parser = None
        self.extracted_tags = None
        list1 = self.URL.split('/')
        self.page_info = list1[len(list1)-1]
        self.logMe = loggerObj.logger

    def set_url(self, URL: str):
        self.URL = URL

    def get_url(self):
        """ Fetches the url and sets interval vars:
        html_obj : html fetched
        soup : bs4 soup of html_obj
        :return: None
        """
        self.html_obj = requests.get(self.URL)
        self.soup = bs4.BeautifulSoup(self.html_obj.content, features="lxml")
        self.logMe.info('soup created, length: ' + str(len(self.soup)))

    def get_tag_data(self, tag_pattern):
        """Query the soup for tag_pattern

        :param tag_pattern: find this tag in the soup
        :return: None
        """
        self.extracted_tags = self.soup.find_all(re.compile(tag_pattern))
        for a_req_tag in self.extracted_tags:
            self.logMe.info('a_req_tag: ' + a_req_tag)
            pprintpp.pprint(a_req_tag)
            print(a_req_tag.previous_sibling)
            print(a_req_tag.next_sibling)
        print('Ends')

    def get_required_params(self):
        """AWS has many params for each action.
            This procedure lists only required params.
        """
        if self.soup is None:
            return
        else:
            bdts = self.soup.find_all('dt')
            bdds = self.soup.find_all('dd')
            indexid = 0
            pattern = re.compile(r'.*Required:\W(?P<req_yn>\w\w\w?)\W.*')
            print('{:<0}'.format(self.page_info))
            self.logMe.info('{:<0}'.format(self.page_info))
            for bdt in bdts:
                try:
                    ifmatched = pattern.search(bdds[indexid].text)
                    if 'Yes' in ifmatched.group(0).rstrip():
                        print('   {:<5} {:<40}'.format(bdt.text.lstrip().rstrip(), ifmatched.group(0).rstrip()))
                        self.logMe.info('   {:<5} {:<40}'.format(bdt.text.lstrip().rstrip(), ifmatched.group(0).rstrip()))
                except Exception:
                    continue
                indexid = indexid + 1

    def get_services_n_regions(self):
        self.URL = 'https://docs.aws.amazon.com/general/latest/gr/rande.html#rds_region')
        qHTML.get_url()
        if self.soup is None:
            return
        else:
            h2s = self.soup.find_all('h2')
            allrs = qHTML.soup.select('main-col-body h2')
            for i, a in enumerate(allrs, start=1):
                print(i, a)
