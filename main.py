from turtle import Turtle,Screen
from paddle1 import Paddle
from Ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)

#create line in middle
line=Turtle()
line.hideturtle()
line.color("white")
line.pensize(3)
line.penup()
line.goto(0,-300)
line.setheading(90)
for i in range(30):
    line.forward(10)
    line.penup()
    line.forward(10)
    line.pendown()

# def go_up():
#     new_y=paddle.ycor


#create paddle1
r_paddle = Paddle((370,0))
l_paddle = Paddle((-370,0))
ball=Ball()
r_scoreboard=Scoreboard((100,200))
l_scoreboard=Scoreboard((-100,200))


screen.listen()
screen.onkey(r_paddle.paddle_up,"Up")
screen.onkey(r_paddle.paddle_down,"Down")
screen.onkey(l_paddle.paddle_up,"w")
screen.onkey(l_paddle.paddle_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
#Detect collision with top and bottom
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()
#Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()
#Detect when paddle misses
    if ball.xcor() > 390:
        ball.reset_position()
        l_scoreboard.update_l_score()
    if ball.xcor() < -390:
        ball.reset_position()
        r_scoreboard.update_r_score()



screen.exitonclick()