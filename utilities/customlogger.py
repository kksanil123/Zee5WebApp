import logging


class LogGen:

    @staticmethod
    def get_logger():
        logging.basicConfig(filename=r'/home/PycharmProjects/Zee5WebApp/Logs/automation.log',
                            format='%(asctime)s, %(levelname)s, %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger