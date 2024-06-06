from turtle import Turtle

WIDTH = 1
HEIGHT = 5


class Paddle (Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH)
        self.penup()
        self.setpos(pos[0], pos[1])

    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.setpos(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.setpos(self.xcor(), new_y)
