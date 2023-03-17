
# assignment: programming assignment 5
# author: Nickolas Tran
# date: 3/16/2023
# file: game.py


from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
from random import choice
import numpy as np


def clickButton(gui, tiles, position):
    x = tiles.tiles[position - 1]
    if tiles.is_valid_move(x):
        tiles.update(x)
        updateBoard(gui, tiles)


def addButton(gui, tiles, font, position):
    return Button(gui, text = tiles, name = str(position), bg = "lavender",
                  fg = "black", font = font, height = 2, width = 8,
                  command = lambda : clickButton(gui, tiles, position))


def updateBoard(gui, tiles):
    win_messages = ["congrats", "gg", "ez", "peepee", "yeee"]
    for x in tiles.tiles:
        if tiles.tiles[x - 1] == 0:
            gui.nametowidget(str(x)).configure(text = " ")
        else:
            gui.nametowidget(str(x)).configure(text = str(tiles.tiles[x - 1]))
    if tiles.is_solved():
        print("You Win!")
        for x in tiles.tiles():
            gui.nametowidget(str(x)).configure(text = choice(win_messages))


def shuffle(gui, tiles, steps = 30):
    tiles.shuffle(steps)
    updateBoard(gui, tiles)


if __name__ == "__main__":

    tiles = Fifteen()

    empty = np.where(tiles.tiles == 0)[0][0]
    gui = Tk()
    gui.title("Fifteen")

    font = font.Font(family = "Segoe UI", size = "25", weight = "bold")

    buttons = []
    for x in tiles.tiles:
        newButton = addButton(gui, tiles, font, x)
        buttons.append(newButton)

    k = 4
    for i in range(k):
        for j in range(k):
            buttons[i * k + j].grid(row = i + 1, column = j, columnspan = 1)

    shuffle_button = Button(gui, text = "SHUFFLE", name = "shuffle",
                        bg = "lavender", fg = "black", font = font, height = 1,
                        width=10, command = lambda : shuffle(gui, tiles, empty))
    shuffle_button.grid(row=6, column=1, columnspan=2)
    
    tiles.shuffle()
    updateBoard(gui, tiles)

    gui.mainloop()
