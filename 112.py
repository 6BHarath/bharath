#!/usr/bin/python3
import random

op = ["Rock","Paper","Scissors"]
AI = op[random.randint(0,2)]
user = input("Pick either Rock, Paper or Scissors: ")
user = user.lower()
print("you chosse",user,"ai chosse",AI)
if user == 'rock' or 'paper' or 'scissors':
    print ("The computer has drawn",AI, "whilst you have drawn ",user)
if user == 'rock':
    if AI == 'Rock':
        print ('Tie Game')
    elif AI == 'Paper':
        print ('AI Wins')
    else:
        print ('User Wins')
if user == 'paper':
    if AI == 'Rock':
        print ('User Wins')
    elif AI == 'Paper':
        print ('Tie Game')
    else:
        print ('AI Wins')
if user == 'scissors':
    if AI == 'Rock':
        print ('AI Wins')
    elif AI == 'Paper':
        print ('User Wins')
    else:
        print ('Tie Game')
