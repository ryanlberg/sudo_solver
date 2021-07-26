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