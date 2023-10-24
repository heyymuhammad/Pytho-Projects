import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkeypress(player.move_forward,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_cars()
    car_manager.move_cars()

    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            score_board.game_over()
            game_is_on=False
    
    if player.ycor() == 280:
        score_board.increase_level()
        player.reset_position()
        car_manager.increase_speed()


screen.exitonclick()