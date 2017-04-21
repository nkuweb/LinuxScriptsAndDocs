from fabric.api import run
from fabric.api import local
from fabric.operations import sudo, prompt, put
import os

def host_type():
	local ("uname -s")
def make_file():
	local ("mkdir hallo")
def say_hello():
	local("echo Hello")
def sendFile():
	path=raw_input("Path")
	put(path,None,False,True)
def get_backup(ip):
	os.system("backup.sh {0}".format(ip))
	os.system("bash add_cron")

##Write Tests Git Integration
##ADD_CRON scriptlerinin ne zaman konusulacagini tartisalim.
