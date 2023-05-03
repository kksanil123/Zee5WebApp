import logging


class LogGen:

    @staticmethod
    def get_logger():
        logging.basicConfig()
        logger = logging.getLogger()
        return logger




