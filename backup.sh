echo "WELCOME the BACKUP SYSTEM"
TIME=`date +%b-%d-%y`
tar -cvpzf $TIME.tar.gz /
scp -r $TIME.tar.gz $1:$2
echo "Backup End!"
