
# assignment: programming assignment 5
# author: Nickolas Tran
# date: 3/13/2023
# file: fifteen.py


import numpy as np
from graph import Graph
from random import choice


class Fifteen:
    def __init__(self, size = 4):
        self.tiles = np.array([i for i in range(1, size ** 2)] + [0])
        self.adj = [[1, 4],[0, 2, 5], [1, 3, 6], [2, 7], 
                    [0, 5, 8], [1, 4, 6, 9], [2, 5, 7, 10], 
                    [3, 6, 11], [4, 9, 12], [5, 8, 10, 13], 
                    [6, 9, 11, 14], [7, 10, 15], [8, 13], 
                    [9, 12, 14], [10, 13, 15], [11, 14]]


    def update(self, move):
        for i, value in enumerate(self.tiles):
            if value == move:
                move_tile = i
            if value == 0:
                empty_tile = i
        self.tiles[move_tile], self.tiles[empty_tile] = self.tiles[empty_tile], self.tiles[move_tile]


    def transpose(self, i, j):
        if self.is_valid_move(i, j):
            self.tiles[i], self.tiles[j] = self.tiles[j], self.tiles[i]
            return self.tiles


    def shuffle(self, steps = 100):
        index = np.where(self.tiles == 0)[0][0]
        for x in range(steps):
            move_index = choice(self.adj[index])
            self.tiles[index],self.tiles[move_index] = self.tiles[move_index],self.tiles[index]
            index = move_index


    def is_valid_move(self, move):
        move = np.where(self.tiles == int(move))[0][0]
        index = np.where(self.tiles == 0)[0][0]
        move_index = self.adj[index]
        if move in move_index:
            return True
        else:
            return False


    def is_solved(self):
        solutions = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])
        return np.array_equal(self.tiles, solutions)


    def draw(self):
        values = [str(i).rjust(2) if i != 0 else "  " for i in self.tiles]
        print("+---+---+---+---+")
        print("|{} |{} |{} |{} |".format(values[0], values[1], values[2], values[3]))
        print("+---+---+---+---+")
        print("|{} |{} |{} |{} |".format(values[4], values[5], values[6], values[7]))
        print("+---+---+---+---+")
        print("|{} |{} |{} |{} |".format(values[8], values[9], values[10], values[11]))
        print("+---+---+---+---+")
        print("|{} |{} |{} |{} |".format(values[12], values[13], values[14], values[15]))
        print("+---+---+---+---+")


    def __str__(self):
        string = ""
        for i in range(len(self.tiles)):
            if i == 4 or i == 8 or i == 12:
                string += "\n"
            if self.tiles[i] == 0:
                string += "   "
            else:
                string += "{:2d} ".format(self.tiles[i])
        string += "\n"
        return string


def solve(): # optional
    pass


def is_solvable(): # optional
    pass


if __name__ == "__main__":

    game = Fifteen()
    assert str(game) == " 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n"
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == " 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n"
    game.update(15)
    assert str(game) == " 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n"
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != " 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n"
    assert game.is_solved() == False

     
    """You should be able to play the game if you uncomment the code below"""  
    game = Fifteen()
    game.shuffle() 
    game.draw()
    while True:
        move = input("Enter your move or q to quit: ")
        if move == "q":
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print("Game over!")
