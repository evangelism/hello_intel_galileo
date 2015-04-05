import sys
import time
from wiringx86 import GPIOGalileoGen2 as GPIO

def main(argv):
   print 'Starting up'
   gpio = GPIO(debug=False)
   gpio.pinMode(8,gpio.OUTPUT)
   for i in range(4):
      print 'Hi\n'
      gpio.digitalWrite(8,gpio.HIGH)
      time.sleep(0.5)
      print 'Lo\n'
      gpio.digitalWrite(8,gpio.LOW)
      time.sleep(0.5)
   print 'Done\n'
   gpio.cleanup()

main(sys.argv)
