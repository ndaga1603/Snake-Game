
from turtle import Turtle

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.write(f"score: {self.score}", align="center", font=("courier", 15, "normal"))
       

    
    def score_track(self):
        self.score = self.score + 1
        self.clear()
        self.write("score: {}".format(self.score), align="center", font=("courier", 15, "normal"))



    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("courier", 30, "normal"))

        
        
        