# rock-paper-scissors-exercise

Iteratively develop a command-line Python application which will allow a human user to play a game of Rock-Paper-Scissors against a computer (NPC) opponent

## Set-up

Use GitHub to create a new remote project repository called "rock-paper-scissors-exercise." Be sure to add a "README.md" file and a ".gitignore" file (specifying Python) when prompted.

After this is complete, download or "clone" the repo onto your computer.

Then navigate to where you downloaded the copy from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd rock-paper-scissors-exercise
```
Use the text editor to create a file in that repo called "game.py," and then place the following contents inside:

#game.py

print("Rock, Paper, Scissors, Shoot!")

## Environment Setup

Create and activate a new project-specific Anaconda virtual environment:

```sh
conda create -n my-game-env python=3.8 # (first time only)
conda activate my-game-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

From within the virtual environment, demonstrate your ability to run the Python script from the command-line:

```sh
python game.py
```

If you see the "Rock, Paper, Scissors, Shoot!" message, you are ready to move on to project development.

## Asking User for Input

The application should prompt the user to input an option ("rock", "paper", or "scissors") via command-line interface. It should then store the input for later reference.

```sh
user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")
```

## Validating User Inputs

The application should then ensure that what the user input is a valid option ("rock", "paper", or "scissors"). If the selection is invalid, the program should fail gracefully by displaing a friendly message to the user, and preventing further program execution. The program should not try to further process an invalid input, as it may lead to runtime errors.

Also want to ensure that variations of the options are allowed. Display the choice made or the fail message after validation.

```sh
#make the user_choice all lower case so it is consistent with options
user_choice = user_choice.lower()

#validate the user selection

r = "Rock"
p = "Paper"
s = "Scissors"

#make a list that contains all of the options

options = [r, p, s]

if user_choice in options:
  print("You chose: ", user_choice)
else:
   print("The action you input is not valid. Try again next time!")
   exit()

```

## Simulating Computer Selection

The application should select one of the options ("rock", "paper", or "scissors") at random and assign that as the computer player's choice.

First need to import the random package to randomize the computer selection

```sh
import random
```

Then you can select one of the options from the list and display the result.

```sh
comp = random.choice(options)

print("The Computer chose: ", comp)
```

## Play the game

Print out code to explain that you are now playing the game.

```sh
print("-------------------")
print()

print("Rock, Paper, Scissors, Shoot!")

print()
print("-------------------")
```

## Determining the Winner & Displaying Results

The application should compare the user's selection to the computer player's selection, and determine which is the winner. The following logic should govern that determination:

1. Rock beats Scissors
2. Paper beats Rock
3. Scissors beats Paper
4. Rock vs Rock, Paper vs Paper, and Scissors vs Scissors each results in a "tie"

Once the winner is determined, display the pairing and the ultimate result. Then print a farewell message

```sh

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
```

## Customizing the Player Name

The user is allowed to configure their own player name by passing an environment variable called "PLAYER_NAME" stored in a local ".env" file.

To get started, import the module that is necessary when working with a ".env" file

```sh
import os
```

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username:

    PLAYER_NAME="Your name here"

Use the following code to take the environment variables from .env and assign it to a variable.

```sh
from dotenv import load_dotenv

load_dotenv()

PLAYER_NAME = os.getenv("PLAYER_NAME", default="Player One")

print("-------------------")
print(f"Welcome {PLAYER_NAME} to my Rock-Paper-Scissors game...")
print("-------------------")
```
