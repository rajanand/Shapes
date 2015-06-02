import turtle

def draw_square():
    for i in range (0,4):
        fika.forward(100)
        fika.right(90)

def draw_circle(no_of_circle):
    angle = (360/float(no_of_circle))
    for j in range (0, no_of_circle):
        draw_square()
        fika.left(angle)
        
fika = turtle.Turtle()
fika.speed(15)
fika.color("yellow")
background = turtle.Screen()
background.bgcolor("red")

draw_circle(60)
background.exitonclick()
