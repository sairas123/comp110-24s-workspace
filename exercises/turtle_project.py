"""Turtle project: A colorful Abstract house."""

_author_ = 730439074

from turtle import Turtle, colormode, done
leo: Turtle = Turtle() 
MAX_SPEED = 0
leo.speed(MAX_SPEED)
 

def main() -> None:
    """The entrypoint of my scene."""
    leo.color("blue")
    square(leo, -50, -50, 100)  # house base
    triangle(leo, -25, 55, 80)  # roof
    square(leo, -30, 0, 30)  # left window
    square(leo, 20, 0,30)  # right window
    rectangle(leo, 10, -50, 40, 60)  # door at the center
    circle(leo, 35, -20, 5)  # doorknob
    done()


def square(a_turtle: Turtle, x: float, y: float, size: float) -> None:
    """A blue square for a house base."""
    leo.goto(x, y)
    leo.begin_fill()
    # leo.penup()
    # leo.pendown()

    for x in range(4):
        leo.forward(size)
        leo.right(90)
    leo.end_fill()
        
    
def triangle(a_turtle: Turtle, x: float, y: float, size: float) -> None:
    """draw a yellow triangle for the roof with equal sides."""
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.color("yellow")
    leo.begin_fill()

    for x in range(3):
        leo.forward(size)
        leo.left(120)  # 120 degree for equilateral triangle 

    leo.end_fill()


def window(a_turtle: Turtle, x: float, y: float, size: float) -> None:
    """Draw two yellow square window."""
    leo.goto(x, y) 
    leo.color("yellow")
    leo.begin_fill()

    for x in range(4):
        leo.forward(size)
        leo.left(90)

    leo.end_fill()


def rectangle(a_turtle: Turtle, x: float, y: float, width: float, height: float) -> None: 
    """Draw a pink rectangle door."""
    leo.goto(x, y)
    leo.penup()
    leo.pendown()
    leo.color("pink")
    leo.begin_fill()

    for x in range(2):
        leo.forward(width)
        leo.left(90)
        leo.forward(height)
        leo.left(90)

    leo.end_fill()


def circle(a_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """A circular Doorknob."""
    leo.goto(x, y - radius)
    leo.penup()
    leo.pendown()
    leo.begin_fill()
    leo.circle(radius)
    leo.end_fill()


if __name__ == "__main__":
    main()