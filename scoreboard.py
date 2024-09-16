from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self,position):
        super().__init__()
        self.l_score=0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.display_l_score()
        self.display_r_score()

    def display_l_score(self):
        self.write(arg=f"{self.l_score}",align="center",font=("courier",50,"normal"))

    def display_r_score(self):
        self.write(arg=f"{self.r_score}",align="center",font=("courier",50,"normal"))

    def update_l_score(self):
        self.l_score+=1
        self.clear()
        self.display_l_score()

    def update_r_score(self):
        self.r_score+=1
        self.clear()
        self.display_r_score()
