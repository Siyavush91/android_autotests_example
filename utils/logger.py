import logging

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=Singleton):
    def __init__(self):
        self.logs = ""
        self.soft_assert_fail = False

    def logs_info(self, value):
        self.logs += value + '\n'
        logging.info(value + '\n')

    def logs_exception(self, value):
        self.logs += value + '\n'
        logging.exception(value + '\n')

    def logs_warning(self, value):
        self.logs += value + '\n'
        logging.warning(value + '\n')

    def logs_debug(self, value):
        self.logs += value + '\n'
        logging.debug(value + '\n')

logger = Logger()
