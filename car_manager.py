import random as ran
import turtle as t
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        # carlist holds all the moving car objects
        # move holds the distance which the cars move.
        self.carlist = []
        self.move = 5
        for i in range(25):
            Turt = t.Turtle()
            Turt.hideturtle()
            Turt.penup()
            Turt.shape("square")
            Turt.turtlesize(1, 2)
            # putting the cars at a random position beyond the right edge of the screen
            # in order to prevent them from starting at the same x-coordinate.
            Turt.setpos(ran.randint(282,1082),ran.randint(-275,275))
            Turt.color(ran.choice(COLORS))
            Turt.setheading(180)
            self.carlist.append(Turt)
        # individually making all the turtles visible.
        for j in self.carlist:
            j.showturtle()
    def resetcheck(self):
        # resets the cars after the reach the end of the screen.
        for j in self.carlist:
            if j.xcor() < -285:
                j.hideturtle()
                j.setpos(ran.randint(282,1082),ran.randint(-275,275))
                j.showturtle()

    def Move(self):
        # moves the cars.
        for j in self.carlist:
            j.forward(self.move)


    def Update(self):
        # Updates the cars by resetting their position and increasing their
        # speed after player beats a level.
        for j in self.carlist:
            j.hideturtle()
            j.setpos(ran.randint(275,1025), ran.randint(-275, 275))
            j.showturtle()
        self.move+=10
