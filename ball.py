from turtle import Turtle

STRETCH = 1.25

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(STRETCH, STRETCH)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x=x_cor, y=y_cor)

    def bounce(self):
        self.y_move = self.y_move * -1

    def invert(self):
        self.x_move = self.x_move * -1

    def restart(self):
        self.goto(0,0)
        self.invert()
        self.bounce()