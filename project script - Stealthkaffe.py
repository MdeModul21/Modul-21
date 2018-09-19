#Imported libs
from gpiozero import LED
from random import random
import time

#objects
LEDR = LED(21)
LEDG = LED(22)
LEDGR = LED(23)
RLEDGron = LED(12)
RLEDGul = LED(13)

#timers
delay1 = 5

var = 1
while var == 1:
    RLEDGron.on()
    RLEDGul.on()
    print("Stealth-mode engaged")
    kaffe =int(input("Initiate Brew sequence, press 1: "))
    print("")
    if kaffe == 1:
        print("Stealth-mode disengaging")
        RLEDGul.off()
        print("Brewing")
        print("")
        RLEDGron.off()
        time.sleep(10)
        print("Brewing complete")
        print("")
        print("Stealth-mode re-engaging...")
        print("")
        RLEDGul.on()
        RLEDGron.on()
    else:
        print("Error...")
        print("")
        print("Stealth-mode re-engaging...")
        print("")
        var == 1
        
