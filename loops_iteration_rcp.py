# Chapter 5 - Rock Paper Scissors vs 3
import random

def choose_rps():
    "output: randomly returns rock, paper, or scissors"
    r = random.randint(0,2)
    if r == 0:
        return "rock"
    elif r == 1:
        return "scissors"
    else:
        return "paper"

def rps(player1, player2):

  if player1 == player2:
    print('it\'s a tie!')
  elif (player1 == 'rock' and player2 == 'scissors') or (player1 == 'scissors' and player2 == 'paper') or (player1 == 'paper' and player2 == 'rock'):
    print ('player 1 wins!')
  else:
     print ('player 2 wins!')

rps(choose_rps(),choose_rps())

def play_again():
  r = random.randint(0,1)
  if r == 0:
    return True
  else:
    return False

i=0
for i in range(1,2):
  print('Let\'s pay again!')
  rps(choose_rps(),choose_rps())
