from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)


l_paddle = Paddle((-370,0))
r_paddle = Paddle((370,0))

ball = Ball()
scoreboard = Scoreboard() 

screen.listen()
screen.onkeypress(l_paddle.go_up, "Up")
screen.onkeypress(l_paddle.go_down, "Down")

screen.onkeypress(r_paddle.go_up, "w")
screen.onkeypress(r_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect with wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    #Detect with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    #Out of range  
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    #Out of range  
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()