from microbit import *


temp = temperature()
temp = temp*9/5 + 32

while True:
	display.scroll(temp)