from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("white")
        self.penup()
        self.goto((20,-460))
        self.x_step=20
        self.y_step=20

    def move(self):
        
        x = self.xcor()+self.x_step
        y = self.ycor()+self.y_step
        self.goto(x,y)



        
    

    def bounce(self, i):
        
        if i==0 :
            self.x_step*=-1
            
        else:
            self.y_step*=-1
            

        