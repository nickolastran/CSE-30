
class Board:
      def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
            self.sign = " "
            self.size = 3
            self.board = list(self.sign * self.size ** 2)
            # the winner"s sign O or X
            self.winner = ""

      def get_size(self):
        return self.size                                                                # optional, return the board size (an instance size)

      def get_winner(self):
        return self.winner                                                              # return the winner"s sign O or X (an instance winner)

      def set(self, cell, sign):
            valid_choices = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]      # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
            index = valid_choices.index(cell)                                           # you can use a tuple ("A1", "B1",...) to obtain indexes
            self.board[index] = sign

      def isempty(self, cell):
            cells = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
            if self.board[cells.index(cell)] == " ":                                  # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
                  return True                                                           # return True if the cell is empty (not marked with X or O)
            else:
                  return False

      def isdone(self):
            done = False
            if (self.board[0] != " ") and (self.board[0] == self.board[3] == self.board[6]):
                  self.winner = self.board[0]
                  return True
            elif (self.board[0] != " ") and (self.board[0] == self.board[1] == self.board[2]):
                  self.winner = self.board[0]
                  return True
            elif (self.board[0] != " ") and (self.board[0] == self.board[4] == self.board[8]):
                  self.winner = self.board[0]
                  return True
            elif (self.board[6] != " ") and (self.board[6] == self.board[7] == self.board[8]):
                  self.winner = self.board[6]
                  return True
            elif (self.board[6] != " ") and (self.board[6] == self.board[4] == self.board[2]):
                  self.winner = self.board[6]
                  return True
            elif (self.board[1] != " ") and (self.board[1] == self.board[4] == self.board[7]):
                  self.winner = self.board[1]
                  return True
            elif (self.board[2] != " ") and (self.board[2] == self.board[5] == self.board[8]):
                  self.winner = self.board[2]
                  return True
            elif (self.board[3] != " ") and (self.board[3] == self.board[4] == self.board[5]):
                  self.winner = self.board[3]
                  return True
            elif " " not in self.board:
                  self.winner = ""
                  return True
            return done

      def show(self):
            print("   A   B   C")
            print(" +---+---+---+")
            print("1| {} | {} | {} |".format(self.board[0], self.board[3], self.board[6]))
            print(" +---+---+---+")
            print("2| {} | {} | {} |".format(self.board[1], self.board[4], self.board[7]))
            print(" +---+---+---+")
            print("3| {} | {} | {} |".format(self.board[2], self.board[5], self.board[8]))
            print(" +---+---+---+")
            # draw the board