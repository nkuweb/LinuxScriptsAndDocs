
from fabric.api import run
from fabric.api import local
def host_type():
	local ("uname -s")
def make_file():
	local ("mkdir hallo")
def say_hello():
	local("echo Hello")
##Write Tests Git Integration

