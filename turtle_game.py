from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = False
color_list = ["red", "green", "yellow", "orange", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
screen.setup(width=600,height=500)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which Turtle will win the race? Enter a color:")
all_turtle = []

# create multiple abject with different colors and defferent position and add to empty list
# create multiple abject and instance from on class and act on each one is individual
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-280,y=y_position[turtle_index])
    new_turtle.color(color_list[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 280:
            is_race_on = False
            winnning_color = turtle.pencolor()
            if winnning_color == user_bet:
                print(F"you've won! the {winnning_color} turtle is the winner🥰")
            else:
                print(f"you've lose! the {winnning_color} turtle is the winner💔")

        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)

screen.exitonclick()

