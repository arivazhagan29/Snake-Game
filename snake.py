from turtle import Turtle
position=[(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()

    def create_snake(self):
        for x in position:
            self.add_segment(x)

    def add_segment(self,x):
        new_tim = Turtle("circle")
        new_tim.color("white")
        new_tim.penup()
        new_tim.goto(x)
        self.segments.append(new_tim)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move_snake(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(20)

    def Up(self):
        if(self.segments[0].heading()!=270):
            self.segments[0].setheading(90)
    def Right(self):
        if (self.segments[0].heading() != 180):
            self.segments[0].setheading(360)
    def Left(self):
        if (self.segments[0].heading() != 360):
            self.segments[0].setheading(180)
    def Down(self):
        if (self.segments[0].heading() != 90):
            self.segments[0].setheading(270)