from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score = {self.score}",move = False, align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
