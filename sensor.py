from time import sleep
import random 
import Adafruit_DHT
import RPi.GPIO as GPIO

verde = 16
amarillo = 20
rojo = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(verde,GPIO.OUT)
GPIO.setup(amarillo,GPIO.OUT)
GPIO.setup(rojo,GPIO.OUT)

pinSensor = 12
sensor = Adafruit_DHT.DHT11
datos = Adafruit_DHT.read(sensor,pinSensor)

#humedad = datos[0]
humedad = random.randint(10,100)

if humedad < 40:
    GPIO.output(rojo, GPIO.HIGH)
elif humedad >= 40 and humedad <= 60:
    GPIO.output(amarillo, GPIO.HIGH)
elif humedad >= 61:
    GPIO.output(verde, GPIO.HIGH)

sleep(1)
GPIO.output(rojo, GPIO.LOW)
GPIO.output(amarillo, GPIO.LOW)
GPIO.output(verde, GPIO.LOW)