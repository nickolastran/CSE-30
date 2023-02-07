
from random import choice
import random 

class Player:
      def __init__(self, name, sign):
            self.name = name                                                                      # players name
            self.sign = sign                                                                      # players sign O or X

      def get_sign(self):
            return self.sign                                                                      # return an instance sign

      def get_name(self):
            return self.name                                                                      # return an instance name

      def choose(self, board):
            valid_choices = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
            while True: 
                  cell = input(f"{self.name}, {self.sign}: Enter a cell [A-C][1-3]:\n").upper()   # prompt the user to choose a cell
                  if cell in valid_choices:                                                       # if the user enters a valid string and the cell on the board is empty, update the board
                        if board.isempty(cell):                                                   # use the methods board.isempty(cell), and board.set(cell, sign)
                              board.set(cell, self.sign)
                              break
                        else:
                              print("You did not choose correctly.")                              # otherwise print a message that the input is wrong and rewrite the prompt
                  else:                                                                           # use the methods board.isempty(cell), and board.set(cell, sign)
                        print("You did not choose correctly.")

class AI(Player):
      def choose(self, board):
            print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
            valid_choices = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
            while True:
                  ai_choices = random.choice(valid_choices)
                  if board.isempty(ai_choices):
                       print(ai_choices)
                       board.set(ai_choices, self.sign)
                       break
                  else:
                       pass

class MiniMax(Player):
      def choose(self, board):
            print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
            cell = MiniMax.minimax(self, board, True, True)
            print(cell)
            board.set(cell, self.sign)

      def minimax(self, board, self_player, start):
            valid_choices = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]     # base case
            if self.sign == "X":
                  opponent_sign = "O"
            else:
                  opponent_sign = "X"

            if board.isdone():
                  if board.get_winner() == self.sign:
                        return 1                                                        # self is a winner

                  elif board.get_winner() == "":
                        return 0                                                        # is a tie

                  else:
                        return -1                                                       # self is a loser (opponent is a winner)

            else:
                  min_score = float("inf")                                              # maxscore = -10 (any small number < -1 or float(‘-inf'))
                  max_score = float("-inf")                                             # minscore = 10 (any big number > 1 or float(‘inf'))
                  move = ""
                  for cell in valid_choices:
                        if board.isempty(cell):
                              if self_player:
                                    board.set(cell, self.sign)
                                    score = MiniMax.minimax(self, board, False, False)
                                    if score > max_score:
                                        move = cell
                                        max_score = score
                                    board.set(cell, " ")

                              else:
                                    board.set(cell, opponent_sign)
                                    score = MiniMax.minimax(self, board, True, False)
                                    if score < min_score:
                                        min_score = score
                                    board.set(cell, " ")
                  if start:
                        return move

                  elif self_player:
                        return max_score

                  else:
                        return min_score
