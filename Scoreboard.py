from turtle import Turtle
from Constants import HEIGHT, FONT, ALIGNMENT


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.goto(0, HEIGHT//2-90)
        self.rewrite()
        self.hideturtle()
        self.penup()

    def rewrite(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT,
                   font=FONT)

    def end(self):
        self.goto(0, 0)
        self.write(f"Game Over.", align=ALIGNMENT,
                   font=FONT)
