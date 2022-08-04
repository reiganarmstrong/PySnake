import time
from turtle import done
from Food import Food
from Snake import Snake
from Scoreboard import Scoreboard
from Constants import WIDTH, SCREEN, HEIGHT, SLEEP_TIME


def play_game():
    game_is_on = True
    snake = Snake()
    food = Food()
    board = Scoreboard()
    while game_is_on:
        SCREEN.update()
        snake.forward()
        if snake.wall_collision() or snake.tail_collision():
            board.end()
            game_is_on = False
        if snake.body[0].distance(food) < 15:
            snake.extend_body()
            food.randomize_position()
            board.score += 1
            board.rewrite()
        time.sleep(SLEEP_TIME)


if __name__ == "__main__":
    SCREEN.title("PySnake")
    SCREEN.setup(width=WIDTH, height=HEIGHT)
    SCREEN.bgcolor("black")
    SCREEN.listen()
    SCREEN.tracer(0)
    play_game()
    done()
