# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
message=''
show=0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards=[]
        
    def __str__(self):
        lst=[]
        for Card in self.cards:
            lst.append(str(Card))
        return str(lst)
        
    def add_card(self, Card):
        self.cards.append(Card)
        return self.cards
            
    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
    def get_value(self):
        self.point=0
        for i in range(len(self.cards)):
            if self.cards[i][1] in VALUES:
                self.point=self.point+VALUES[self.cards[i][1]]
                if "A"==self.cards[i][1]:
                    if self.point + 10 <= 21:
                        self.point =  self.point + 10
                    else: 
                        self.point = self.point
        return self.point        
        
    def busted(self):
        self.go_busted=False
        if self.point > 21: 
            self.go_busted=True
        else: 
            self.go_busted=False
        return self.go_busted
    
    def draw(self, canvas, p):
        for Card in self.cards: 
            pass 
        
# define deck class
class Deck:
    def __init__(self):
        self.deck=[]
        for suit in SUITS: 
            for rank in RANKS:
                self.deck.append(suit+rank)
        return self.deck
    
    # add cards back to deck and shuffle
    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop(0)
    
    
    def __str__(self):
        return str(self.deck)

            


#define event handlers for buttons
def deal():
    global outcome, in_play, score, message, my_deck, player, dealer, my_deck, show
    player=Hand()
    dealer=Hand()
    my_deck=Deck()
    my_deck.shuffle()
    in_play = True
    player.go_busted = False
    dealer.go_busted = False
    show=0
    player.cards=[]
    dealer.cards=[]
    my_deck
    player.add_card(my_deck.deal_card())
    player.add_card(my_deck.deal_card())
    dealer.add_card(my_deck.deal_card())  
    dealer.add_card(my_deck.deal_card())
    message="Hit or Stand?"
    outcome=''
    
    
def hit():
    global in_play ,outcome, message, score, player, dealer, my_deck, show
    # if the hand is in play, hit the player
    if in_play: 
        player.add_card(my_deck.deal_card())
        player.get_value()
        player.busted()
    # if busted, assign an message to outcome, update in_play and score
        if player.go_busted: 
            show=1
            outcome="You went bust and lose"
            message="New deal?"
            in_play=False
            score-=1
            
def stand():
    global in_play,score, outcome, player, dealer, message, my_deck, show
    show= 1
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        dealer.get_value()
        player.get_value()
        while dealer.get_value()< 17: 
            dealer.add_card(my_deck.deal_card())  
            dealer.get_value()
            dealer.busted()
    # assign a message to outcome, update in_play and score
        if dealer.go_busted:
            outcome="You won"
            score+=1
        else:    
            if dealer.get_value()>=player.get_value():
                score-=1
                outcome="You lost"       
            elif dealer.get_value()<player.get_value():
                score+=1
                outcome="You won"
        message='New deal?'        
        in_play=False
        
        
        
# draw handler    
def draw(canvas):
    global dealer, player, show
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack",(100,100),45,'orange')
    canvas.draw_text("Score:" + str(score),(400,100),20,'black')
    canvas.draw_text("Dealer",(100,200),25,'black')
    canvas.draw_text(outcome,(300,200),25,'black')
    canvas.draw_text("Player",(100,400),25,'black')
    canvas.draw_text(message,(300,400),25,'black')
    canvas.draw_image(card_back,CARD_BACK_CENTER, CARD_BACK_SIZE, [100 + CARD_BACK_CENTER[0], 250 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    for i in range(1, len(dealer.cards)):
        dealer_card = Card(dealer.cards[i][0],dealer.cards[i][1])
        dealer_card.draw(canvas,[99+120*i,249])
    for j in range(len(player.cards)):
        player_card = Card(player.cards[j][0],player.cards[j][1])
        player_card.draw(canvas, [99+120*j,450])
    if show==1:     
        dealer_card = Card(dealer.cards[0][0],dealer.cards[0][1])
        dealer_card.draw(canvas,[99,249])


# initialization frame
frame = simplegui.create_frame("Blackjack", 700, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# deal an initial hand
deal()

# get things rolling
frame.start()

