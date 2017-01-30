from picamera import PiCamera
from time import sleep

camera=PiCamera()     
#opcion basica para un solo balance de blancos
camera.start_preview()
camera.awb_mode='flash'
sleep(5)
camera.capture('/home/pi/progra-python/flash.jpg')
camera.stop_preview()

