from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
tim.pensize(2)
tim.speed(10)
screen.colormode(255)
screen.title("Spirograph")
tim.hideturtle()

def random_colour():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    clr = (red, green, blue)
    return clr



# ALTERNATE STYLE OF SPIROGRAPH
times_left = 360 / 60
total_times_left = 60 / 10
j = 0
while j < total_times_left:
    colour = random_colour()
    tim.pencolor(colour)
    i = 0
    while i < times_left:
        tim.circle(100)
        # or
        # for _ in range(90):
        #     tim.left(4)
        #     tim.forward(2)
        tim.left(60)
        i += 1
    tim.left(10)
    j += 1
# 60 here is arbitrary (60 means 6 circles forming a sort of hexagon with its centers.
# 10 here is also arbitrary to choose the minimum gaps.
# i.e minimum offset angle of 10 degrees to continue with next 6 circles.
# therefore 60/10 = 6 times, the 6 circles are drawn.

#
# def draw_spiro(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         colour = random_colour()
#         tim.pencolor(colour)
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)

# draw_spiro(15)

screen.exitonclick()
