#!/bin/python3
iter = 0
players = {}
playerCnt = int(input("How many players? 2+ : "))
for i in range(playerCnt):
  iter += 1
  tadd = str(input(f"Player {iter} name: "))
  players[tadd]= ""

print(players)