import RPi.GPIO as GPIO
import time
import random
from functools import partial


def main():

    GPIO.setmode(GPIO.BCM)
    init_LEDs()
    init_buttons()

    while(True):
        s = make_sequence()
        show_lights(s)
        buttons = get_button_sequence(len(s))
        is_right = check_sequence(buttons, s)
        if is_right:
            celebrate()
        else:
            fail()
        time.sleep(0.5)

def celebrate():
    print('You got it')
    for x in range(0,10):
        GPIO.output( (15), True)
        time.sleep(0.1)
        GPIO.output( (15), False)
        GPIO.output( (18), True)
        time.sleep(0.1)
        GPIO.output( (18), False)
        GPIO.output( (23), True)
        time.sleep(0.1)
        GPIO.output( (23), False)
        GPIO.output( (24), True)
        time.sleep(0.1)
        GPIO.output( (24), False)
    time.sleep(2)

def fail():
    print('Nope.. sorry')
    GPIO.output( (15, 18, 23, 24), True)
    time.sleep(0.5)
    GPIO.output( (15, 18, 23, 24), False)

def check_sequence(buttons, sequence):
    if buttons == sequence:
        return True
    else:
        return False

def get_button_sequence(number):
    global buttons
    buttons = []
    while(len(buttons) < number):
        time.sleep(0.5)
    return buttons[:number]


def make_sequence():
        

    sequence = []
    sequence.append(random.choice([23,18,15,24]))

    for x in range(0, 5):
            
        sequence.append(random.choice([23,18,15,24]))

    #print('Sequence is: %s'%(sequence))
    return sequence



def show_lights(sequence):
        
    for LED in sequence:


        GPIO.setup(LED, GPIO.OUT)
        GPIO.output(LED, True)
        time.sleep(.5)
        GPIO.output(LED,False)
        time.sleep(.5)


buttons = []

times_clicked = 0
def button_callback(in_pin,led,channel):
    global buttons
    if GPIO.input(in_pin):
        print('.', end='', flush=True)
        #print(led)
        buttons.append(led)
        #print(buttons)

def init_buttons():
    GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(26, GPIO.RISING, callback=partial(button_callback,26,24))
    GPIO.add_event_detect(19, GPIO.RISING, callback=partial(button_callback,19,23))
    GPIO.add_event_detect(13, GPIO.RISING, callback=partial(button_callback,13,18))
    GPIO.add_event_detect(6, GPIO.RISING, callback=partial(button_callback,6,15))

def init_LEDs():
    for LED in (15,18,23,24):
        GPIO.setup(LED, GPIO.OUT)


main()


