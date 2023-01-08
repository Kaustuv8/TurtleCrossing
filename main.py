import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
# Creating Screen.
screen = Screen()
screen.setup(width=600, height=600)
# Pauses the Screen upon creation.
screen.tracer(0)
# Creating the player.
Timmy = Player()
# Creating the Cars.
Cars = CarManager()
# Creating the scoreboard.
Board = Scoreboard()
# Defining the controls.
screen.listen()
screen.onkey(Timmy.up, "w")
screen.onkey(Timmy.down, "s")
game_is_on = True
# Running the game.
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Checking for finish line.
    if Timmy.isatfinishline():
        Board.Update()
        Timmy.reset()
        Cars.Update()
    # Checking for car collision.
    for i in range(len(Cars.carlist)):
        if Cars.carlist[i].distance(Timmy) < 20:
            Board.GameOverScreen()
            game_is_on = False
    Cars.Move()
    Cars.resetcheck()
screen.exitonclick()
