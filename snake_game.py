
import turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self. all_turtles = []
        self.make_turtle()
        self.head = self.all_turtles[0]



    def add_segment(self, position):
        new_turtle = turtle.Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.all_turtles.append(new_turtle)

    def make_turtle(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def extend_a_snake(self):
        self.add_segment(self.all_turtles[-1].position())


    def move(self):
        for a_turtle in range(len(self.all_turtles) - 1, 0, -1):
            x_cor = self.all_turtles[a_turtle - 1].xcor()
            y_cor = self.all_turtles[a_turtle - 1].ycor()
            self.all_turtles[a_turtle].goto(x_cor, y_cor)
        self.head.forward(20)


    def reset(self):
        for seg in self.all_turtles:
            seg.goto(800, 800)
            
        self.all_turtles.clear()
        self.make_turtle()
        self.head = self.all_turtles[0]


    def up(self):
        if  self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
