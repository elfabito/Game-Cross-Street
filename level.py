from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.goto(-220, 260)
        self.hideturtle()
        self.level = 0
        self.update_level()


    def raise_level(self):
        self.level += 1
        self.update_level()
    def update_level(self):
        self.clear()
        self.goto(-220, 260)
        self.write(f"Level: {self.level}", True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", True, align=ALIGNMENT, font=FONT)