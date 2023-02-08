from turtle import Turtle

ALIGN="center"
FONT=('Arial', 14, 'normal')

class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.write_points(0)

    def write_points(self, number_of_points):
        self.clear()
        self.write(number_of_points, align=ALIGN, font=FONT)