from turtle import *
import random

# Set up the screen
screen = Screen()
screen.colormode(255)
screen.setup(width=800, height=800)
screen.title("Spot Paintings")


# Generate a random RGB color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# Set up the turtle
raana = Turtle()
raana.speed(0)
raana.penup()
raana.hideturtle()

# Set initial values
radius = 40
dots = 6

# Draw colorful circular patterns
for x in range(6):
    angle = 360 / dots

    for y in range(dots):
        raana.goto(0, 0)
        raana.setheading(y * angle)
        raana.forward(radius)
        raana.dot(25, random_color())

    # Increase the radius and number of dots
    radius += 50
    dots += 6

# Keep the window open until clicked
screen.exitonclick()