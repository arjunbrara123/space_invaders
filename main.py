from turtle import Turtle, Screen       # Library for displaying GUI window
from scoreboard import Scoreboard       # Custom Class object to display user scores
from spaceship import SpaceShip         # Custom Class object to create spaceships
from alien_manager import AlienManager  # Custom class to autogenerate aliens
import time                             # Library for pausing between ball movements to create animation effect

# Initialise the screen and environment
p_score = 0                             # Initialise Player score
screen = Screen()                       # Initialise screen object
screen.setup(width=800, height=600)     # Set up screen dimensions
screen.bgcolor("black")                 # Set screen background colour to black
screen.title("Space Invaders")                # Set screen window title
screen.tracer(0)                        # Turn off automatic screen updates
scoreboard = Scoreboard()               # Initialise scoreboard object to show player scores
alien_manager = AlienManager()          # Initialise the alien manager
alien_manager.setup_aliens()            # Set up on-screen aliens
time_delay = 0.008                      # Set initial ball speed
winning_score = 3                       # Set points required to win game
FONT_SPLASH = ("Courier", 60, "bold")   # Font for displaying 'SPACE INVADERS' splash screen
FONT_MSG = ("Courier", 40, "bold")      # Font for displaying messages in centre screen
win_flag = 0                            # Flag to check if won

# Initialise the spaceship
spaceship = SpaceShip((0, -250))        # SpaceShip starting position
screen.update()                         # Update screen to let users see these

# Set up key listeners
screen.listen()
screen.onkey(spaceship.move_left, "Left")       # SpaceShip Left Key
screen.onkey(spaceship.move_right, "Right")     # SpaceShip Right Key
screen.onkey(spaceship.fire_shot, "space")           # Fire shot

# Welcome 'Splash Screen' message
def splash_screen(point=0):
    """Display Splash Screen 'Breakout' message at start of the game"""
    splash = Turtle()               # Initialise Turtle object
    splash.hideturtle()             # Stop displaying turtle object on screen
    splash.penup()                  # Ensure turtle isn't drawing on screen yet
    splash.speed(0)                 # Turn off any updating delays

    splash.color("white")                                               # Set message text colour to white
    splash.setposition(0, -50)                                          # Set position of splash screen welcome message
    splash.write("SPACE INVADERS", align="center", font=FONT_SPLASH)    # Set display font
    screen.update()                                                     # Update screen for user to see splash message
    time.sleep(1)                                                       # Keep on screen for 1 second
    splash.clear()                                                      # Clear splash screen message


# Initialise game loop
game_on = True                      # Set game looping variable for continuous loop
splash_screen()                     # Display splash screen welcome message
while game_on:                      # Start continuous game loop until someone wins!

    # Continuously move aliens
    alien_manager.move()                     # Move aliens forward in set movement direction based on game rules
    spaceship.shoot()

    # Check for collision with a alien
    for alien in alien_manager.all_aliens:      # Loop through all aliens
        for shot in spaceship.all_shots:
            if alien.distance(shot) < 14:          # Check if shot hits a alien
                if alien.active == 1:
                    p_score += 1                    # Add 1 to player score
                    scoreboard.refresh(p_score)     # Refresh scoreboard
                    alien.color("black")            # Set alien to be invisible
                    alien.active = 0                # Set alien to be inactive
                    alien.hideturtle()
                    screen.update()                 # Update screen

    # Check if Player lost
    if alien.ycor() < -200:                     # Check if ball crossed bottom of screen
        scoreboard.game_over()                  # Show updated score on screen

    # Check if player won
    win_flag = 0
    for alien in alien_manager.all_aliens:  # Loop through all aliens
        if alien.active == 1:
            win_flag = 1
    if win_flag == 0:
        scoreboard.winner(p_score)
        game_on = False

    # Update screen
    time.sleep(time_delay)                      # Pause game to facilitate visual animation
    screen.update()                             # Update screen

screen.exitonclick()                            # Keep game on screen until user clicks on the screen
