from turtle import Turtle

class Paddle(Turtle): 
    def __init__(self, position): 
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position): 
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def up(self): 
        self.goto(self.xcor(), self.ycor() + 30)

    def down(self): 
        self.goto(self.xcor(), self.ycor() - 30)