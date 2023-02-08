from turtle import Turtle

ALIGN="center"
FONT=('Arial', 24, 'normal')
FONT_SMALLER = ('Helvetica', 16, 'normal')

class GameOver(Turtle):
    def __init__(self, first_score, second_score):
        super().__init__()
        self.color("white")
        self.write("Game over", align=ALIGN, font=FONT)
        y_cor = self.ycor() - 40
        self.write_the_final_message(f"{second_score} X {first_score}", y_cor)
        y_cor -= 40
        self.write_the_final_message("Clique na tela para fechar o jogo", y_cor)

    def write_the_final_message(self, message, y_cor):
        self.goto(y=y_cor, x=0)
        self.write(message, align=ALIGN, font=FONT_SMALLER)


