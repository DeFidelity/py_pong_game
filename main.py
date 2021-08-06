from turtle import Screen
from the_paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

l_paddle = Paddle((-350, 0))

r_paddle = Paddle((350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.turn_right, "w")
screen.onkey(l_paddle.turn_left, "s", )

screen.listen()
screen.onkey(r_paddle.turn_right, "Right")
screen.onkey(r_paddle.turn_left, "Left", )

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # detect collision with wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_x()
    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -340:
        ball.bounce_y()
    # detect if ball cross the boundary at right
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()
    #  detect if ball cross boundary at left
    if ball.xcor() < - 380:
        ball.reset_ball()
        scoreboard.r_point()
screen.exitonclick()
