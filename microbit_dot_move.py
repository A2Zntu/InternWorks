from microbit import *


x = 2
y = 4
while True:
    display.set_pixel(x, y, 9)
    if button_a.was_pressed():
        display.set_pixel(x, y, 0)
        if x > 0:
            x -= 1
    elif button_b.was_pressed():
        display.set_pixel(x, y, 0)
        if x < 4:
            x += 1
	
	elif button_a.was_pressed and button_b.was_pressed():
		display.set_pixel(x, y, 0)
		if y > 0:
			y -= 1