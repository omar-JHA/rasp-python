from picamera import PiCamera
from time import sleep

camera=PiCamera()
#multiples balances de blancos 
vec=['off','auto','sunlight','cloudy','shade','tungsten','fluorescent','incandescent','flash','horizon']
camera.start_preview()
for x in range(0,9,1):
     camera.awb_mode=vec[x]
     camera.annotate_text="balance:%s"%vec[x]
     sleep(3)
camera.stop_preview()
