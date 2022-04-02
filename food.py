
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid = 0.5, stretch_len = 0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_cor = random.randint(-250, 250)
        y_cor = random.randint(-250, 250)
        self.goto(x_cor, y_cor)
