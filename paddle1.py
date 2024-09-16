from turtle import Turtle
#POSITION=(370,0)
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(position)


    def paddle_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)

    def paddle_down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)




