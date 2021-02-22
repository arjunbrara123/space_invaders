from alien import Alien
from random import choice

COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 2

class AlienManager:

    def __init__(self):
        super().__init__()
        self.all_aliens = set()

    def setup_aliens(self):
        for iColour in range(6):
            for iXPos in range(13):
                alien = Alien(choice(COLOURS), iXPos*50 - 300, iColour*40 + 80)
                self.all_aliens.add(alien)

    def remove_alien(self):
        pass


    def move(self, level=0):
        to_remove = set()
        for alien in self.all_aliens:
            if alien.active == 1:
                alien.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT * level)
                if alien.xcor() < -320:
                    alien.setheading(0)
                    alien.sety(alien.ycor() - 20)
                    alien.forward(10)
                if alien.xcor() > 320:
                    alien.setheading(180)
                    alien.sety(alien.ycor() - 20)
                    alien.forward(10)
