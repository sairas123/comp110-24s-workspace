"""Dictionary Utility Functions."""   

__author__ = "730439074"

import pytest
from exercises.ex05.dictionary import invert

def invert(input1: dict[str, str]) -> dict[str, str]:
    """Return a dictionary that inverts the keys and values otherwise raise KeyError."""
    result = {}
    for key, value in input1.items():
        if value not in result:
            result[value] = key
        else: 
            print(f"same key found: {value}. KeyError.")
    return result

# part 2
def favorite_color(input2: dict[str, str]) -> str:
    """Return which color appears the most when given a string of colors."""
    frequency: dict[str, int] = {} 
    highest_count = 0 

    for person, color in input2.items():
        frequency[color] = frequency.get(color, 0) + 1
        for color, count in frequency.items():
            if count > highest_count:
                most_frequent_color = color
                highest_count = count
    return most_frequent_color


# part 3
def count(input: list[str]) -> dict[str, int]:
    """Returns a dictionary of the values of each item in the list."""
    counts: dict[str, int] = {}
    for value in input:
        if value in counts:
            counts[value] += 1 
        else:
            counts[value] = 1
    return counts 

# part 4
def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Organizes words by the first letter of the word."""
    categorized_words: dict[str, list[str]] = {}
    for word in input:
        first_letter = word[0].lower()
        if first_letter not in categorized_words:
            categorized_words[first_letter] = []
        #else:
        categorized_words[first_letter].append(word)
    return categorized_words

#part 5
def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """ Returns the attendance log with the students name for each of the given days."""
    if day not in attendance:
        attendance[day] = [student]
    else:
        if student not in attendance[day]:
            attendance[day].append(student)
