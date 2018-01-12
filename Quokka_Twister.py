import quokka
import random

r = 0
g = 0
b = 0

colours =  ['RED', 'GREEN', 'YELLOW', 'BLUE']
sides = ['LEFT', 'RIGHT']
limbs = ['HAND', 'FOOT']

start_statements = ['Ready?', '3' , '2', '1']

quokka.radio.enable()
quokka.radio.config(channel=6)

timer = 2
lives = 2

#show colour on neopixels

def colour_show(current_colour, r, g, b):
    if current_colour == 'RED':
        r = 255
    if current_colour == 'GREEN':
        g = 255
    if current_colour == 'YELLOW':
        r =255
        g =150
    if current_colour == 'BLUE':
        b =255
    quokka.neopixels.clear()
    for i in range(8):
        quokka.neopixels.set_pixel(i, r, g, b)
        quokka.neopixels.show()
        quokka.sleep(5)

#show side on display
'''def side_show(current_side):
    quokka.display.fill(1)
    quokka.display.text(current_side, 5, 5, 0)
    quokka.display.show()'''

#temporary limb and side
def show_body(current_limb, current_side):
    quokka.display.fill(1)
    quokka.display.text((current_side + '' + current_limb), 5, 5, 0)
    quokka.display.show()

#reset the turn - screen, timer, colours, neopixels
def turn_reset():
    quokka.sleep(timer*1000)
    r = 0
    g = 0
    b = 0
    quokka.display.fill(1)
    quokka.display.show()
    quokka.neopixels.clear()
    quokka.neopixels.show()
    timer = timer*0.8
    quokka.sleep(500)

def start_sequence():
    for word in start_statements:
        quokka.display.fill(1)
        quokka.display.text(word, 5, 5, 0)
        quokka.display.show()
        quokka.sleep(1000)
    quokka.display.fill(1)
    quokka.display.show()

quokka.neopixels.clear()
quokka.neopixels.show()
quokka.display.fill(0)

while True:
    # start screen

    if quokka.buttons.a.was_pressed():
        start_sequence()

        #Twister

        if lives > 0:

        #Gameplay positions

            # colour show and select
            current_colour = random.choice(colours)
            colour_show(current_colour, r, g, b)

            '''#Side select
            current_side = random.choice(sides)
            side_show(current_side)
            #Limb select
            current_limb = random.choice(limbs)
            limb_show(current_limb)'''

            #temporary body:
            current_limb = random.choice(limbs)
            current_side = random.choice(sides)
            side_show(current_side)

            print(current_colour + ' ' + current_body)
            turn_reset()
