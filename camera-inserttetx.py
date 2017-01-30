from picamera import PiCamera
from time import sleep

camera=PiCamera()

camera.start_preview()
camera.annotate_text="Helo wordl!"
sleep(3)
#variable para el brillo de 0 a 100 por default esta en 50
camera.brightness=70
camera.capture('/home/pi/progra-python/image1.jpg')
camera.stop_preview()
