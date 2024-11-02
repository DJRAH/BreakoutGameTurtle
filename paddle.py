from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, lent, wid):
        super().__init__()
        self.shapesize(stretch_len=lent, stretch_wid=wid)
        self.color("blue")
        self.shape('square')
        self.penup()
        
    
    def droit(self):
        x = int(self.xcor())+60
        self.goto(x,self.ycor())
    
    def gauche(self):
        x = int(self.xcor())-60
        self.goto(x,self.ycor())