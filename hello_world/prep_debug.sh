#!/bin/bash
if [ $# -lt 2 ]; then
    echo "Missing param"
    echo "Usage: $0 <project name> <IP>"
    exit 1
fi
echo test: $1



DOCKER_IMAGE_NAME='kai-boards-host'
LOGIN_USER='kai'
LOGIN_PASSWORD='sigmastar'
TARGETIP=$2
EXECUTABLE=$1
TMPPATH=/tmp/kai_dbg

#kill gdbserver on target
sshpass -p $LOGIN_PASSWORD ssh $LOGIN_USER@$TARGETIP killall gdbserver &> /dev/null 
# create temporary folder
sshpass -p $LOGIN_PASSWORD ssh $LOGIN_USER@$TARGETIP mkdir -p $TMPPATH
# remove old executable on target
sshpass -p $LOGIN_PASSWORD ssh $LOGIN_USER@$TARGETIP rm $TMPPATH/$EXECUTABLE
# make the target
docker exec $DOCKER_IMAGE_NAME arm-linux-gnueabihf-gcc -g /Kai/IoThings-GUI-PyQT-Kai/hello_world/${EXECUTABLE}.c -o /Kai/IoThings-GUI-PyQT-Kai/hello_world/$EXECUTABLE
# copy over new executable
sshpass -p $LOGIN_PASSWORD scp -o 'StrictHostKeyChecking no' $EXECUTABLE $LOGIN_USER@$TARGETIP:$TMPPATH/$EXECUTABLE
# start gdb on target (IS ONE LONG COMMAND)
sshpass -p $LOGIN_PASSWORD ssh -n -f $LOGIN_USER@$TARGETIP "nohup gdbserver localhost:3000 $TMPPATH/$EXECUTABLE > /dev/null 2>&1 &"