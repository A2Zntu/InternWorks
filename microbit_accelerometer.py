from microbit import *

while True:
	if accelerometer.was_gesture("down"):
		display.show(Image.ARROW_N)
	elif accelerometer.was_gesture("up"):	
		display.show(Image.ARROW_S)
	elif accelerometer.was_gesture("left"):	
		display.show(Image.ARROW_W)
	elif accelerometer.was_gesture("right"):	
		display.show(Image.ARROW_E)
	
