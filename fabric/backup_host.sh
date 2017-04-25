
TIME=`date +%b-%d-%y`
sudo tar czf /$TIME.tar.gz --exclude=/backup.tar.gz --exclude=/home --exclude=/media --exclude=/dev --exclude=/mnt --exclude=/proc --exclude=/sys --exclude=/tmp /

echo "Backup End!"
