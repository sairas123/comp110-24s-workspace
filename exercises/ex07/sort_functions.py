"""Functions that implement sorting algorithms."""

__author__ = "730439074"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    for index in range(1, len(x)): #iterates through the list
        current_element = index 
        current_value = x[current_element]
        #compares current values and swaps the two elements;has to be 1 greater than the value of sorted
        while current_element > 0 and current_value < x[current_element -1]:
            x[current_element], x[current_element-1] = x[current_element -1], current_value
            current_element -= 1


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    for index in range (len(x)):   #less than counter value which is the sorted portion
        minimum_element = index 
        for i in range (index + 1, len(x)): #minimum element in an unsored portion of a list and if smaller then swap it with current element
            if x[i] < x[minimum_element]:
                minimum_element = i 
        if minimum_element != index:
            x[index], x[minimum_element] = x[minimum_element], x[index]
    