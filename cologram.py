# import colorgram
import random
from turtle import Turtle, Screen
import turtle as t

timmy = t.Turtle()
screen = Screen()
t.colormode(255)

rgb_color = [(246, 244, 243), (233, 239, 245), (240, 245, 242), (246, 239, 241), (132, 166, 204), (220, 148, 108),
             (32, 41, 60), (197, 136, 149), (41, 106, 155), (141, 183, 162), (164, 59, 49), (237, 212, 93),
             (147, 61, 68), (214, 83, 73), (52, 111, 91), (34, 61, 56), (233, 167, 159), (157, 33, 30), (170, 29, 33),
             (15, 99, 71), (170, 189, 220), (229, 162, 166), (54, 45, 49), (57, 52, 48), (31, 60, 109), (178, 105, 115),
             (108, 126, 158), (175, 200, 188), (35, 150, 209), (65, 66, 56)]

# colors = colorgram.extract('image1.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_color.append(new_color)
# timmy.onclick(50, btn=1, add=None)


timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
num_of_dots = 101

for dot_count in range(1, num_of_dots):
    timmy.dot(20, random.choice(rgb_color))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen.exitonclick()