# game.py

r = "rock"
p = "paper"
s = "scissors"
options = [r, p, s]
import random
import os

from dotenv import load_dotenv

load_dotenv()

PLAYER_NAME = os.getenv("PLAYER_NAME", default="Player One")

print("-------------------")
print(f"Welcome {PLAYER_NAME} to my Rock-Paper-Scissors game...")
print("-------------------")

#asking user for an input

user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

user_choice = user_choice.lower()

#validate the user selection
#stop the program (not try to determine the winner)
#... if the user choice is invalid

if user_choice in options:
  print("You chose: ", user_choice)
else:
   print("The action you input is not valid. Try again next time!")
   exit()

#simulating a computer input

comp = random.choice(options)

print("The Computer chose: ", comp)

print("-------------------")
print()

print("Rock, Paper, Scissors, Shoot!")

print()
print("-------------------")

#determining who won

if user_choice == r and comp == s:
   print("Rock beats Scissors. You win!")
elif user_choice == r and comp == p:
   print("Paper beats Rock. You lose.")
elif user_choice == p and comp == s:
    print("Scissors beats Paper. You lose.")
elif user_choice == p and comp == r:
    print("Paper beats Rock. You win!")
elif user_choice == s and comp == p:
    print("Scissors beats Paper. You win!")
elif user_choice == s and comp == r:
    print("Rock beats Scissors. You lose.")
elif user_choice == comp:
    print(user_choice, " vs. ", comp, ". Tie!")

print("-------------------")

print("Thanks for playing. Please play again soon!")
print()
