from graphics import *
from random import *
from window import *
from gameFunc import *

"""
Main function runs game and utilizes all previously created functions to recreate the game Flappy Bird
"""
def main():
    
    #Pipe characteristic variables
    gap = 150   
    initialX = 400
    pipes = []
    
    #Initialize flappy bird movement
    gravity = 2.5 
    jump = -18 
    direction = 0  
    
    #Initialize window for splash screen and game to be drawn
    win = GraphWin("Flappy Bird", 400, 600, autoflush=False)
    
    while True:
        #Initialize score
        s = 0

        #If replay button was not clicked, exit was clicked, or function does not provide valid returns, break out of main function and close window.
        game = restart_game(win)
        if not game:
            return
        #Else input return values into function and continue with game
        flappysm, score = game
        
        #Create 20 pipes starting off screen 
        pipes.clear() #Clear pipes list before starting new loop
        for i in range(20):  
            pipex = initialX + i * 235
            pipes.append(createPipe(win, pipex, gap))

        while True:
            
            #While game is played, key (space) is checked. If space is pressed make flappy fly (decrease y-value or go up) else apply gravity (increase y-value)
            key = win.checkKey()

            if key == "space":
                direction = jump
            
            direction += gravity
            flappysm.move(0, direction) #Direction reflects user input and affected by variable jump and gravity
            
            #For each pipe created, move pipes across x-axis 
            for tp, bp in pipes: 
                tp.move(-3, 0)
                bp.move(-3, 0)

                #If the top pipes center x-coordinate < 200, and has not yet passed the center, add one to the score, return true for that pipe, and display increment.
                if tp.getCenter().getX() < 200 and not tp.passed:
                    s += 1  
                    tp.passed = True 
                    score.setText(f"Score: {s}") 
                    
            
            #If user scores 20 (passes 20 pipes), start winner sequence. Winner text as well as replay and exit buttons are drawn to the window.
            if s >= 20:
                winner(win)
                
                replay, rlabel = drawButton(Point(200, 270), win, 100, 50, "Replay")
                exit, elabel = drawButton(Point(200, 340), win, 100, 50, "Exit")
                
                while True:
                    click = win.getMouse()
    
                    if clicked(exit, click):
                        win.close()
    
                    if clicked(replay, click):
                        replay.undraw()
                        rlabel.undraw()
                        exit.undraw()
                        elabel.undraw()
                        break
                break
                        
            
            #If flappy touches pipe or floor (boolean returns true) then start gameover sequence. Gameover text as well as replay and exit buttons are drawn to the window. 
            if collision(flappysm, pipes):
                game_over(win)

                replay, rlabel = drawButton(Point(200, 270), win, 100, 50, "Replay")
                exit, elabel = drawButton(Point(200, 340), win, 100, 50, "Exit")

                while True:
                    click = win.getMouse()

                    if clicked(exit, click):
                        win.close()

                    if clicked(replay, click):
                        replay.undraw()
                        rlabel.undraw()
                        exit.undraw()
                        elabel.undraw()
                        break
                break

            update(30)


main()
