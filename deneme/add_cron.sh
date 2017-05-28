crontab -l > script
echo "* 24 * * * bash backup.sh" >> mycron
