from graphics import *
from random import *

"""
createPipe: Function creates pipe by randomly generating the height of the bottom pipe and creating the top pipe accounting 
for the gap and window height. It takes three inputs of window, initial x-coordinate, and the gap between the top and bottom height

- Bottom pipe height is randomized between range. The rectangle x-coordinate is from the input (usually is off window screen) second 
point is hard-corded to 75 to create pipe width. y-coordinate subtracts the height of the window by randomized height and second point 
second point is 503 to drawn to start on ground image

- Top pipe x-coordinates are the same as the bottom pipes, but y takes into account the window, the gap, and the height of the bottom pipe

- Both pipes are returned. 
"""

def createPipe(win, x, gap):
    bh = randint(100, 400) 
    
    bp = Rectangle(Point(x, 600 - bh), Point(x + 75, 503)) 
    bp.setFill("green")
    bp.draw(win)
    
    tp = Rectangle(Point(x, 0), Point(x + 75, 600 - bh - gap))
    tp.setFill("green")
    tp.draw(win)
    
    #Will be used to track score
    tp.passed = False
    
    return tp, bp

"""
collision: Boolean that checks is flappy touches either the top or bottom pipe as well as if flappy touches the ground. 

- 'For loop' for each pipe created, check if flappy, the center x-coordinate (17 is added to represent the edge of flappy: top or bottom)
and see if it touches the top pipe. Then check the bottom pipe. If true, then return true. The same goes for flappy touching the ground.

- Else false: allows game to keep going normally.
"""
def collision(flappy, pipes):
    for tp, bp in pipes:
        if flappy.getAnchor().getX() + 17 > tp.getP1().getX() and flappy.getAnchor().getX() - 17 < tp.getP2().getX():
            if flappy.getAnchor().getY() - 17 < tp.getP2().getY() or flappy.getAnchor().getY() + 17 > bp.getP1().getY():
                return True
    
    #If flappy touches base/floor, return True
    if flappy.getAnchor().getY() + 17 > 500:  
        return True
    
    #Else False
    return False

"""
For game_over and winner, these texts are drawn onto screen if collision is true or if the user scores 20 points. 
"""
#Utilized if collision occurs
def game_over(win):
    gmovr = Text(Point(200, 220), "GAME OVER")
    gmovr.setSize(30)
    gmovr.setFill("red")
    gmovr.draw(win)
    
#Utilized when user reaches a score of 20
def winner(win):
    win_text = Text(Point(200, 220), "YOU WIN!!")
    win_text.setSize(30)
    win_text.setFill("red")
    win_text.draw(win)