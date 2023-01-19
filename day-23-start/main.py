import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player =Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_forward, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()

    if player.is_at_finish_line():
        player.reset_position()
        scoreboard.increase_level()
        cars.increase_speed()

    for car in cars.all_cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False






screen.exitonclick()
