from turtle import Turtle


class Snake:
    def __init__(self):
        self.position=((-20,0),(0,0),(20,0))
        self.snake_parts=[]
        self.create_snake()
        self.snake_head=self.snake_parts[-1] 
        self.snake_head.color("black")

    def create_snake(self):
        for i in range(len(self.position)):
            new_snake=Turtle('square')
            new_snake.penup()
            new_snake.color("white")
            new_snake.goto(self.position[i])
            self.snake_parts.append(new_snake) 

    def extend(self): # دالة لزيادة طول الثعبان
        segment =Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(self.snake_parts[0].pos()) # اضافة الجزء ف الاخر
        self.snake_parts.insert(0,segment)

    def move(self): 
        for i in range(len(self.snake_parts)-1): # except the head
            self.snake_parts[i].goto(self.snake_parts[i+1].pos()) 
        self.snake_head.fd(20)

    def go_up(self):
        if self.snake_head.heading() == 270:
            pass
        else:
            self.snake_head.setheading(90)

    def go_down(self):
        if self.snake_head.heading()== 90:
            pass
        else:
            self.snake_head.setheading(270)

    def go_right(self):
        if self.snake_head.heading()== 180:
            pass
        else:
            self.snake_head.setheading(0)

    def go_left(self):
        if self.snake_head.heading()== 0:
            pass
        else:
            self.snake_head.setheading(180)