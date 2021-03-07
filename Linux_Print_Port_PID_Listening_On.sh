#!/bin/bash

# script.sh PID

set -e

 

if [ -z "$1" ]

  then

    echo "No argument supplied"

fi

 

longPortNumber=$(/usr/sbin/lsof -Pan -p $1 -i -sTCP:LISTEN)

# echo $longPortNumber

port=$(/usr/sbin/ss -l -p -n | grep "$1,"| awk '{ print $5; }'| awk -F':' '{print $2}')

ipaddress=$(/usr/sbin/ss -l -p -n | grep "$1,"| awk '{ print $5; }'| awk -F':' '{print $1}')

echo $port

echo $ipaddress