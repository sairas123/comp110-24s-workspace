"""Functional Battleship."""

__author__ = "730439074"

import random


BLUE_BOX: str = "\U0001F7E6"
WHITE_BOX: str = "\U00002B1C"
RED_BOX: str = "\U0001F7E5"

# part 1:
def input_guess(grid_size: int, specif_type: str) -> int :
    """Setting up grid sizes."""
    assert specif_type == "row" or specif_type == "column"
 
    if specif_type == "row":
        guess = int(input("Guess a row: "))
        while guess < 1 or guess > grid_size:
            guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

    else:
        guess = int(input("Guess a column: "))
        while guess < 1 or guess > grid_size:
            guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

    return guess

    
#part 2
def print_grid(grid_size:int, row_guess: int, guess_column: int, correct: bool) -> None:
   """User's row and column guesses: """
   row_counter = 1 
   while row_counter <= grid_size:
        emoji_chain = ""
        column_counter = 1   
        if row_guess == row_counter:
            while column_counter <= grid_size:
                if guess_column == column_counter: 
                    if correct:
                        emoji_chain += RED_BOX
                    else:
                        emoji_chain += WHITE_BOX
                else:
                    emoji_chain += BLUE_BOX
                column_counter += 1  # increase column counter by one so you dont have an infinite loop
        else:
            while column_counter <= grid_size:
                emoji_chain += BLUE_BOX
                column_counter += 1  # to avoid an infinite loop
         print(emoji_chain)
        row_counter += 1


    #part 3
def correct_guess(secret_row:int, secret_column: int, guess_row:int, guess_column:int) -> bool :
    """Determine if the user was correct or not."""
    if secret_row == guess_row and secret_column == guess_column:
        return True
    else:
        return False

#part 4
def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Pull all smaller pieces together."""
    turn = 0 
    max_turns = 5
    won = False

    while turn < max_turns and not won: 
        turn += 1
        print(f"=== Turn {turn}/{max_turns} ===")
        guess_row: int = input_guess(grid_size, "row")
        guess_column: int = input_guess(grid_size, "column")
        #prompt usder for a row input guess
        if correct_guess(secret_row, secret_column,guess_row, guess_column):
            print_grid(grid_size, guess_row, guess_column, True)
            print("Hit!")
            print(f"You won in {turn}/{max_turns} turns!")
            won = True
        else:
            print_grid(grid_size, guess_row, guess_column, False)
            print("Miss!")
    if turn >= 5:
        print(f"X/{max_turns}- Better luck next time!") #refers to print_grid

if __name__ ==  "__main__":
   grid_size: int = random.randint(3, 5)
   main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))