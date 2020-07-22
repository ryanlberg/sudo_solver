import pygame, sys, random
import time
pygame.init()

sys.setrecursionlimit(10000)

size = width, height = 600, 800

white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
font = pygame.font.SysFont("Courier New", 36)
screen = pygame.display.set_mode(size)

class board():

    def __init__(self, board=None):
        self.gameboard = []
        if board:
            self.gameboard = board

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

    def emptyblocks(self):
        for x in self.block.keys():
            if len(self.block[x]) > 0:
                return False
        return True
    
    def solved(self):
        return self.emptyrows() and self.emptycols() and self.emptyblocks()

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
                cell.draw(screen)
        
    def setup_new_game(self):
        for i in range(len(self.gameboard)):
            for j in range(len(self.gameboard[i])):
                cell = self.gameboard[i][j]
                num = random.randint(1, 10)
                if num < 2:
                    to_choose = list(self.rows[i].intersection(self.cols[j]).intersection(self.block[cell.getblock()]))
                    print(to_choose)
                    index = random.randint(0, len(to_choose)-1)
                    toadd = to_choose[index]
                    cell.set_val(toadd)
                    cell.set_isset()
                    self.cols[j].remove(toadd)
                    self.rows[i].remove(toadd)
                    self.block[cell.getblock()].remove(toadd)

    def solve(self):
        return self.__solve__(0, 0)

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
                            screen.fill(white)
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
         





class sudokucell:

    def __init__(self, row, col, posx, posy, size):
        self.value = 0
        self.posx = posx
        self.posy = posy
        self.row = row
        self.col = col
        self.size = size
        self.isset = False
        self.isstarted = False
        self.color = black

    def draw(self, screen):
         border = 3
         draw = ""
         if not self.value == 0:
             draw = str(self.value)
         cellrect = pygame.Rect(self.posx, self.posy, self.size, self.size)
         pygame.draw.rect(screen, self.color, cellrect, border)
         text_surf = font.render(draw, True, black)
         midx = cellrect.centerx - 10
         midy = cellrect.centery - 18
         screen.blit(text_surf, (midx, midy))
         
    def get_col(self):
        return self.col 

    def getblock(self):
        return self.__translate__(self.row, self.col)

    def get_val(self):
        return self.value

    def set_isset(self):
        self.isset = True

    def get_isset(self):
        return self.isset

    def set_val(self, value):
        self.value = value

    def __translate__(self, row, col):
        if row >= 0 and row <= 2:
            if col >= 0 and col <=2:
                return 0
            elif col >= 3 and col <=5:
                return 1
            elif col >= 6 and col <= 8:
                return 2
        elif row >= 3 and row <= 5:
            if col >= 0 and col <=2:
                return 3
            elif col >= 3 and col <=5:
                return 4
            elif col >= 6 and col <= 8:
                return 5
        elif row >= 6 and row <= 8:
            if col >= 0 and col <= 2:
                return 6
            elif col >= 3 and col <= 5:
                return 7
            elif col >= 6 and col <= 8:
                return 8
   
    def click(self, screen):
        self.color = (0, 128, 0)
        self.draw(screen)
        

    def __str__(self):
        return f'val: {self.value}, row: {self.row}, col: {self.col}, block: block: {self.getblock()}'

    def update(self, value):
       
        self.value = value

class button():

    def __init__(self, color, x, y, width, height, text= ""):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self):
        border = 3
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        button_text_surf = font.render(self.text, True, black)
        pygame.draw.rect(screen, black, button_rect, border) 
        textx = self.x +(self.width//2- button_text_surf.get_width()//2)
        texty = self.y + (self.height//2 - button_text_surf.get_height()//2)
        screen.blit(button_text_surf, (textx, texty))

    def isClicked(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False


def setup_game():
    margin = 30
    cellsize = (width-margin*2)//9
    print(cellsize)
    sudokuboard = []
    for x in range(9):
        sudokuboard.append([])
        for y in range(9):
            sudokuboard[x].append(sudokucell(x, y, x*cellsize + margin, y * cellsize + margin, cellsize))

    gameboard = board(sudokuboard)
    solve = button(gray, 390, 650, 120, 50, "solve")
    start = button(gray, 90, 650, 120, 50, "start")
    gameboard.isstarted = True
    start.draw()
    solve.draw()
    gameboard.draw()
    return gameboard, solve, start


if __name__ == "__main__":
    gameboard, solve, start = setup_game()
    cellselected = None
    while True:

        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            
            
            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = gameboard.translate_mouse_value(mouse_pos[0]), gameboard.translate_mouse_value(mouse_pos[1])
                print(y, x)
                if solve.isClicked(mouse_pos):
                    gameboard.solve()
                
                if start.isClicked(mouse_pos):
                    gameboard, solve, start = setup_game()
                    gameboard.setup_new_game() 
                
                if y >= 0 and y <= 8 and x >= 0 and x <= 8:
                    if cellselected:
                        cellselected.color = black
                    cellselected = gameboard.gameboard[x][y]
                    cellselected.click(screen)
                
                   

            if event.type == pygame.KEYDOWN:
                if cellselected:
    
                    if event.key == pygame.K_1:                    
                        cellselected.update(1)
                    elif event.key == pygame.K_2:  
                        cellselected.update(2)
                    elif event.key == pygame.K_3:
                       
                        cellselected.update(3)
                    elif event.key == pygame.K_4:
                       
                        cellselected.update(4)
                    elif event.key == pygame.K_5:
                       
                        cellselected.update(5)
                    elif event.key == pygame.K_6:
                       
                        cellselected.update(6)
                    elif event.key == pygame.K_7:
                        
                        cellselected.update(7)
                    elif event.key == pygame.K_8:
                        
                        cellselected.update(8)
                    elif event.key == pygame.K_9:
                        
                        cellselected.update(9)
                    cellselected.color = black
                    cellselected = None
                

            
            #print(gameboard.translate_mouse_value(x), gameboard.translate_mouse_value(y))
        screen.fill(white)
        solve.draw()
        start.draw()
        gameboard.draw()
        pygame.display.update()