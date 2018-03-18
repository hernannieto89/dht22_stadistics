import os
import sys

import RPi.GPIO as GPIO
import Adafruit_DHT


def setup(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    sensor = Adafruit_DHT.DHT22
    return sensor


def check_sudo():
    """
    Checks for superuser privileges.
    :return: None
    """
    if os.getuid() != 0:
        print >> sys.stderr, "You need to have root privileges to run this script.\n" \
                             "Please try again, this time using 'sudo'. Exiting."
        sys.exit(1)
