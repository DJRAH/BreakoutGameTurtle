from turtle import *
import random, time
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.bgcolor("black")
screen.setup(width=1600, height=1200)
screen.title("PingPong DjRAH")

#bar user
paddle = Paddle(6, 1)
paddle.goto((20,-470))

#contruct wall
col = ['blue','yellow','red','white','green','red','blue']
tous=[]
for j in range(4):
    mur=[]
    for i in range(10):
        p = Paddle(8,3)
        mur.append(p)
        mur[i].color(col[j])
        mur[i].goto((164*i-768, 380-j*65)) 
    tous.append(mur)
 
#the ball
bal = Ball()



screen.listen()

screen.onkey(paddle.droit, "Right")
screen.onkey(paddle.gauche, "Left")
screen.onkeypress(paddle.droit, "Right")
screen.onkeypress(paddle.gauche, "Left")


game_on=True
while(game_on):

    bal.move()

    x = bal.xcor()
    y = bal.ycor()
    
    if y >= 490 or  y < -490:
        bal.bounce(1)
    if x>= 768 or x <= -768:
        bal.bounce(0)

    #bal.distance(paddle)<50
  

    time.sleep(0.01)
    screen.update()

    for j in tous:
        for i in j:
            if bal.distance(i)< 100:
                i.hideturtle()
                j.remove(i)
                bal.bounce(0)
                bal.bounce(1)
        
    

    

screen.exitonclick()