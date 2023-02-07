
import turtle

t = turtle.Turtle()                                     # main program set up
t._tracer(750)                                          # speed of the fractal
screen = turtle.Screen()                                # screen set up (size, color of background, title)
screen.setup(500, 500)
screen.bgcolor("light steel blue")
screen.title("Tree Fractal")

def draw_tree(branchs, leaves, angle):
    if leaves < 0:   
        t.pencolor("#3A5F0B")                           # color code for green leaves
        for i in range(4):
            t.right(90)
            t.forward(branchs * 1.5)
            t.dot(branchs * 1.5)
        t.pencolor("#53350A")                           # color code for brown trunks
        return leaves
    else:
        t.pencolor("#53350A")                           # color code for brown trunks
        t.pensize(leaves)
        t.forward(branchs)
        t.left(angle)
        draw_tree(branchs * 0.75, leaves - 1, angle)
        t.pensize(leaves * 2)
        t.right(angle * 2)
        draw_tree(branchs * 0.75, leaves - 1, angle)
        t.left(angle)
        t.penup()
        t.back(branchs)
        t.pendown()

t.left(90)
t.penup()
t.back(150)
t.pendown()
draw_tree(75, 10, 25)
screen.mainloop()                                       # leaves screen on 
