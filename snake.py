from turtle import Turtle,Screen
import random

colors = ("red","green","blue","yellow","orange","pink","purple")

MOVE_DISTANCE = 20 # RENAME

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.beginner_snake()


    def beginner_snake(self):
        for _ in range(3):
            self.add_part()

        self.head = self.segments[0]


    def add_part(self):
        random_box_size = random.randint(5, 10) / 10

        new_segment = Turtle("square")
        new_segment.color("white") # change later
        new_segment.shapesize(stretch_len=random_box_size, stretch_wid=random_box_size)
        new_segment.pu()

        self.segments.append(new_segment)
    

    def reset(self):
        for part in self.segments:
            part.goto(1000,1000)

        self.segments.clear()
        self.beginner_snake()


    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()

            self.segments[i].goto(x, y)

        self.head.forward(MOVE_DISTANCE)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


