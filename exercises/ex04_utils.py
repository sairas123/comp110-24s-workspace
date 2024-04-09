"""List Utility Functions!"""   

__author__ = "730439074"


def all(input1: list[int], input2: int) -> bool:
    """If all the numbers within the input list match then it will return true, else it will return false."""
    if len(input1) == 0:   
        return False

    for num in input1:
        if num != input2:
            return False   

    return True   


def max(input: list[int]) -> int:
    """Returns the max number in the list and if it isn't raises a 'value error'."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")

    current_max = input[0]  
    for num in input:
        if num > current_max:
            current_max = num

    return current_max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns True based on if the lists contain the same elements all in the same order otherwise else False."""
    if len(list1) != len(list2):  
        return False

    for idx in range(len(list1)):
        if list1[idx] != list2[idx]:
            return False

    return True  


def extend(list1: list[int], list2: list[int]) -> None:  
    """Appends the elements into list1."""
    for num in list2:
        list1.append(num) 