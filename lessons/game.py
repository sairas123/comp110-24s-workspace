"""Number guessing game."""
from random import randint

Secret: int = randint (1,5)
correct: bool = False

while correct == False: # not correct
    guess: int = int(input("Guess a number: "))
    if guess == Secret: 
        print(f"You got it right! {guess} is the secret number!")
        correct = True
    else:
        if guess <= Secret :
            print("Too low, try again!")
        if guess >= Secret:
            print("Too high, try again!")
        
