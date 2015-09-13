import time
import RPi.GPIO as GPIO
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
while True:
  GPIO.output(7,GPIO.LOW)
  GPIO.output(8,GPIO.HIGH)
  time.sleep(0.05)
  GPIO.output(8,GPIO.LOW)
  GPIO.output(7,GPIO.HIGH)
  time.sleep(0.05)

