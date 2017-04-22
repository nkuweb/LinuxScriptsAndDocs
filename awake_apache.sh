YOUR_INTERFACE = arg
sudo apt-get update
sudo apt-get install apache2
sudo service apache2 restart
i=0
x=$(ifconfig $arg | grep inet | awk '{ print $2 }')

echo "LOOk the second line above  write it your browser."
