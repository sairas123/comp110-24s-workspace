"""Tutle tutorial"""

__author__ = "730439074"

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

i: int = 0
while (i < 4):
    leo.forward(300)
    leo.left(90)
    i = i + 1
