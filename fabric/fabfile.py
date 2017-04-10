
from fabric.api import run
from fabric.api import local
from fabric.operations import sudo, prompt, put


def host_type():
	local ("uname -s")
def make_file():
	local ("mkdir hallo")
def say_hello():
	local("echo Hello")
def sendFile():
	path=raw_input("Path")
	put(path,None,False,True)
##Write Tests Git Integration

