from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, goto):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(goto)

    def turn_right(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def turn_left(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
