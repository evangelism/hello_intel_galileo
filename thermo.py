import sys
import time
from wiringx86 import GPIOGalileoGen2 as GPIO

def main(argv):
   print 'Starting up'
   gpio = GPIO(debug=False)
   for i in range(5):
      gpio.pinMode(8+i,gpio.OUTPUT)
   gpio.pinMode(19,gpio.ANALOG_INPUT)
   for i in range(4100):
      x = gpio.analogRead(19)
      print x
      n = (x-460)/30
      for j in range(5):
         if j<n: 
           s=gpio.HIGH 
         else: 
           s=gpio.LOW
         gpio.digitalWrite(8+j,s)
      time.sleep(0.1)
   print 'Done\n'
   gpio.cleanup()

main(sys.argv)
