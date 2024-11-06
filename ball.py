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



    def update_y(self):
        y = random.randint(0,490)
        h = random.randint(0,1)
        if h==0:
            self.y_step=y
        else:
            self.y_step=-y

    def update_x(self):
        x = random.randint(0,50)
        h = random.randint(0,1)
        if h==0:
            self.x_step=x
        else:
            self.x_step=-x
        
  
    

    def bounce(self, i):
        
        if i==0 :
            #self.x_step = random.randint(15,25)
            self.x_step*=-1
            
        else:
            #self.y_step = random.randint(15,25)
            self.y_step*=-1
            

        