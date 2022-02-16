### Interfacing With the Raspberry Pi
## MODULE 4 
#Connect an LED to your Raspberry Pi and write a program to gradually increase brightness, and then gradually decrease brightness. 
#The exact rate of increase and decrease is not critical but let it take at least one second to go from maximum to minimum brightness. 
#Be sure to use pulse width modulation to change the brightness of the LED. Also, be sure to wire the LED in series with an appropriate 
#resistor so that it does not receive too much current.

# Link to demo video: 

# R > (3.3-1.8/0.02) = 75 --> 3.3 is high voltage of pin set as output, 1.8 is voltage drop across LED, and 0.02 is the maximum current of the led
# using 270 Ohm resistor

import RPi.GPIO as GPIO # Import GPIO library so you can manipulate general purpose pins
import time # Import time library to use sleep function

GPIO.setmode(GPIO.BOARD) # Could be .BOARD (pin numbering) or .BCM (Broadcom SOC channel names)
GPIO.setup(18, GPIO.OUT) # Set pin 18 on BOARD as output 
pwm = GPIO.PWM(18, 50) # Initialize PWM on pwmPin (18) at 50 kHz frequency 
pwm.start(0) # Start PWM with 0% duty cycle (low)

for i in range(0, 100, 1): # Loop from 0 to 99 (low to high) --> setting 100 throws ValueError: dutycyle must have value from 0.0 to 100.0
	pwm.ChangeDutyCycle(i)
	time.sleep(0.01) # Wait for 0.01 seconds at current LED brightness, so that it takes approx. 1 second to go from min to max brightness

for i in range(100, 0, -1): # Loop from 99 to 0 (decrements by 1)
	pwm.ChangeDutyCycle(i)
	time.sleep(0.01) # Approx. 1 second to go from max to min brightness

pwm.stop() # Stop PWM
GPIO.cleanup() # Resets GPIO ports used back to input mode