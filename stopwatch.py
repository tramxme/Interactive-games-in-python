# template for "Stopwatch: The Game"
import simplegui


# define global variables
number = 0
x=0
y=0
trace=0
# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D

def format(number):
    global A,B,C,D
    if number <= 9: 
        A = 0
        B = 0
        C = 0
        D = number
    elif number > 9 and number <100:
        A = 0
        B = 0
        C = number//10
        D = number%10
    elif number >= 100 and number<600:
        A = 0
        B = number//100
        C = (number%100)//10
        D = (number%100)%10
    elif number>=600:
        A = number//600
        new_num = number%600
        if new_num<=9:
            B = 0
            C = 0
            D = new_num
        elif new_num > 9 and new_num<100:
            B = 0 
            C = new_num//10
            D = new_num%10
        elif new_num >=100:
            B = new_num//100
            C = (new_num%100)//10
            D = (new_num%100)%10
    return str(A)+':'+str(B)+str(C)+'.'+str(D)        
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"

# define event handler for timer with 0.1 sec interval

def incr():
    global number
    number = number + 1 

def draw_handler(canvas):
    global number, x, y
    canvas.draw_text(format(number), (100,150), 30 ,'red')
    canvas.draw_text(str(x), (260,30), 15,'red')
    canvas.draw_text('/', (270,30),15,'red')
    canvas.draw_text(str(y), (280,30), 15,'red')
    
   
def button_handler1():
    global trace,number
    incr()
    timer.start()
    trace=0
    
    
def button_handler2():
    global trace, x, y
    timer.stop()
    trace = trace +1
    if trace ==1:
        y = y + 1
        if number%10==0:
            x = x + 1
    
    
def button_handler3():
    global number, x, y 
    number = 0
    x = 0
    y = 0 
    
# create frame
frame = simplegui.create_frame("Stop watch", 300, 300)
timer = simplegui.create_timer(100, incr)
frame.set_draw_handler(draw_handler)
frame.add_button('Start', button_handler1, 50)
frame.add_button('Stop', button_handler2, 50)
frame.add_button('Reset', button_handler3, 50)
# register event handlers

# start timer and frame
frame.start()