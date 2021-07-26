import random
import pygame

class board():

    def __init__(self, screen, board=None):
        self.screen = screen
        self.gameboard = []
        if board:
            self.gameboard = board
        self.white = (255, 255, 255)
        self.cols = {}
        self.rows = {}
        self.block = {}

        for x in range(9):        
            self.cols[x] = set([x for x in range(1, 10)])
            self.block[x] = set([x for x in range(1, 10)])
            self.rows[x] = set([x for x in range(1, 10)]) 

    
    def translate_mouse_value(self, val):
        border = 30
        size = 60
        return (val-border) // (size)

    
    
    # True if there are no values to add to a row, column or 3x3 block. otherwise false.
    def solved(self):
        return self.emptyrows() and self.emptycols() and self.emptyblocks()

    def emptyblocks(self):
        for x in self.block.keys():
            if len(self.block[x]) > 0:
                return False
        return True

    def emptyrows(self):
        for x in self.rows.keys():
            if len(self.rows[x]) > 0:
                return False
        return True

    def emptycols(self):
        for x in self.cols.keys():
            if len(self.cols[x]) > 0:
                return False
        return True

    def draw(self):
        for row in self.gameboard:
            for cell in row:
                cell.draw(self.screen)
        
    ## sets up a new game with a 20% chance of adding a value to a blcok for a new game.
    def setup_new_game(self):
        for i in range(len(self.gameboard)):
            for j in range(len(self.gameboard[i])):
                cell = self.gameboard[i][j]
                num = random.randint(1, 10)
                if num < 2:
                    to_choose = list(self.rows[i].intersection(self.cols[j]).intersection(self.block[cell.getblock()]))
                    index = random.randint(0, len(to_choose)-1)
                    toadd = to_choose[index]
                    cell.set_val(toadd)
                    cell.set_isset()
                    self.cols[j].remove(toadd)
                    self.rows[i].remove(toadd)
                    self.block[cell.getblock()].remove(toadd)

    def solve(self):
        return self.__solve__(0, 0)

    # 'Private' method for solving the current game board. This method uses the backtracking
    # paradigm to solve the current game board using the inserted mandatory values.
    def __solve__(self, row, col):
         
         if self.solved():
             return
         if row <= 8:
            cur = self.gameboard[row][col]
            if not cur.get_isset():
                for value in range(1, 10):
                
                        if value in self.cols[col] and value in self.rows[row] and value in self.block[cur.getblock()]:
                            cur.set_val(value)
                            self.cols[col].remove(value)
                            self.rows[row].remove(value)
                            self.block[cur.getblock()].remove(value)
                            self.screen.fill(self.white)
                            self.draw()
                        
                            if col == 8:
                                self.__solve__(row+1, 0)
                            else:
                                self.__solve__(row, col+1)

                            if self.solved():
                                return
                            
                            cur.set_val(0)
                            self.cols[col].add(value)
                            self.rows[row].add(value)
                            self.block[cur.getblock()].add(value)
                            pygame.display.update()
            else:
                if self.solved():
                    return
                if col == 8:
                    self.__solve__(row+1, 0)
                else:
                    self.__solve__(row, col+1)
                    
            return 
         

