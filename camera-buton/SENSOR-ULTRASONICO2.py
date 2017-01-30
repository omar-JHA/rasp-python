import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
Trigger=10
Echo=12

GPIO.setup(Trigger,GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)

print "sensor ultrasonico"
try:
    while True:
        GPIO.output(Trigger,False)
        time.sleep(0.5)
        
        GPIO.output(Trigger,True)
        time.sleep(0.00001)

        GPIO.output(Trigger,False)
        inicio=time.time()

        while GPIO.input(Echo)==0:
            inicio=time.time()
        while GPIO.input(Echo)==1:
            final=time.time()
            
        transcurrido=final-inicio
        distancia=transcurrido*3400
        distancia=distancia/2
        print "Distancia=%.1fcm"%distancia
except KeyboardInterrupt:
    GPIO.cleanup()
