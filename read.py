import sys
import time
from wiringx86 import GPIOGalileoGen2 as GPIO

def main(argv):
   print 'Starting up'
   gpio = GPIO(debug=False)
   gpio.pinMode(19,gpio.ANALOG_INPUT)
   for i in range(30):
      x = gpio.analogRead(19)
      print x
      time.sleep(0.5)
   print 'Done\n'
   gpio.cleanup()

main(sys.argv)
