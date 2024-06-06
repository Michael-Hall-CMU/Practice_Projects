from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def generate_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            starting_y = random.randint(-250, 250)
            new_car.setpos(300, starting_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            new_x = car.xcor() - self.car_speed
            car.setpos(new_x, car.ycor())

    def increase_move_speed(self):
        self.car_speed += MOVE_INCREMENT
