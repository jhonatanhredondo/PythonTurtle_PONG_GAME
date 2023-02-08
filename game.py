from turtle import Screen
from paddle import Paddle
from ball import Ball
from gameover import GameOver
from scoreboard import Scoreboard
import time

HEIGHT_OF_SCREEN = 600
WIDTH_OF_SCREEN = 800
RIGHT_PADDLE_POSITION = (350, 0)
LEFT_PADDLE_POSITION = (-350, 0)
RIGHT_PADDLE_SCORE = (100, 260)
LEFT_PADDLE_SCORE = (-100, 260)
SAFE_DISTANCE = 20
DISTANCE_PADDLE_WALL = 330
PADDLE_HEIGHT = 100
FINAL_SCORE = 5
GAMESPEED = 0.1

class Game():
    def __init__(self, screen):
        screen = Screen()

        # 800x600 black background with the title Pong
        screen.setup(height=HEIGHT_OF_SCREEN, width=WIDTH_OF_SCREEN)
        screen.bgcolor("black")
        screen.title("Pong")
        screen.tracer(0)

        # both players. The first player is the right one and the second is the left one.
        first_paddle = Paddle(RIGHT_PADDLE_POSITION)
        second_paddle = Paddle(LEFT_PADDLE_POSITION)

        # create both scoreboards
        first_score = Scoreboard(RIGHT_PADDLE_SCORE)
        second_score = Scoreboard(LEFT_PADDLE_SCORE)

        # create the ball object
        ball = Ball()
        self.game_is_on = True 


        # end the game and write the final message
        def endgame():
            self.game_is_on = False
            first_score.clear()
            second_score.clear()
            GameOver(first_paddle.get_score(), second_paddle.get_score())

        # keys to move the players Up and Down -> player 1 and W and S -> player 2
        screen.listen()
        screen.onkey(first_paddle.up, "Up")
        screen.onkey(first_paddle.down, "Down")
        screen.onkey(second_paddle.up, "w")
        screen.onkey(second_paddle.down, "s")
        screen.onkey(endgame, "x")

        # maintain the game running and updating the screen until game_is_on = True
        while self.game_is_on:
            time.sleep(GAMESPEED)
            screen.update()
            ball.move()

            # detect collision with the wall
            if ball.ycor() > (HEIGHT_OF_SCREEN/2) - SAFE_DISTANCE or ball.ycor() < -((HEIGHT_OF_SCREEN/2) - SAFE_DISTANCE):
                ball.bounce()

            # detect collision with the paddle
            if ball.xcor() > DISTANCE_PADDLE_WALL or ball.xcor() < -DISTANCE_PADDLE_WALL:
                if ball.distance(first_paddle) < (PADDLE_HEIGHT/2) or ball.distance(second_paddle) < (PADDLE_HEIGHT/2): 
                    ball.invert()

            # detect if user scored and write the user score in the screen
            if ball.xcor() > (WIDTH_OF_SCREEN/2):
                second_paddle.point()
                second_score.write_points(second_paddle.get_score())
                ball.restart()
            elif ball.xcor() < -(WIDTH_OF_SCREEN/2):
                first_paddle.point()
                first_score.write_points(first_paddle.get_score())
                ball.restart()

            # detect if someone has done 5 points
            if second_paddle.get_score() == FINAL_SCORE:
                endgame()
            elif first_paddle.get_score() == FINAL_SCORE:
                endgame()

        # On click exit the window
        screen.exitonclick()