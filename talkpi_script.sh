#!/bin/sh

echo "Starting TALKPI PROCESS IN 5 sec ... "

sleep 5

echo "START \n"

sudo python //home/pi/talkpi.py > //home/pi/talkpi.log &
