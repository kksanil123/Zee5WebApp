import configparser

config = configparser.RawConfigParser()
config.read(r'./Configuration/config.ini')


class ReadConfig:
    @staticmethod
    def get_app_url():
        return config.get('App info', 'app_url')
