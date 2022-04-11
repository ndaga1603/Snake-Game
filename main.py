

import turtle
import time
from snake_game import Snake
from score_board import Score
from food import Food


screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The snake Game")
screen.tracer(0)

scores = Score()
snake = Snake()
food = Food()


the_game_contiinue = True
while the_game_contiinue:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.listen()
    screen.onkey(fun=snake.up, key="")
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=snake.right, key="Right")
    screen.onkey(fun=snake.left, key="Left")

# detect if snake hits a food
    if snake.all_turtles[0].distance(food) < 15:
        scores.increase_score()
        scores.score_track()
        snake.extend_a_snake()
        food.refresh()

# detect wall collison
    if snake.all_turtles[0].xcor() < -280 or snake.all_turtles[0].xcor() > 280 or snake.all_turtles[0].ycor() < -280 or snake.all_turtles[0].ycor() > 280:
       snake.reset()
       scores.reset()


# detect collision with tail
    for turtle in snake.all_turtles[1:]:
        if snake.head.distance(turtle) < 10:
            scores.reset()
            

screen.exitonclick()
