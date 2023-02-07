
import turtle

t = turtle.Turtle()                                                  # main program
screen = turtle.Screen()                                             # screen setup (size, background color, title, start of drawing)
screen.setup(1000, 1000)
screen.bgcolor("lavender")
screen.title("Star Recursions")
sides = 0

t.hideturtle()                                                       # make the turtle invisible
t.penup()
t.goto(-450,100)
t.showturtle()                                                       # make the turtle visible
t.pendown()

def star(size, n, d = 2):
    t.pendown()
    t.goto(250,100)
    t.begin_fill()
    if (n % 2 != 0):
        for x in range(n):
            t.forward(size)
            t.right(360 * (d / n))

    else:
        for x in range(n):
            t.forward(size / (n / 2))
            for x in range(3):
                t.left(120)
                t.forward(size/(n / 2))
            t.right(360 / n)

def star_recursive(size, n, d = 2):
    global sides
    t.pendown()
    t.begin_fill()
    if sides == 0:
        sides = n

    if n == 0:
        sides = 0
        return n
    
    else:
        if (sides % 2 != 0):
            t.forward(size)
            t.right(360 * (d / sides))
            star_recursive(size, n - 1)
            
        else:
            t.forward(size / (sides / 2))
            t.left(120)
            t.forward(size / (sides / 2))
            t.right(360 / sides)
            star_recursive(sides, n - 1)
           
star_recursive(300, 5)                                         # size of shape, number of sides
star(300, 8)                                                   # size of shape, number of sides
screen.mainloop()                                              # keeps main screen on
