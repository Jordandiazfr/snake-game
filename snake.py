from turtle import Turtle

STARTING_POSITIONS = [(-40, 0), (-20, 0), (0, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("red")
        self.heading = self.segments[0].heading

    def create_snake(self):
        for position in STARTING_POSITIONS[::-1]:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        # Optional moving
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.heading() != LEFT:
            self.head.setheading(RIGHT)




