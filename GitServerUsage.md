# Git Server Usage
Accept your HOST_KEY is written into 
```sh
$ mykey_file >>  ~/.ssh/authorized_key
```
And you have a permission to the Git Server.
```sh
$ git remote add [YOUR_USER_NAME] root@[GIT_SERVER_IP]:/[REPOSITORY_PATH]
```
You have the remote acces to the git repository
You can start standart git process for versioning your own project.

## ROAD MAP 
For quality of code we are using Test on ./git/hooks files payloads:
	* post-checkout
	* pre-receive 'Push'	
	* pre-commit
	* post-receive 'Pushed to the repository'

We add the docker versioning to the hooks for CI duration.
