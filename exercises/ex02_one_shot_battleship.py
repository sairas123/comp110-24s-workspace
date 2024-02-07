"""One Shot Battleship."""

__author__ = "730439074"

Blue_Box: str = "\U0001F7E6"
White_Box: str = "\U00002B1C"
Red_Box: str = "\U0001F7E5"
 
grid_size = 4 
secret_row = 3
secret_column = 2

# prompt user to guess row and column 
# Has to be an int

guess_row = int(input("Guess a row:"))

while guess_row < 1 or guess_row > grid_size:
    print(f"The grid is only {grid_size} by {grid_size}. Try again:")
    guess_row = int(input("Guess a row:"))

# print("Guess a column:")
guess_column = int(input("Guess a column:"))

while guess_column < 1 or guess_column > grid_size:
    print(f"The grid is only {grid_size} by {grid_size}. Try again:")
    guess_column = int(input("Guess a row:"))

if guess_row == secret_row and guess_column == secret_column:
    print("HIT!")
elif guess_row == secret_row:  # purpose of elif statements is to give a hint
    print("Correct row, wrong column")
elif guess_column == secret_column:
    print("correct column, wrong row")
else:
    print("Miss!")

row_counter = 1  # ROW COUNTER


while row_counter <= grid_size:
    emoji_chain = ""
    column_counter = 1  # COLUMN COUNTER starting at 1   
    if guess_row == row_counter:
        while column_counter <= grid_size:
            if guess_column == column_counter:  # if equal concatenate result bow (red or white) to the row string
                if guess_column == secret_column:
                 emoji_chain += Red_Box
                else:
                    emoji_chain += White_Box 
            else:
                emoji_chain += Blue_Box
            column_counter += 1  # increase column counter by one so you dont have an infinite loop
    else:
        while column_counter <= grid_size:
            emoji_chain += Blue_Box
            column_counter += 1  # to avoid an infinite loop
        # emoji_chain += Blue_Box
    row_counter += 1
    print(emoji_chain)