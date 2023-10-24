from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
colors = ["red", "yellow", "purple", "orange", "blue"]


i= -100
turtles = []
continue_game = True

for element in colors:
    new_turtle = element
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(element)
    turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.goto(-230, i)
    i+=50

while continue_game:
    for object in turtles:
        if object.xcor() >= 230:
            continue_game= False
            if user_bet == object.pencolor():
                print(f"You won! {object.pencolor()} won the game.")
            else:
                print(f"You Lose! {object.pencolor()} won the game.")
        else:
            object.forward(random.randrange(0,10))


screen.exitonclick()