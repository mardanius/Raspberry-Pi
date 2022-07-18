import RPi.GPIO as GPIO
from time import sleep # Import the sleep function from the time module

verde = 16 
amarillo = 20
rojo = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(verde,GPIO.OUT)
GPIO.setup(amarillo,GPIO.OUT)
GPIO.setup(rojo,GPIO.OUT)

#GPIO.output(led1,GPIO.HIGH)
#GPIO.output(led1,GPIO.LOW)

while True: # Run forever
    # rojo
    GPIO.output(rojo, GPIO.HIGH) # Turn on
    sleep(3)                  # Sleep for 1 second
    GPIO.output(rojo, GPIO.LOW)  # Turn off

    # Amarillo
    GPIO.output(amarillo, GPIO.HIGH) # Turn on
    sleep(1)                  # Sleep for 1 second
    GPIO.output(amarillo, GPIO.LOW)  # Turn off

    # Verde
    GPIO.output(verde, GPIO.HIGH) # Turn on
    sleep(5)                  # Sleep for 1 second
    GPIO.output(verde, GPIO.LOW)  # Turn off

    # Amarillo
    GPIO.output(amarillo, GPIO.HIGH) # Turn on
    sleep(1)                  # Sleep for 1 second
    GPIO.output(amarillo, GPIO.LOW)  # Turn off
    
    
    
    