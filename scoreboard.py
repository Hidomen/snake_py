from turtle import Turtle,Screen

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,250)  
        self.update()  


    def score_up(self):
        self.score += 1
        self.update()


    def update(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                self.high_score = self.score
                
                file.write(str(self.high_score))


        self.clear()
        self.write(f"Score: {self.score}, Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)


    def reset(self):
        self.score = 0
        self.update()