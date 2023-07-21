from turtle import Turtle
import random

COLORS = ["red", "yellow", "green", "orange", "blue"]
START = 5
MORE = 10

class Car:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            t = Turtle()
            t.penup()
            t.shape("square")
            t.shapesize(stretch_wid=1, stretch_len=2)
            t.color(random.choice(COLORS))
            t.goto(300, random.randint(-250, 250))
            self.all_cars.append(t)

    def move(self):
        for car in self.all_cars:
            car.backward(START)



