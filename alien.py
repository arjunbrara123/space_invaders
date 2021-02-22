from turtle import Turtle, register_shape


class Alien(Turtle):

    register_shape("alien.gif")

    def __init__(self, col, xpos, ypos):
        super().__init__()
        self.shape("alien.gif")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color(col)
        self.penup()
        self.setpos(xpos, ypos)
        self.active = 1
        self.setheading(0)
