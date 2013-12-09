# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [WIDTH/2,HEIGHT/2]
right=range(WIDTH/2,WIDTH-1-PAD_WIDTH)
paddle1_pos=[HALF_PAD_WIDTH,HEIGHT/2]
paddle2_pos=[WIDTH-HALF_PAD_WIDTH,HEIGHT/2]
paddle1_vel=[0,0]
paddle2_vel=[0,0]
ball_vel=[2,2]
score1=0
score2=0
# helper function that spawns a ball, returns a position vector and a velocity vector

# if right is True, spawn to the right, else spawn to the left
    
    
def ball_init(right):
    global ball_pos, ball_vel# these are vectors stored as lists
    ball_pos = [WIDTH/2,HEIGHT/2]
    ball_vel[0]= (random.randrange(120,240))/60 
    ball_vel[1]= (random.randrange(60,180))/60
    if right==True: 
        ball_vel[0] = ball_vel[0]
        ball_vel[1] = -ball_vel[1]
    if right==False:
        ball_vel[0] = -ball_vel[0]
        ball_vel[1] = -ball_vel[1]
    pass
    
    #The velocity of the ball should be upwards and towards the right if right == True
    #and upwards and towards the left if right == False

# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,ball_pos  # these are floats
    global score1, score2  # these are ints
    paddle1_pos=[HALF_PAD_WIDTH,HEIGHT/2]
    paddle2_pos=[WIDTH-HALF_PAD_WIDTH,HEIGHT/2]
    paddle1_vel=[0,0]
    paddle2_vel=[0,0]
    ball_vel=[1,2]
    score1=0
    score2=0
    ball_pos = [WIDTH/2,HEIGHT/2]

def draw(c):
    global WIDTH,HEIGHT,PAD_WIDTH,PAD_HEIGHT,score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[0]+=paddle1_vel[0]
    paddle1_pos[1]+=paddle1_vel[1]
    paddle2_pos[0]+=paddle2_vel[0]
    paddle2_pos[1]+=paddle2_vel[1]
   
    if paddle1_pos[1]<=HALF_PAD_HEIGHT:
        paddle1_pos[1]=HALF_PAD_HEIGHT
    elif paddle1_pos[1]>=(HEIGHT-1-HALF_PAD_HEIGHT):
        paddle1_pos[1]=HEIGHT-HALF_PAD_HEIGHT
    if paddle2_pos[1]<=HALF_PAD_HEIGHT:
        paddle2_pos[1]=HALF_PAD_HEIGHT
    elif paddle2_pos[1]>=(HEIGHT-1-HALF_PAD_HEIGHT):
        paddle2_pos[1]=HEIGHT-HALF_PAD_HEIGHT
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    # draw paddles
    c.draw_line([0, paddle1_pos[1]-HALF_PAD_HEIGHT],[0, paddle1_pos[1]+HALF_PAD_HEIGHT],PAD_WIDTH*2,'White')
    c.draw_line([WIDTH, paddle2_pos[1]-HALF_PAD_HEIGHT],[WIDTH,paddle2_pos[1]+HALF_PAD_HEIGHT],PAD_WIDTH*2,'White')

    # update ball
    
    if ball_pos[1] >= (HEIGHT-1-BALL_RADIUS) or ball_pos[1]<=BALL_RADIUS:
        ball_vel[0] = ball_vel[0]
        ball_vel[1] = -ball_vel[1]  
    
    if ball_pos[0] >= (WIDTH-1-BALL_RADIUS-PAD_WIDTH):
        if ((paddle2_pos[1]-HALF_PAD_HEIGHT) <= ball_pos[1]) and (ball_pos[1] <= (paddle2_pos[1]+HALF_PAD_HEIGHT)):
            ball_vel[0] = - ball_vel[0]
            ball_vel[0]=1.1*ball_vel[0]
            ball_vel[1]=1.1*ball_vel[1]
        else:
            ball_init(False)
            score1+=1
            
    if ball_pos[0]<=(PAD_WIDTH+BALL_RADIUS):
        if ((paddle1_pos[1]-HALF_PAD_HEIGHT)<= ball_pos[1]) and (ball_pos[1] <= (paddle1_pos[1]+HALF_PAD_HEIGHT)):
            ball_vel[0] = - ball_vel[0]
            ball_vel[0]=1.1*ball_vel[0]
            ball_vel[1]=1.1*ball_vel[1]       
        else: 
            ball_init(True)
            score2+=1
            
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1] 
        # draw ball and scores
    c.draw_circle(ball_pos,BALL_RADIUS,1,'White','White')
    c.draw_text(str(score1), [200,50], 30, 'White')
    c.draw_text(str(score2), [400,50],30,'White')

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP['w']:
        paddle1_vel[1] = -5
    elif key==simplegui.KEY_MAP['s']:
        paddle1_vel[1] = 5
    if key==simplegui.KEY_MAP['up']:
        paddle2_vel[1] = -5
    elif key==simplegui.KEY_MAP['down']:
        paddle2_vel[1] = 5
 
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP['w']:
        paddle1_vel[1] = 0
    elif key==simplegui.KEY_MAP['s']:
        paddle1_vel[1] = 0
    if key==simplegui.KEY_MAP['up']:
        paddle2_vel[1] = 0
    elif key==simplegui.KEY_MAP['down']:
        paddle2_vel[1] = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart",init, 100)



# start frame
init()
frame.start()