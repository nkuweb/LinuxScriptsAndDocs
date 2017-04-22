from __future__ import with_statement
from fabric.operations import sudo, prompt, put
import os
from fabric.api import *
env.disable_known_hosts = True


def run_main_script(file_name):
	main_script = open(file_name)
	run(main_script)

def awake_apache():
	apache_scripts = open("awake_apache.sh")
	run(apache_scripts)

def sendFile():
	path=raw_input("Path")
	put(path,None,False,True)

def get_backup():
	run_main_script("backup.sh")
	run_main_script("add_cron.sh")

def awake_db(db_name):
	run_main_script("db_awake.sh")

'''def awake_nginx():
##Write Tests Git Integration
##ADD_CRON scriptlerinin ne zaman konusulacagini tartisalim.
'''
