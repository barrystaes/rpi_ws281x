# NeoPixel library colors example
# Author: Barry Staes (barry@staes.nl)
#
# Simplest example, of use to measure electrical current and brightnes.

import time

from neopixel import *


# LED strip configuration:
LED_COUNT   = 64      # Number of LED pixels.
LED_PIN     = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA     = 5       # DMA channel to use for generating signal (try 5)
LED_INVERT  = False   # True to invert the signal (when using NPN transistor level shift)


# Define functions which animate LEDs in various ways.
def colorAll(strip, c, wait_s):
	"""Show color"""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, c)
	strip.show()
	time.sleep(wait_s)


# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print 'Press Ctrl-C to quit.'
	while True:
                # Base colors
		print 'White'
		colorAll(strip, Color(255,255,255), 5) # White
		print 'Red'
		colorAll(strip, Color(255,  0,  0), 5) # Red
		print 'Green'
		colorAll(strip, Color(  0,255,  0), 5) # Green
		print 'Blue'
		colorAll(strip, Color(  0,  0,255), 5) # Blue
		print 'Black'
		colorAll(strip, Color(  0,  0,  0), 5) # Black

                # Mixed colors
		print 'Mixed: White 50%'
		colorAll(strip, Color(127,127,127), 5) # White 50%
		print 'Mixed: White 2%'
		colorAll(strip, Color(  5,  5,  5), 5) # White  2%
		print 'Mixed: Red + Green = Yellow'
		colorAll(strip, Color(255,255,  0), 5) # Yellow
		print 'Mixed: Green + Blue = Cyan'
		colorAll(strip, Color(  0,255,255), 5) # Cyan
		print 'Mixed: Blue + Red = Purple'
		colorAll(strip, Color(255,  0,255), 5) # Purple
		print 'Black'
		colorAll(strip, Color(  0,  0,  0), 5) # Black
