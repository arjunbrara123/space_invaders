from turtle import Turtle, register_shape


class Shot(Turtle):

    #register_shape("alien.gif")

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("black")
        self.shapesize(stretch_wid=0.3, stretch_len=1)
        self.penup()
        self.active = 1
        self.setheading(90)

    def fire_shot(self, xpos):
        self.active = 1
        self.color("yellow")
        self.setpos(xpos, -250)

    def move(self):
        if self.active == 1:
            self.forward(5)
            if self.ycor() > 300:
                self.active = 0
                self.color("black")