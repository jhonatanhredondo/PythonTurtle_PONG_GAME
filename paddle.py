from turtle import Turtle

# Stretch of the turtle or the player shape
WIDTH = 1
HEIGHT = 5
DISTANCE_PLAYER_WALKS = 20 

class Paddle(Turtle):
    score = 0 

    def __init__(self, position):
        super().__init__(shape="square")
        self.penup()
        self.color("white")
        self.shapesize(HEIGHT, WIDTH)
        self.setpos(position)

    # Take the current ycor and move up by adding 20
    def up(self):
        new_y = self.ycor() + DISTANCE_PLAYER_WALKS
        self.goto(self.xcor(), new_y)

    # Take the current ycor and move up by subtracting 20
    def down(self):
        new_y = self.ycor() - DISTANCE_PLAYER_WALKS
        self.goto(self.xcor(), new_y)

    def point(self):
        self.score += 1

    def get_score(self):
        return self.score
