import turtle

def draw_circle(max_diameter,no_of_circle,no_of_inner_circle):
    circle = float(no_of_circle)
    angle = (360/circle)
    for i in range (0,no_of_circle):
        dia = max_diameter
        for j in range(0,no_of_inner_circle):
            fika.circle(dia,360)
            dia -= (max_diameter/no_of_inner_circle)
        fika.right(angle)
        
fika = turtle.Turtle()
fika.speed(15)
fika.color("yellow")
window = turtle.Screen()
window.bgcolor("red")

draw_circle(100,30,4)
window.exitonclick()
