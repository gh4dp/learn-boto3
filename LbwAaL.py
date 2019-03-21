import logging


class LbwAaL:
    """A logging facility for entire module.
        Driver creates it and tosses around in other classes
    """
    def __init__(self):
        # create file handler which logs even debug messages
        fh = logging.FileHandler('learn-boto3.log')
        fh.setLevel(logging.DEBUG)

        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s\t%(levelname)s\t%(filename)s\t%(funcName)s\t%(lineno)d\t%(message)s')
        fh.setFormatter(formatter)

        # create logger
        self.logger = logging.getLogger('learn-boto3')
        self.logger.setLevel(logging.DEBUG)

        # add the handlers to the logger
        self.logger.addHandler(fh)
