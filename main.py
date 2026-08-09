from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import time

def main(): 
    screen = Screen()
    screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    p1_paddle = Paddle((350, 0))
    p2_paddle = Paddle((-350, 0))

    scoreboard = Scoreboard()

    ball = Ball()

    screen.listen()
    screen.onkey(p1_paddle.up, "Up")
    screen.onkey(p1_paddle.down, "Down")
    screen.onkey(p2_paddle.up, "w")
    screen.onkey(p2_paddle.down, "s")

    game_on = True
    while game_on: 
        time.sleep(0.1)
        ball.move()
        screen.update()

        # Check for collision with wall
        if ball.xcor() > SCREEN_WIDTH / 2 + 80: 
            # Update scoreboard
            scoreboard.increase_score(2)
            ball.reset()

        # Check for collision with wall
        if ball.xcor() < SCREEN_WIDTH / -2 - 80: 
            # Update scoreboard
            scoreboard.increase_score(1)
            ball.reset()

        # Check for collision with top or bottom wall
        if ball.ycor() > SCREEN_HEIGHT / 2 or ball.ycor() < SCREEN_HEIGHT / -2: 
            # Bounce ball away from wall
            ball.bounce_y()

        # Check for collision with paddle
        if ball.distance(p1_paddle) < 50 and ball.xcor() > 320 or ball.distance(p2_paddle) < 50 and ball.xcor() < -320: 
            ball.bounce_x()

        # Check for collision with left paddle

        
    screen.exitonclick()

if __name__ == "__main__":
    main()