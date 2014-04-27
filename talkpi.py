#!/usr/bin/env python

'''
Created on Nov 22, 2013

@author: jwsschneider

License: All of the code and supporting files in the talkpi git repository are licensed under the Creative Commons Attribution-ShareAlike 4.0 International Public License (https://creativecommons.org/licenses/by-sa/4.0/legalcode and https://creativecommons.org/licenses/by-sa/4.0/). Anyone is free to take and modify the files as long as the attribution to its original author is maintained and the modifier agrees to, in turn, license his/her modified files under the Creative Commons Attribution-ShareAlike 4.0 International Public License, too.

'''

import RPi.GPIO as GPIO
import time
import os

# main function
def main():

    GPIO.setmode(GPIO.BOARD) # set up the GPIO pins
    GPIO.setwarnings(False) # suppress warnings

    GPIO.setup(12,GPIO.IN) # setup pin 12 as an input for button (switch)

    GPIO.setup(11,GPIO.OUT) # setup pin 11 as an LED output
   

    ‘’’
    tell the GPIO library to look out for an 
    event on pin 12
    ‘’’
    GPIO.add_event_detect(12, GPIO.FALLING, bouncetime=200)

    # loop and wait for the button to be pressed
    while True:

	# if the button is pressed, we enter this block of code
        if (GPIO.event_detected(12)):
            print "Button pressed at " + str(time.time()) # print when button was pressed to output log
            GPIO.output(11,True) # convert the blinking LED to a solid-burn to indicate that we’re playing the talking script now
            ‘’’
            This is the line of code that is executed on the command line when the button is pressed. There is nothing
            preventing you from changing this line of code to something else (playing music, for example). I have the 
            code executing espeak and reading a text script located on a USB drive. That way, a user can just swap out the
            USB drive’s text file to make the program say different things.
            ‘’’
            os.system('espeak -v us-mbrola-2 -f /media/C070-1328/text_db.txt --stdout | aplay')

            # reset the event detection
            GPIO.remove_event_detect(12)
            GPIO.add_event_detect(12, GPIO.FALLING, bouncetime=200)
	
	# make the LED flash on and off to indicate that we’re in the loop, but the button hasn’t been pressed yet
        GPIO.output(11,True)
	time.sleep(1)
	GPIO.output(11,False)
	time.sleep(1)

    # always cleanup your GPIO pins before exiting. Otherwise, the LEDs may continue to burn after exit!
    GPIO.cleanup()
    GPIO.output(11,False) # shut off the LED status light for good


# launch program
if __name__=="__main__":
    main()


