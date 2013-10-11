import os
import ConfigParser


config_file = os.path.expanduser("~/.imgur.conf")

def get_client_id():

	parser = ConfigParser.RawConfigParser()
	parser.read(config_file)

	return parser.get("client", "id")
