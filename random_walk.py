from turtle import Turtle, Screen
import random
import turtle as t

timmy = Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


screen = Screen()
move = [0, 90, 180, 270]
timmy.shape("turtle")

timmy.pensize(10)
timmy.speed("fast")

for _ in range(200):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(move))
for _ in range(40):
    timmy.circle(50)
screen.exitonclick()
