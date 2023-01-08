STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    # Defines the turtle object to be controlled by the player.
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("turtle")
        self.setpos(0,-280)
        self.left(90)
        self.showturtle()

    # Defines the control functions for the player.
    def up(self):
        self.forward(10)
    def down(self):
        self.backward(10)
    def isatfinishline(self):
        # Checks if player is at the finish line.
        if self.ycor() == 280:
            return True
        return False
    def reset(self):
        # Puts the player back to the beginning after beating a level.
        self.hideturtle()
        self.setpos(0,-280)
        self.showturtle()


