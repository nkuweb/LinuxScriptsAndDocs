x= ifconfig en0 | grep inet | awk '{ print $2 }'
echo $x
