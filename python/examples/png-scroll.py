# NeoPixel library png-scroll example
# Author: Barry Staes (barry@staes.nl)
#
# Maps the X axis of a PNG file to the led strip, and scrolls through the Y axis with
# the specified FPS. Note a dark PNG looks (a lot) brighter on LEDs vs a tv/monitor. 

import time

from neopixel import *
from PIL import Image, ImageFilter # Install this with "pip install Pillow" 


# LED strip configuration:
LED_COUNT   = 64      # Number of LED pixels.
LED_PIN     = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA     = 5       # DMA channel to use for generating signal (try 5)
LED_INVERT  = False   # True to invert the signal (when using NPN transistor level shift)


def showImageScroll(strip, image, fps):
	"""Show image scrolling"""
	for y in range(0, original.size[1]):
		for x in range(0, original.size[0]):
			r, g, b = rgb_im.getpixel((x, y)) # slow and values not sanitized
			strip.setPixelColor(x, Color(r,g,b))
			#print "pixel %s,%s is %02x,%02x,%02x" % (x,y,r,g,b)
		strip.show()
		time.sleep(1.0 / fps) # above code also takes time: actual FPS is lower

# Main program logic follows:
if __name__ == '__main__':


	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
	# Intialize the library (must be called once before other functions).
	strip.begin()


	# Read bitmap
	original = Image.open("sparkles.png")
	rgb_im = original.convert('RGB')


	print 'Press Ctrl-C to quit.'
	while True:
		showImageScroll(strip, rgb_im, 25);
