import configparser

config = configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")


class Readconfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'amazon')
        return url

