
import turtle

t = turtle.Turtle()                                       # main program
screen = turtle.Screen()                                  # screen setup (size, background color, title, start of drawing)
screen.setup(900, 900)
screen.bgcolor("ivory")
screen.title("Polygon Recursions")
sides = 0

t.hideturtle()                                            # make the turtle invisible
t.penup()
t.goto(-300,100)
t.showturtle()                                            # make the turtle visible
t.pendown()

def polygon(size, n):
    t.pendown()
   # t.goto(250,100)
    t.fillcolor("purple")
    t.begin_fill()
    for x in range(n):
        t.forward(size)
        t.right(360 / n)
    
    t.goto(200,100)
    t.end_fill()

def polygon_recursive(size, n):
    global sides
    if sides == 0:
        sides = (360 / n)
    t.pendown()
    t.begin_fill()
    if n <= 0:
        sides = 0
        return n
    else:
        t.forward(size)
        t.right(sides)
        return polygon_recursive(size, n - 1)

polygon(150,5)                                          # size of shape, number of sides
polygon_recursive(150, 5)                               # size of shape, number of sides
screen.mainloop()                                       # keeps the screen active without closing
