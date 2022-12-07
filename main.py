import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_index = [-100, -60, -20, 20, 60, 100]
all_turtles = []
# tim = Turtle(shape="turtle")
# tim.color(random.choice(colors))
# tim.penup()
# tim.goto(x=-230, y=-100)

for t_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[t_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_index[t_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle win")
            else:
                print(f"You lose! The {winning_color} turtle win")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
print(all_turtles)