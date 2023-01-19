from turtle import Turtle, Screen

tim = Turtle()
screen = Screen ()


def move_forwards(): #Forward
    tim.forward(10)
def move_backwards(): #backward
    tim.backward(10)
def move_clockwise(): #clockwise
    tim.right(90)
def move_anticlockwise(): #anticlockwise
    tim.left(90)
def move_tendegree(): #controll degree 10 
    tim.left(10)
def move_fivedegree(): #controll degree 5
    tim.left(5)
def undo(): #undo action
    tim.undo()
def clear(): #clear the screen
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkeypress(key="Up", fun=move_forwards)
screen.onkeypress(key="Down", fun=move_backwards)
screen.onkeypress(key="Right", fun=move_clockwise)
screen.onkeypress(key="Left", fun=move_anticlockwise)
screen.onkeypress(key="d", fun=move_tendegree)
screen.onkeypress(key="a", fun=move_fivedegree)
screen.onkeypress(key="w", fun=undo)
screen.onkeypress(key="c", fun=clear)


screen.exitonclick()