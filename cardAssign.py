import flop
import random
import playerCount

cards = flop.cards
PACntr = 0
assign = []
players = playerCount.players
for x in players:
  for i in range(2):
    n = random.randint(0, len(cards)-1)
    assign.append(cards[n])
    cards.pop(n)
  players[x]= assign
  assign = []
  
  