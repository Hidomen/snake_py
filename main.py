from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
# import random

WALL_COR = 300

def game():


    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=600, height=600)


    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    food = Food()
    scoreboard = Scoreboard()

    game_over = False

    while not game_over:
        screen.update()
        time.sleep(0.1)

        snake.move()

        #detections
            # got a food
        if snake.head.distance(food) < 15:
            snake.extend()
            food.spawn()
            scoreboard.score_up()
            if snake.head.distance(food) < 30:
                snake.extend()
                food.spawn()    
                scoreboard.score_up()
            # collision to wall

        if  -WALL_COR > snake.head.xcor() or snake.head.xcor() > WALL_COR or -WALL_COR > snake.head.ycor() or snake.head.ycor() > WALL_COR:
            snake.reset()
            scoreboard.reset()
            # collision to itself
        for i in range(1, len(snake.segments) - 1):
            if snake.head.distance(snake.segments[i]) < 5:
                snake.reset()
                scoreboard.reset()

    # game over screen

    screen.exitonclick()

# def random_color():
#     r = random.randint(1,255)
#     g = random.randint(1,255)
#     b = random.randint(1,255)
    
#     return r, g, b

game()




