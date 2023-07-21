from turtle import Turtle
DIST = 10
START = (0, -280)
FINISH = 200

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.color("black")
        self.shape("turtle")
        self.goto(START)

    def move_up(self):

        new_y = self.ycor() + DIST
        self.goto(self.xcor(),new_y)

    def move_left(self):
        new_x = self.xcor() - DIST
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + DIST
        self.goto(new_x,  self.ycor())

    def move_down(self):
        new_y = self.ycor() - DIST
        self.goto(self.xcor(), new_y)

    def reset_poss(self):
        self.goto(START)