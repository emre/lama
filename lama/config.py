import os
import ConfigParser


config_file = os.path.expanduser("~/.imgur.conf")


def get_client_id():

    if not os.path.exists(config_file):
        raise IOError("you need to create a config file as ~/.imgur.conf")

    parser = ConfigParser.RawConfigParser()
    parser.read(config_file)

    return parser.get("client", "id")
