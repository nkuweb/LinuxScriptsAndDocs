# SYSADMIN and LINUX USERS DOCS AND SCRIPTS REPO
This repo has ready to use code for server management with Fabric


CODE SERVICES:
* backup_host(for centos)
* awake_apache(for centos)
* db_awake(mysql)
* setup docker
* mongodb

* NOTICE : Os-detector,More-Db-Options,More Details,Monitoring ... will be add. 


```sh
$ git clone https://github.com/nkudatascience/LinuxScriptsAndDocs
$ cd LinuxScriptsAndDocs
$ pip install -r requirements.txt
$ cd fabric
$ fab -H [SERVER_IP] [code_service]
```
# MONGODB
For get the backup of your db is simple.
	```sh
		$ mongodump --db [DB_NAME] --port [PORT_NAME]
	```
For restore this backup
	   ```sh
		$ mongorestore -d [DB_NAME] -c [COLLECTION_NAME] [DUMP_FILE.bson]
	   ```

