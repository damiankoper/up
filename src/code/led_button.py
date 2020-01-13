#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
ledPin = 26
btnPin = 19

GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
ledOn = True
def button_callback(channel):
	global ledOn
	time.sleep(0.015)
	btnInput = GPIO.input(btnPin)
	if btnInput is GPIO.HIGH:
		if ledOn is True:
			ledOn = False
			print ("OFF")
			GPIO.output(ledPin, GPIO.LOW)
		else:
			ledOn = True
			print ("ON")
			GPIO.output(ledPin, GPIO.HIGH)			
GPIO.add_event_detect(btnPin,GPIO.RISING,callback=button_callback)



while True:
#	print ("OFF");
#	GPIO.output(ledPin, GPIO.LOW);
	time.sleep(0.001);
#	print ("ON");
#	GPIO.output(ledPin, GPIO.HIGH);
#	time.sleep(1);



