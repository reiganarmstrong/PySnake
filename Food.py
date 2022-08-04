import random
from turtle import Turtle
from Constants import HEIGHT, WIDTH


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.randomize_position()

    def randomize_position(self):
        random_x = random.randint(-WIDTH//2+20, WIDTH//2-20)
        random_y = random.randint(-HEIGHT//2+20, HEIGHT//2-20)
        self.goto(random_x, random_y)
