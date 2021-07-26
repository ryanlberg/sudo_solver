import pygame

class button():

    def __init__(self, screen, color, x, y, width, height, text= ""):
        self.color = color
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = (0, 0, 0) #black
        self.font = pygame.font.SysFont("Courier New", 36)

    def draw(self):
        border = 3
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        button_text_surf = self.font.render(self.text, True, self.color)
        pygame.draw.rect(self.screen, self.color, button_rect, border) 
        textx = self.x +(self.width//2- button_text_surf.get_width()//2)
        texty = self.y + (self.height//2 - button_text_surf.get_height()//2)
        self.screen.blit(button_text_surf, (textx, texty))

    def isClicked(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False