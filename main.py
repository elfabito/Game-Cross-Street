from turtle import Turtle, Screen
from player import Player
from car import Car
from level import Level
import time

s = Screen()
s.title("Cruza la calle tortuguita")
s.setup(width=600, height=600)
s.tracer(0)


player = Player()
car_m = Car()
level = Level()

s.listen()
s.onkey(player.move_up, 'w')
# s.onkey(player.move_down, 's')
s.onkey(player.move_left, 'a')
s.onkey(player.move_right, 'd')

end_of_game = True
while end_of_game:
    time.sleep(0.1)
    s.update()

    car_m.create_car()
    car_m.move()

    for car in car_m.all_cars:
        if car.distance(player) < 20:
            end_of_game = False
            level.game_over()

    if player.ycor() == 260:
        level.raise_level()
        player.reset_poss()





s.exitonclick()