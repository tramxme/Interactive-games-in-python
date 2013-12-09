# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random

# initialize global variables used in your code
secret_num=0
number_guesses=0
range_min=0
range_max=100

# define event handlers for control panel
def init():
    global range_min, range_max, number_guesses, secret_num
    range_min = 0
    secret_num = random.randrange(range_min, range_max)
    number_guesses = math.ceil(math.log(range_max-range_min + 1, 2))
    print 'New game. Range is', range_min,'to', range_max
    print 'Number of remaining guesses is', number_guesses

    
    # button that changes range to range [0,100) and restarts
def range100():
    global secret_num,range_max,number_guesses
    range_max = 100
    init()
    # button that changes range to range [0,1000) and restarts
def range1000():
    global secret_num,range_max,number_guesses
    range_max = 1000
    init()
    # main game logic goes here 
def get_input(guess):
    global secret_num, number_guesses
    number_guesses = number_guesses - 1 
    num = int(guess)
    print 'Guess was', num
    print 'Number of remaning guesses is', number_guesses
    if num == secret_num and number_guesses >= 0:
        print 'Correct!'
        init()
    elif num > secret_num and number_guesses > 0: 
        print 'Lower!'
    elif num < secret_num and number_guesses > 0:
        print 'Higher!'
    elif number_guesses == 0:
        print 'You ran out of guesses. The number is', secret_num
        init()
    
# create frame
frame=simplegui.create_frame('Guess a number',300,300)
init()
# register event handlers for control elements
frame.add_button('Range in [0,100)',range100,200)
frame.add_button('Range in [0,1000)',range1000,200)
frame.add_input('Enter a number',get_input,200)

# start frame
frame.start()

# always remember to check your completed program against the grading rubric
