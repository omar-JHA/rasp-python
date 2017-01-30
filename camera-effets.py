#efectos de camara 
from picamera import PiCamera
from time import sleep

camera=PiCamera()
camera.resolution=(1080,1500)
camera.start_preview()
camera.image_effect='deinterlace2'
sleep(5)
camera.capture('/home/pi/progra-python/deinterlace2.jpg')
camera.stop_preview()
