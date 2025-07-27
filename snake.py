from turtle import Turtle


SNAKE_POSITION = [(-20, 0), (0, 0), (20, 0)]
SNAKE_MOVE = 20

class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]


    def create_snake(self):
        for i in SNAKE_POSITION:
            self.add_snake(i)

    def add_snake(self, position):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.snake_list.append(segment)

    def extend_snake(self):
        self.add_snake(self.snake_list[-1].pos())

    def move(self):
        for i in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[i - 1].xcor()
            new_y = self.snake_list[i - 1].ycor()
            self.snake_list[i].goto(new_x, new_y)
        self.snake_list[0].forward(SNAKE_MOVE)

    def reset(self):
        for seg in self.snake_list:
            seg.goto(1000, 1000)
        self.snake_list.clear()
        self.create_snake()
        self.head = self.snake_list[0]
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)