import logging
from pprint import pformat
class Logger:

    def __init__(self):
        self.stream = None
        self.init_stream()

    def init_stream(self):
        """Configures stream messaging"""

        # Get the logger
        self.stream = logging.getLogger('cognition-to-fasttext')

        # Prevent duplicate messages
        self.stream.propagate = False

        # Set logger level
        self.stream.setLevel(logging.DEBUG)

        # Add the file handler
        fh = logging.FileHandler('app.log')
        fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        fh.setLevel(logging.DEBUG)
        self.stream.addHandler(fh)

        # Add the stream handler
        sh = logging.StreamHandler()
        sh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.stream.addHandler(sh)


    def debug(self, m, extra=None, stream=True):
        """
        Logs a `debug`-level message

        :param m: message
        :param extra: dict of extra variables
        :return: None
        """
        if stream:
            if extra is None:
                self.stream.debug(m)
            else:
                self.stream.debug('{}\n{}\n'.format(m, pformat(extra)))


    def info(self, m, extra=None, stream=True):
        """
        Logs an `info`-level message

        :param m: message
        :param extra: dict of extra variables
        :return: None
        """
        if stream:
            if extra is None:
                self.stream.info(m)
            else:
                self.stream.info('{}\n{}\n'.format(m, pformat(extra)))


    def warn(self, m, extra=None, stream=True):
        """
        Logs a `warning`-level message

        :param m: message
        :param extra: dict of extra variables
        :return: None
        """
        if stream:
            if extra is None:
                self.stream.warn(m)
            else:
                self.stream.warn('{}\n{}\n'.format(m, pformat(extra)))

    def error(self, m, extra=None, stream=True):
        """
        Logs an `error`-level message

        :param m: message
        :param extra: dict of extra variables
        :return: None
        """
        if stream:
            if extra is None:
                self.stream.error(m)
            else:
                self.stream.error('{}\n{}\n'.format(m, pformat(extra)))


    def exception(self, e):
        """
        Logs an `error`-level message

        :param e: exception
        """
        self.stream.exception(e)

log = Logger()