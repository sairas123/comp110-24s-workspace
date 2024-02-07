"""EXO1 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730439074"

Blue_Box: str = "\U0001F7E6"
White_Box: str = "\U00002B1C"
Red_Box: str = "\U0001F7E5"

boat = int(input("Pick a secret boat location between 1 and 4: "))
if boat < 1:
    print(" Error!", boat, "too low!")
    exit()
if boat > 4:
    print("Error!", boat, "too high!")
    exit()
    
num = int(input("Guess a number between 1 and 4: "))

if num < 1:
    print(f"Error! {num} is an invalid guess.")
    exit()
   
if num > 4:
    print(f"Error! {num} is an invalid guess.")
    exit()

answer = Red_Box 

if num == boat:
    answer = Red_Box
else:
    answer = White_Box

emoji_chain = ""

if num == 1:
    emoji_chain += answer
else:
    emoji_chain += Blue_Box

if num == 2: 
    emoji_chain += answer
else:
    emoji_chain += Blue_Box

if num == 3:
    emoji_chain += answer
else: 
    emoji_chain += Blue_Box

if num == 4: 
    emoji_chain += answer
else:
    emoji_chain += Blue_Box

print(emoji_chain)

if num == boat: 
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")