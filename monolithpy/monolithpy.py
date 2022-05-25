from os import path
from subprocess import PIPE
from subprocess import Popen
from subprocess import CalledProcessError

EXECUTABLE_PATH = f"{path.abspath(path.dirname(__file__))}/bin/monolith"
OPTS = {
    "no_audio": (bool, "-a"),
    "no_css": (bool, "-c"),
    "charset": (str, "-C"),
    "ignore_network_errors": (bool, "-e"),
    "omit_frames": (bool, "-f"),
    "no_webfonts": (bool, "-F"),
    "no_javascript": (bool, "-j"),
    "noscript_contents": (bool, "-n"),
    "output": (str, "-o"),
    "quiet": (bool, "-s"),
    "timeout": (int, "-t"),
    "user_agent": (str, "-u"),
    "no_video": (bool, "-v"),
    "no_image": (bool, "-i")
}


class Monolith:
	"""
	Options not yet added :
		-b: Use custom base URL
		-I: Isolate the document
		-k: Accept invalid X.509 (TLS) certificates
		-M: Don't add timestamp and URL information

	Available options :
		no_audio (bool) : Exclude audio sources
		no_css (bool) : Exclude CSS
		charset (str) : Save document using custom charset
		ignore_network_errors (bool) : Ignore network errors
		omit_frames (bool) : Omit frames
		no_webfonts (bool) : Exclude web fonts
		no_javascript (bool) : Exclude JavaScript
		noscript_contents (bool) : Extract contents of NOSCRIPT elements
		output (str) : Write output to file (use “-” for STDOUT)
		verbose (bool) : Be quiet
		timeout (int) : Adjust network request timeout
		user_agent (str) : Provide custom User-Agent
		no_video (bool) : Exclude videos
		no_image (bool) : Remove images
	"""
	def __init__(self, options: dict=None):
		self.options = {"output": "page.html"} if options is None else options

	def download_webpage(self, url):
		cmd_options = self.__parse_options(self.options)
		command = (EXECUTABLE_PATH, url) + cmd_options

		child_process = None
		try:
			child_process = Popen(command, shell=False, stdout=PIPE)
		except KeyboardInterrupt:
			child_process.kill()
		except CalledProcessError as process_error:
			print(f"An error occurred while running command. {type(process_error).__name__} {process_error}")
		else:
			while True:
				output = child_process.stdout.readline()
				if child_process.poll() is not None:
					break
				if output:
					print(output.strip().decode())
		finally:
			return child_process.returncode 

	@staticmethod
	def __parse_options(p_options: dict):
		for option, value in p_options.items():
			if option not in OPTS.keys():
				raise ArgsParseError(f"Unknown option '{option}'")
			elif not isinstance(value, OPTS.get(option)[0]):
				raise ArgsParseError(
					f"Invalid type for option '{option}'. " +
					f"'{type(value).__name__}' instead of '{OPTS.get(option)[0]}'")

		options = []
		for option, value in p_options.items():
			if not isinstance(value, bool):
				if option == "output":
					if (path.isdir(value) and path.exists(value)):
						output_file = path.join(value, "page.html")
					else:
						output_file = value
					options += [OPTS.get(option)[1], f"{output_file}"]
				else:
					options += [OPTS.get(option)[1], f"{value}"]
			else:
				if value is True:
					options.append(OPTS.get(option)[1])

		return tuple(options)


class MonolithException(Exception):
	"""Base class for monolith exceptions"""

class ArgsParseError(MonolithException):
	"""Raised when failed to parse options"""

