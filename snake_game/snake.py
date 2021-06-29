from turtle import Turtle
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            new_segment = Turtle("square")
            self.segments.append(new_segment)
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(-20*i, 0)

    def move(self, steps=MOVE_DISTANCE):
        for i in range(len(self.segments) -1, 0, -1):
            temp_x = self.segments[i-1].xcor()
            temp_y = self.segments[i-1].ycor()
            self.segments[i].goto(temp_x, temp_y)
        self.head.forward(steps)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)