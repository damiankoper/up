#!/bin/bash
PIN=26
echo $PIN > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio${PIN}/direction
while true; do
	echo 0 > /sys/class/gpio/gpio${PIN}/value
	echo "OFF"
	sleep 1s
	echo 1 > /sys/class/gpio/gpio${PIN}/value
	echo "ON"
	sleep 1s
done
