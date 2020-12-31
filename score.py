from turtle import Turtle
FONT = ("Courier", 14, "bold")
ALIGN = "CENTER"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.sety(280)
        self.update_score()

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.write("Score: %s" % self.score, font=FONT, align=ALIGN)

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER!", font=FONT, align=ALIGN)
