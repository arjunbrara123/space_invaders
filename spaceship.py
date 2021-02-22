from turtle import Turtle, register_shape               # Import Turtle library for class inheritance
from shot import Shot                                   # Shot from spaceship

class SpaceShip(Turtle):

    register_shape("ship.gif")

    def __init__(self, pos):
        """Initialise 'spaceship' object as subclass of 'Turtle' object"""
        super().__init__()                              # Call 'turtle' initiation
        self.penup()                                    # Stop displaying trail
        self.shapesize(stretch_wid=1, stretch_len=5)    # Stretch turtle to create a 'spaceship' shape
        #self.color("white")                             # Set colour to white
        self.shape("ship.gif")                          # Set spaceship shape
        self.setpos(pos)                                # Move spaceship to desired position on screen
        self.all_shots = []
        self.charge = 10

    def move_left(self):
        """Move a spaceship left"""
        self.setx(self.xcor() - 30)                     # Move spaceship left 60 paces

    def move_right(self):
        """Move a spaceship right"""
        self.setx(self.xcor() + 30)                     # Move spaceship right 60 paces

    def fire_shot(self):
        if self.charge >= 10:
            shot = Shot(self.xcor())
            self.all_shots.append(shot)
            self.charge = 0

    def shoot(self):
        for shot in self.all_shots:
            shot.move()
        self.charge += 1
