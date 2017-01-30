from picamera import PiCamera
from time import sleep
from gpiozero import Button

button=Button(17)#es el GPIO17
camera=PiCamera()

camera.start_preview()
button.wait_for_press()
camera.capture('/home/pi/progra-python/camera-buton/image2.jpg')
camera.stop_preview()
