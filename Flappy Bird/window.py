from graphics import *

"""
- Function code from class 

drawButton: Function creates rectangle with text in the center. It takes in five inputs - Center point of the rectangle, the window 
that the shape will be drawm, the width and height, and what text will be displayed in the middle. 

Used to create the four buttons in the game: Start, Exit, Replay, and Instructions
"""

def drawButton(center, win, w, h, text):
    xc, yc = center.getX(), center.getY()
    w, h = w // 2, h // 2
    
    button = Rectangle(Point(xc - w, yc - h), Point(xc + w, yc + h))
    button.setFill('orange')
    button.draw(win)
    
    label = Text(Point(xc, yc), text)
    label.draw(win)

    return button, label

"""
- Function code from class 

clicked: Gets button coordinates and user input to see if user input is within the bounds of the button created

Works in tandem with drawButton.
"""

def clicked(button, p):
    xlo, ylo = button.getP1().getX(), button.getP1().getY()
    xhi, yhi = button.getP2().getX(), button.getP2().getY()
    x, y = p.getX(), p.getY()
    
    return (xlo < x < xhi) and (ylo < y < yhi)


"""
Instruct: takes window as input. Instructions list is created with all wanted sentences. 'For loop' is created to draw each sentence 
30 units from eachother. Drawn initially at y = 150 and each instance of the loop adds 30 to the y-coordinate to create this. Each 
sentence is appended to a list and that list is returned. 
"""
def instruct(win):
    instructions = ["Welcome to Flappy Bird!",
                    "Use the spacebar to make flappy fly.",
                    "Avoid hitting the pipes!",
                    "The game begins as soon as you hit Start so,",
                    "Get Ready!!!",
                    "Score 20 points and you win the game!",]
    
    #Draw each sentence 30 units from eachother 
    y = 150
    words = []
    for sent in instructions:
        text = Text(Point(200, y), sent)
        text.setSize(15)
        text.setFill("black")
        text.draw(win)
        words.append(text)
        y += 30  
        
    return words

"""
restart_game: The purpose of this function was to redraw all splash screen items and actions (clicked buttons) if the user
chooses to replay the game after death or win. It also initialized the game flappy bird as well as the score. Function also takes
window as input.
"""
def restart_game(win):
    
    
    #Undraws all currently drawn items before starting restart game sequence
    for items in win.items[:]:
        items.undraw()

        
    b = Image(Point(200, 250), "background-day.png")
    b.draw(win)
    f = Image(Point(200, 575), "base.png")
    f.draw(win)
    
    flappy = Image(Point(200, 200), "flappy.png") 
    flappy.draw(win)
    
    title = Text(Point(200, 260), "Get Ready!")
    title.setSize(30)
    title.draw(win)
    
    start, slabel = drawButton(Point(200, 310), win, 100, 50, "Start")
    exit, elabel = drawButton(Point(200, 380), win, 100, 50, "Exit")
    
    instructions = Rectangle(Point(310, 20), Point(380, 50))
    instructions.setFill("orange")
    instructions.draw(win)
    
    txt = Text(instructions.getCenter(), "Instructions")
    txt.setFill("black")  
    txt.draw(win)
    
    #User input to start or exit game as well as open or close instructions
    while True:
        click = win.getMouse()
        if clicked(exit, click): 
            win.close()
        if clicked(start, click):  
            break  
        if clicked(instructions, click): 
            bx = Rectangle(Point(20, 130), Point(380, 320))
            bx.setFill("white")
            bx.draw(win)
            
            it = instruct(win)  
            
            win.getMouse()  
            bx.undraw()  
            
            for text in it:
                text.undraw()

            continue
            
    title.undraw()
    start.undraw()
    slabel.undraw()
    exit.undraw()
    elabel.undraw()
    instructions.undraw()
    txt.undraw()
    flappy.undraw()  
    
    flappysm = Image(Point(200, 200), "flappy copy.png")
    flappysm.draw(win)
    
    score = Text(Point(50, 565), "Score: 0")
    score.setSize(20)
    score.setFill("black")
    score.draw(win)
    
    return flappysm, score 


