import RPi.GPIO as GPIO
import os
import time

def toggle():
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(24,GPIO.OUT)
  print( "LED on" )
  GPIO.output(24,GPIO.HIGH)
  os.system('curl -X POST http://10.0.0.111/score/increment')
  #r = requests.post("http://10.0.0.111/score/increment")
  #print(r.status_code, r.reason)
  time.sleep(1)
  print( "LED off" )
  GPIO.output(24,GPIO.LOW)

while True:
  toggle()
  time.sleep(0.5)
