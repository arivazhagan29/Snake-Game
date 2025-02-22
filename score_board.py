from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}",align="center",font=("Arial",14,"normal"))
        self.hideturtle()

    def inc_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}",align="center",font=("Arial",14,"normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 40)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 14, "normal"))
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=("Arial", 20, "normal"))