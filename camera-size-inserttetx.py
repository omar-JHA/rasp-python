from picamera import PiCamera
from time import sleep

camera=PiCamera()

camera.start_preview()
#ajuste de texto de 6 a 160 por default esta en 32
camera.annotate_text_size=6
camera.annotate_text="Helo wordl!"
sleep(3)
#variable para el brillo de 0 a 100
camera.brightness=70
camera.capture('/home/pi/progra-python/image1.jpg')
camera.stop_preview()
