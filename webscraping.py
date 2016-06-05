from lxml import html
from bs4 import BeautifulSoup
from urllib2 import urlopen
import requests
import random, time
import RPi.GPIO as GPIO

# Set GPIO to Broadcom system and set RGB Pin numbers
RUNNING = True
GPIO.setmode(GPIO.BCM)
red = 17
green = 18
blue = 21

# Set pins to output mode
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

Freq = 100 #Hz

# Setup all the LED colors with an initial
# duty cycle of 0 which is off
RED = GPIO.PWM(red, Freq)
RED.start(0)
GREEN = GPIO.PWM(green, Freq)
GREEN.start(0)
BLUE = GPIO.PWM(blue, Freq)
BLUE.start(0)

RED.ChangeDutyCycle(191)
GREEN.ChangeDutyCycle(87)
BLUE.ChangeDutyCycle(0)
time.sleep(600)

while 1:
    BASE_URL = 'http://whyisthetowerorange.com/'
    html = urlopen(BASE_URL).read()
    soup = BeautifulSoup(html, "lxml")
    reason = soup.select('div[id^=reason]')
    if "It's not" in str(reason[0]):
        print "It's not."
        RED.ChangeDutyCycle(0)
        GREEN.ChangeDutyCycle(0)
        BLUE.ChangeDutyCycle(0)
    else:
        print "The Tower is Orange"
        RED.ChangeDutyCycle(191)
        GREEN.ChangeDutyCycle(87)
        BLUE.ChangeDutyCycle(0)
    time.sleep(600)

