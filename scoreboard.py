from turtle import Turtle

FONT = ("Courier", 12, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.level_up()

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", False, "center", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "center", FONT)

