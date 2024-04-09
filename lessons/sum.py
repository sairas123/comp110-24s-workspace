"""Summing the elements of a list using different loops."""

__author__ = "730439074"

def w_sum(vals: list[float]) -> float:
    total_sum = 0.0
    idx: int = 0.0
    while idx < len(vals):
        total_sum += vals[idx]
        idx += 1 
    print(total_sum)

def f_sum(vals):
    total = 0.0
    for val in vals:
        total += val
    print(total)

def f_range_sum(vals):
    total = 0.0
    for index in range(0.0, len(vals)):
        total += vals[index]
    print(f"{total}") 



