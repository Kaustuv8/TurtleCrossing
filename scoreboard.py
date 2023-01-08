FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # This object controls the level and the gameover screen.
        self.penup()
        self.hideturtle()
        self.setpos(-260,265)
        self.write("Level : 1", False, font = ("Courier", 24, "normal"))
        self.level = 1


    def Update(self):
        # Updates the level.
        self.clear()
        self.level+=1
        self.write(f"Level : {self.level}", False, font=("Courier", 24, "normal"))


    def GameOverScreen(self):
        # write "GAME OVER" after the player collides with a car.
        self.setpos(0,0)
        self.write("GAME OVER", False,align="center",font=("Courier", 24, "normal"))
