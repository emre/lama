from __future__ import print_function

import requests
import os
import datetime
import base64
import config
import platform


class Commands(object):

	def __init__(self):
		self.platform = platform.system()

	SCREENSHOT_COMMANDS = {
		"Linux": "scrot -s {0}",
		"Darwin": "",
	}

	CLIPBOARD_COMMANDS = {
		"Linux": "xsel --clipboard --input",
		"Darwin": "",
	}

	NOTIFY_COMMANDS = {
		"Linux": 'notify-send "{0}"',
		"Darwin": "",
	}

	def take(self):
		return self.SCREENSHOT_COMMANDS.get(self.platform)

	def copy_to_clipboard(self):
		return self.CLIPBOARD_COMMANDS.get(self.platform)

	def send_notification(self):
		return self.NOTIFY_COMMANDS.get(self.platform)


class ScreenShotUploader(object):

	def __init__(self):
		self.commands = Commands()
		self.client_id = config.get_client_id()
		self.target_path = None

	def get_file_name(self):
		return datetime.datetime.now().strftime("%Y_%M_%d_%H%M%s.png")

	def take_screenshot(self, target_path=None):
		if not self.target_path:
			self.target_path = os.path.expanduser("~/imgur_uploads")
			if not os.path.exists(self.target_path):
					os.mkdir(self.target_path)
			os.chdir(self.target_path)

		file_name =  self.get_file_name()

		os.system(self.commands.take().format(file_name))

		self.upload_to_imgur(file_name)

	def upload_to_imgur(self, file_name):

		response = requests.post(
		    "https://api.imgur.com/3/upload.json", 
		    headers = {"Authorization": "Client-ID {0}".format(self.client_id)},
		    data = {
		        'image': base64.b64encode(open(os.path.join(self.target_path, file_name), 'rb').read()),
		        'type': 'base64',
		        'name': file_name,
		    }
		)

		data = response.json()
		if data.get("status") == 200:
			print(data.get("data").get("link"))
			os.system("echo {0} | {1}".format(data.get("data").get("link"), self.commands.copy_to_clipboard()))
			os.system(self.commands.send_notification().format("Upload completed. Image url pasted to clipboard."))


		else:
			if 'error' in data.get("data"):
				print(data.get("data").get("error"))


def main():
	ss = ScreenShotUploader()
	ss.take_screenshot()

if __name__ == '__main__':
	main()
