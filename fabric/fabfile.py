from __future__ import with_statement
from fabric.operations import sudo, prompt, put
import os
from fabric.api import *
env.disable_known_hosts = True

def run_main_script(file_name):
		script_file = open('{0}'.format(file_name))
		run(script_file.read())
		script_file.close()


def backup_host():
	run_main_script("backup_host.sh")

def awake_apache():
	run_main_script ("awake_apache.sh")


'''def awake_nginx():
##Write Tests Git Integration
##ADD_CRON scriptlerinin ne zaman konusulacagini tartisalim.
def sendFile():
	path=raw_input("Path")
	put(path,None,False,True)


def awake_db(db_name):
	run_main_script("db_awake.sh")
	TIME=`date +%b-%d-%y`
	sudo tar czf /$TIME.tar.gz --exclude=/backup.tar.gz --exclude=/home --exclude=/media --exclude=/dev --exclude=/mnt --exclude=/proc --exclude=/sys --exclude=/tmp /
	scp -r $TIME.tar.gz $1:$2
	echo "Backup End!"

'''
