from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def main(): 
    screen = Screen()
    screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    p1_paddle = Paddle((350, 0))
    p2_paddle = Paddle((-350, 0))

    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(p1_paddle.up, "Up")
    screen.onkey(p1_paddle.down, "Down")
    screen.onkey(p2_paddle.up, "w")
    screen.onkey(p2_paddle.down, "s")

    game_on = True
    while game_on: 
        screen.update()

    screen.exitonclick()

if __name__ == "__main__":
    main()