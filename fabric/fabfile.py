from fabric.api import run
from fabric.api import local
from fabric.operations import sudo, prompt, put
import os

def sendFile():
	path=raw_input("Path")
	put(path,None,False,True)
def get_backup(ip):
	os.system("backup.sh {0}".format(ip))
	os.system("bash add_cron")
def awake_db(db_name):
	os.system("db_awake.sh -d {0}".format(db_name))

def awake_apache():

def awake_nginx():

##Write Tests Git Integration
##ADD_CRON scriptlerinin ne zaman konusulacagini tartisalim.
