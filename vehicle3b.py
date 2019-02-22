import turtle
import math

wn = turtle.Screen()
wn.bgcolor("grey")
wn.title("Vehicle 3 : Explorer (Cross Wired)")

source = turtle.Turtle()
source.shape("circle")
source.color("black")
source.penup()
source.speed(100)
source.goto(0 ,0)

vr = turtle.Turtle()
vr.shape("circle")
vr.color("purple")
vr.penup()
vr.speed(0)

vl = turtle.Turtle()
vl.shape("circle")
vl.color("purple")
vl.penup()
vl.speed(0)

v = turtle.Turtle()
v.shape("circle")
v.color("red") 
v.penup()
v.speed(100)

x = -250
y = -300
g = 40
l = 15
k1 = 1
k2 = .0000005
k = .5
v.goto(x,y)

dr = math.sqrt((v.xcor()+g/2-source.xcor()) ** 2 +
               (v.ycor()+l-source.ycor()) ** 2)
dl = math.sqrt((v.xcor()-g/2-source.xcor()) ** 2 +
               (v.ycor()+l-source.ycor()) ** 2)
vell = k * (k1 + (k2*dl ** 2))
velr = k * (k1 + (k2*dr ** 2))

vl.goto(v.xcor()-g/2, v.ycor()+l)
vr.goto(v.xcor()+g/2, v.ycor()+l)
vr.dx = vell*(vl.xcor()-source.xcor())/dl
vr.dy = vell*(vl.ycor()-source.ycor())/dl
vl.dx = velr*(vr.xcor()-source.xcor())/dr
vl.dy = velr*(vr.ycor()-source.ycor())/dr
v.dx = (vl.dx+vr.dx)
v.dy = (vl.dy+vr.dy)
v.pendown()

while True:
    dr = math.sqrt((v.xcor()+g/2-source.xcor()) ** 2 +
                   (v.ycor()+l-source.ycor()) ** 2)
    dl = math.sqrt((v.xcor()-g/2-source.xcor()) ** 2 +
                   (v.ycor()+l-source.ycor()) ** 2)
    vell = k * (k1 + (k2*dl ** 2))
    velr = k * (k1 + (k2*dr ** 2))

    vl.goto(v.xcor()-g/2, v.ycor()+l)
    vr.goto(v.xcor()+g/2, v.ycor()+l)
    vr.dx = vell*abs(vl.xcor()-source.xcor())/dl
    vr.dy = vell*abs(vl.ycor()-source.ycor())/dl
    vl.dx = velr*abs(vr.xcor()-source.xcor())/dr
    vl.dy = velr*abs(vr.ycor()-source.ycor())/dr
    if v.dx > 0:
        v.dx = (vl.dx+vr.dx)
    else:
        v.dx = -(vl.dx+vr.dx)
    if v.dy > 0:
        v.dy = (vl.dy+vr.dy)
    else:
        v.dy = -(vl.dy+vr.dy)

    print("x = ", v.xcor(), " y = ", v.ycor(), "Vx = ", v.dx, "Vy = ", v.dy)


    v.sety(v.ycor()-v.dy)
    v.setx(v.xcor()-v.dx)



wn.mainloop()
