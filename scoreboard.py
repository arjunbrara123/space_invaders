from turtle import Turtle               # Import Turtle library for class inheritance

FONT_SCORE = ("Courier", 20, "bold")    # Font for displaying user scores at top
FONT_MSG = ("Courier", 40, "bold")      # Font for displaying messages in centre screen


class Scoreboard(Turtle):

    def __init__(self):
        """Initialise 'ScoreBoard' object as subclass of 'Turtle' object"""
        super().__init__()              # Call 'turtle' initiation
        self.hideturtle()               # Stop displaying turtle object on screen
        self.color("white")             # Set text colour to white
        self.penup()                    # Don't display trail
        self.refresh(0, 0)              # Display starting scores
        self.speed(0)                   # Turn off any updating delays

    def refresh(self, p1_score, scorer=0, col="white"):
        """Show updated user scores on scoreboard"""
        self.clear()                                                # Clear existing scoreboard
        self.goto(300, 250)                                        # Goto Top Left for Player 1 Score position
        self.write(f'Score: {p1_score}', align="center", font=FONT_SCORE)  # Display Player 1's current score

    def game_over(self):
        """Game over on screen"""
        self.goto(0, 0)                                                     # Goto centre of screen
        self.write("GAME OVER!", align="center", font=FONT_MSG)             # Write 'Game Over' message

    def winner(self, score):
        """Display winning player on screen"""
        self.goto(0, 0)                                                     # Goto centre of screen
        self.color("gold")                                                  # Change text colour to gold
        self.write(f"Your Score: {score}!", align="center", font=FONT_MSG)  # Write winning player on screen

    def debug_mode(self):
        """Inform user of debugging mode is active"""
        self.goto(0, 0)                                                     # Goto centre of screen
        self.color("red")                                                   # Change text colour to red
        self.write("DEBUGGING MODE", True, align="center", font=FONT_MSG)   # Write 'Debugging Mode' on screen