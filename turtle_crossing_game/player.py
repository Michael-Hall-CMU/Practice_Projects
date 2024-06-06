from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.setpos(STARTING_POSITION)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def has_collided(self, cars):
        for car in cars:
            if self.distance(car) <= 20 and car.ycor() - 18 <= self.ycor() <= car.ycor() + 18:
                return True

    def reset_position(self):
        self.setpos(STARTING_POSITION)

    def has_finished(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False
