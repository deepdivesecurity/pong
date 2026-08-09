from turtle import Turtle
from constants import SCREEN_HEIGHT

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
COLOR = "red"

class Scoreboard(Turtle): 
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.color("white")
        self.penup()
        self.goto(0, SCREEN_HEIGHT / 2 - 40)
        self.write(f"P1: {self.p1_score}   P2: {self.p2_score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        
    def update_scoreboard(self): 
        self.clear()
        self.write(f"P1: {self.p1_score}   P2: {self.p2_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self, player): 
        if player == 1: 
            self.p1_score += 1
        if player == 2: 
            self.p2_score += 1
        self.update_scoreboard()

    # def game_over(self): 
    #     self.goto(0, 0)
    #     self.color(COLOR)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    # def check_score(self): 
    #     if self.p1_score == 2 or self.p2_score == 2: 
    #         self.game_over()