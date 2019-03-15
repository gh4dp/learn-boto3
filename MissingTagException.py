
class MissingTagException(Exception):
    def __init__(self):
        Exception.__init__(self, "BueatifulSoup Tag is missing Id attribute.")
