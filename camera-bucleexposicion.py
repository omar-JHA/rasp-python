from picamera import PiCamera
from time import sleep

camera=PiCamera()
camera.start_preview()
vec=['off','auto','night','nightpreview','backlight','spotlight','sports','snow','beach','verylong','antishake','fireworks']
for x in range(0,12,1):
     camera.exposure_mode=vec[x]
     camera.annotate_text="exposicion:%s"%vec[x]
     sleep(3)
camera.stop_preview()
