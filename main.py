from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time


# Screen initialization 
screen=Screen()
screen.title("Snake Game ")
screen.setup(600,600)
screen.bgpic("./nbg4.gif")
screen.tracer(0)
# Show snake parts
snake=Snake()
food=Food()
score=Score()
# Moving the snake
screen.listen()
screen.onkey(snake.go_up,"Up")
screen.onkey(snake.go_down,"Down")
screen.onkey(snake.go_right,"Right")
screen.onkey(snake.go_left,"Left")

# Starting the game
game_on=True

while game_on:
    snake.move()
    screen.update()
    time.sleep(.1) # للتحكم ف سرعة اللوب

    # Eating the food
    if snake.snake_head.distance(food) < 15 :
        food.appear()
        snake.extend()
        score.increase_score()
        
    # Check for collision with the wall
    if (
        snake.snake_head.xcor() > 300 or snake.snake_head.xcor() < -300 
        or 
        snake.snake_head.ycor() > 300 or snake.snake_head.ycor() < -300
    ):
        score.game_over()
        game_on=False

    # Check for collision with the body of snake except the head
    for part in snake.snake_parts[:-1]: # -1 exclusive
        if snake.snake_head.distance(part) < 10 :
            score.game_over()
            game_on=False
            break


screen.exitonclick()