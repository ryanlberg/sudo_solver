import pygame

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
        self.font = pygame.font.SysFont("Courier New", 36)
        self.color = (0, 0, 0)

    # Draws individual sudokus cell on board with value if it has been set.
    def draw(self, screen):
         border = 3
         draw = ""
         if not self.value == 0:
             draw = str(self.value)
         cellrect = pygame.Rect(self.posx, self.posy, self.size, self.size)
         pygame.draw.rect(screen, self.color, cellrect, border)
         text_surf = self.font.render(draw, True, self.color)
         midx = cellrect.centerx - 10
         midy = cellrect.centery - 18
         screen.blit(text_surf, (midx, midy))
         
    # Returns which column the sudokucell was in.
    def get_col(self):
        return self.col 

    # Returns which 3x3 block the mouse click fell into. Values range from (0-8)
    def getblock(self):
        return self.__translate__(self.row, self.col)

    # Returns numerical value of sudokucell
    def get_val(self):
        return self.value

    # Sets the current value of the node to true if a value has been entered.
    def set_isset(self):
        self.isset = True


    def get_isset(self):
        return self.isset

    # Sets numerical value of sudokucell
    def set_val(self, value):
        self.value = value


    # Translation from row, column value to 3x3 cell block value for valid placement checking according to sudoku rules.
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
   
    # Highlights cell if clicked.
    def click(self, screen):
        self.color = (0, 128, 0)
        self.draw(screen)
        
    # return string value of cell for error checking.
    def __str__(self):
        return f'val: {self.value}, row: {self.row}, col: {self.col}, block: block: {self.getblock()}'

    #Update numerical value of cell (Same as set_val, but helps with clarity in code.)
    def update(self, value):
        self.value = value