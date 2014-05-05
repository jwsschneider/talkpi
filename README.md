talkpi
======

Simple Raspberry Pi program that reads a script after a button is pushed.


**About:**

I built this project to make a cardboard box talk when you push its button. It represents my first application of the Raspberry Pi's GPIO pins, LEDs, and switches.

The project has a blinking LED (status indicator) and a big red button. When the red button is pressed, the LED burns solid while a the program runs eSpeak (http://espeak.sourceforge.net/), a command-line text-to-speech application. It reads a script stored on a USB flash drive, so it can be easily swapped out. When the speaking is over, the LED starts blinking again and the button can be pressed again.

**Video of talkpi in action:**



**Setup:**

I built stockpi on a Raspberry Pi (Model B, 256 MB RAM) running Raspian (wheezy) 3.10. The code is written in Python. It eSpeak (http://espeak.sourceforge.net/). Installing eSpeak on your RPi is dead easy (http://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Espeak_Text_to_Speech). Because stockpi uses the Raspberry Pi's GPIO pins, you have to import the RPi.GPIO library. RPi.GPIO is included in the latest versions of Raspian, but there are instructions to download it here (http://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/) if you don't already have the library.

I designed the application to run without a monitor, keyboard, or mouse so it could be strapped to the back of a cardboard box. To ensure that it starts on boot, I created a cron job (run as sudo):

```
@reboot  //home.pitalkpi/talkpi.sh
```

When you see the blinking status LED, you'll know that the application is running and listening for the button press!


**Circuit Diagram:**

![Alt text](https://raw.githubusercontent.com/jwsschneider/talkpi/master/images/talkpi_circuit_diagram.png)


**License:**

All of the code and supporting files in the talkpi git repository are licensed under the Creative Commons Attribution-ShareAlike 4.0 International Public License (https://creativecommons.org/licenses/by-sa/4.0/legalcode and https://creativecommons.org/licenses/by-sa/4.0/). Anyone is free to take and modify the files as long as the attribution to its original author is maintained and the modifier agrees to, in turn, license his/her modified files under the Creative Commons Attribution-ShareAlike 4.0 International Public License, too.
