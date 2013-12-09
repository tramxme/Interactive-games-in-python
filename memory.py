# implementation of card game - Memory

import simplegui
import random

#cards: 
cards=range(8)*2  
cards_pos=[0,80]
random.shuffle(cards)
exposed=[False]*16
track=[]
moves=0
state=0
card1=-1
card2=-1
# helper function to initialize globals
def init():
    global state,cards,exposed
    state = 0
    random.shuffle(cards)
    exposed=[False]*16
    card1=-1
    card2=-1
    moves=0
    l.set_text('Moves ='+str(moves))
    print cards    
    
# define event handlers
def mouseclick(pos):
    global state, moves,card1, card2
    index=pos[0]//50
    #if the card already open, don't do anything
    if exposed[index]:
        return
    #if the card is not open, open it
    exposed[index] = True
    #Open the first card
    if state == 0:
        card1=index
        state = 1
    #Open the second card
    elif state == 1:
        card2=index
        state = 2
    #Open the third card
    else:
        #If the first and second card are different, flip them back
        if cards[card1]!=cards[card2]: 
            exposed[card1]=False
            exposed[card2]=False
        #If they show the same card, keep them open, the third card become the 1st card    
        card1=index
        state = 1
        moves += 1
    l.set_text('Moves ='+str(moves))


# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards,exposed
    for n in range(16):
        if exposed[n]==True:
            canvas.draw_text(str(cards[n]),[0+50*n,80],75, 'white')
        else:
            canvas.draw_polygon([[0+50*n,0],[50+50*n,0],[50+50*n,100],[0+50*n,100]],1, 'white','blue')
    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
l=frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
