import pygame, sys
pygame.init()

import board
import sudokucell
import button

size = width, height = 600, 800
white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode(size)

def setup_game():
    margin = 30
    cellsize = (width-margin*2)//9
    sudokuboard = []
    gray = (128, 128, 128)
    for x in range(9):
        sudokuboard.append([])
        for y in range(9):
            sudokuboard[x].append(sudokucell.sudokucell(x, y, x*cellsize + margin, y * cellsize + margin, cellsize))

    gameboard = board.board(screen, sudokuboard)
    solve_button = button.button(screen, gray, 390, 650, 120, 50, "solve")
    start_button = button.button(screen, gray, 90, 650, 120, 50, "start")
    gameboard.isstarted = True
    start_button.draw()
    solve_button.draw()
    gameboard.draw()
    return gameboard, solve_button, start_button

if __name__ == "__main__":
    gameboard, solve, start = setup_game()
    cellselected = None
    
    while True:

        for event in pygame.event.get():

            mouse_pos = pygame.mouse.get_pos()
            
            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = gameboard.translate_mouse_value(mouse_pos[0]), gameboard.translate_mouse_value(mouse_pos[1])
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
                
        screen.fill(white)
        solve.draw()
        start.draw()
        gameboard.draw()
        pygame.display.update()