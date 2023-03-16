
from tkinter import *
import random

def move_left(self):
    x1, y1, x2, y2 = canvas.coords(player)
    if x1 > 0:
        canvas.move(player, -min(x1, 10), 0)

def move_right(self):
    x1, y1, x2, y2 = canvas.coords(player)
    if x2 < width:
        canvas.move(player, min(10, width - x2), 0)

def AI_racket():
    x1, y1, x2, y2 = canvas.coords(AI_rack)
    bx1, by1, bx2, by2 = canvas.coords(ball)
    if bx1 < x1 + (x2 - x1)/2:
        dx = -2
    else:
        dx = 2
    if x2 + dx > width or x1 + dx < 0:
        dx = -dx
    canvas.move(AI_rack, dx, 0)

def check_collision():
    global dx, dy, score
    x1, y1, x2, y2 = canvas.coords(ball)
    overlapping = canvas.find_overlapping(x1, y1, x2, y2)
    for object in overlapping:
        if object == player:
            dy = -abs(dy)
        elif object == AI_rack:
            dy = abs(dy)
            score += 1
            canvas.itemconfig(score_text, text = f"Score: {score}")
    if x2 > width or x1 < 0: 
        dx = -dx
    if y2 > height:
        game_over()
    elif y1 < 0:
        dy = -dy

def game_over():
    canvas.itemconfig(game_over_text, state = NORMAL)
    canvas.unbind_all("<KeyPress-Left>")
    canvas.unbind_all("<KeyPress-Right>")

def animation():
    global dx, dy, score
    check_collision()
    canvas.move(ball, dx, dy)
    AI_racket()
    canvas.after(5, animation)

if __name__ == '__main__':
    # main program
    gui = Tk() 
    canvas = Canvas(gui, width = 400, height = 400) 
    ball = canvas.create_oval(100, 100, 125, 125, fill = "red")
    player = canvas.create_rectangle(150, 380, 250, 390, fill = "purple")
    AI_rack = canvas.create_rectangle(150, 10, 250, 20, fill = "black")
    score = 0
    score_text = canvas.create_text(50, 50, text = f"Score: {score}", font = ("Times", 15))
    canvas.pack()
    width = int(canvas.cget("width"))
    height = int(canvas.cget("height"))
    game_over_text = canvas.create_text(width / 2, height / 2, text = "gg ez go next", font = ("Times", 40), state = HIDDEN)
    dx, dy = random.choice([-2, 2]), random.choice([-2, 2])
    canvas.bind_all("<KeyPress-Left>", move_left)
    canvas.bind_all("<KeyPress-Right>", move_right)
    animation()
    gui.mainloop()
