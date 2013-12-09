# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random
def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    
def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4

def rpsls(guess): 
    player_number= name_to_number(guess)
    comp_number = random.randrange(0,5)
    difference = player_number - comp_number
    if difference==0:
        print 'Player chooses', number_to_name(player_number)
        print 'Computer chooses', number_to_name(comp_number)
        print 'Tie!'
    elif difference%4==0 or difference%4==1:
        print 'Player chooses', number_to_name(player_number)
        print 'Computer chooses', number_to_name(comp_number)
        print 'Player wins!'
    elif difference % 4 ==2 or difference %4 == 3:
        print 'Player chooses', number_to_name(player_number)
        print 'Computer chooses', number_to_name(comp_number)
        print 'Computer wins!'
    return ''
print rpsls("rock")
print rpsls("Spock")
print rpsls("paper")
print rpsls("lizard")
print rpsls("scissors")

