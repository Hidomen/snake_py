from turtle import Turtle,Screen
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed(0)
        self.spawn()



    def spawn(self):
        random_x = random.randint(-14, 14)
        random_y = random.randint(-14, 14)
        
        self.goto(random_x * 20, random_y * 20)
