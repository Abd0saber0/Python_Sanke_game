from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.shapesize(.5,.5)
        self.appear()
    def appear(self):
        random_coor=random.randint(-280,280)
        self.goto(random_coor,random_coor)

# from PIL import Image
# img=Image.open("./pexels-nick-rtr-1632308-3187173.jpg")
# m=img.resize((600,600))
# m.save('nbg4.gif')