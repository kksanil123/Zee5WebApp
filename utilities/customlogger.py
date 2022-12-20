import logging


class LogGen:

    @staticmethod
    def get_logger():
        logging.basicConfig(filename=r'..\Logs\automation.log',
                           format='%(asctime)s: %(levelname)s: %(message)s:', datefmt='%Y-%m-%d %H:%M:%S')

        logger = logging.getLogger()
        logger.setLevel(20)
        return logger


# LogGen().get_logger().info('JUNK 11')



