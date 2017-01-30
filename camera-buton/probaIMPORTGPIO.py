from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

GPIO.output(17,1)#manera booleana 1,true,high
sleep(3)
GPIO.output(17,0)#
sleep(3)

GPIO.cleanup()
