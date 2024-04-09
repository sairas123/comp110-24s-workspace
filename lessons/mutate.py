"""Mutating functions."""
__author__ = "730439074"


def manual_append(a:list[int],b:int) -> None:  #2 parameters and returns nothing
    """manual_append."""
    a.append(b)
num: list[int] = [1,2,3]
manual_append(num, 2)
print(num)

def double(a: list[int]) -> None:
    """"""
    l1_idx = 0   #iterates and "i" or "idx" ued to track loop
    while l1_idx < len(a):
        a[l1_idx] *= 2  #doubles it by 2
        l1_idx += 1
a: list[int] = [1,2,3]
double(a)
print(a)
