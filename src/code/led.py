#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM);
ledPin = 26;
GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.HIGH);
while True:
	print ("OFF");
	GPIO.output(ledPin, GPIO.LOW);
	time.sleep(1);
	print ("ON");
	GPIO.output(ledPin, GPIO.HIGH);
	time.sleep(1);