#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2014, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# pwm_led.py
# Make led to be bright and to be dark by software PWM
#
# Author : sosorry
# Date   : 06/22/2014

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)

pwm_led = GPIO.PWM(LED_PIN, 50)  # channel=12 frequency=50Hz
pwm_led.start(0)

try:
    while True:
        for dc in xrange(0, 101, 5):
            pwm_led.ChangeDutyCycle(dc)
            time.sleep(0.1)
        time.sleep(0.5)

        for dc in xrange(100, -1, -5):
            pwm_led.ChangeDutyCycle(dc)
            time.sleep(0.1)
        time.sleep(0.5)

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    pwm_led.stop()
    GPIO.cleanup()

