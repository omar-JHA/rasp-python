from picamera import PiCamera
from time import sleep

camera=PiCamera()
camera.resolution=(64,64)
camera.framerate=15
camera.start_preview()
sleep(5)
camera.capture('/home/pi/progra-python/image.jpg')
camera.stop_preview()
