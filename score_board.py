

from turtle import Turtle

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.highscore = high_score
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.score_track()

    
    
    def score_track(self):
        self.clear()
        self.write(f"score: {self.score} High score: {self.highscore} ", 
                 align="center", font=("courier", 15, "normal"))
   



    def reset(self):
        if self.score > self.highscore: 
            self.highscore = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.highscore))

        self.score = 0    
        self.score_track()
      

    def increase_score(self):
        self.score = self.score + 1



with open("data.txt") as file:
    high_score = int(file.read())

