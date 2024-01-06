'''
VIDEREUTVIKLET BASERT PÅ EN IDE OG KODE FRA: 
https://www.geeksforgeeks.org/create-a-snake-game-using-turtle-in-python/ (ca. 160 linjer)
Se readme-fil for detaljer om hvordan jeg videreutviklet spillet

** Terje Haldorsen **
'''

# Denne hovedfilen inneholder primaert styring (kontroller) av slangen
# og av tiden, samt faste stoerrelser (variabler) og en del metoder for
# behandling av maten (kan med fordel flytte noe av det til food.py)

# import required modules
# from tkinter import Y # TODO: sjekke om dette brukes, evt. hvor
import turtle
import time
import random
import food as fd
import world
import game
import menu

START_DELAY = 0.15
delay = START_DELAY

# tidsstyring
startTime = time.time()
seconds = 0
pausedTime = 0.0

# kontroll for start, stopp og pause
paused = True
quit = False

# Standardverdier for vindusstørrelse
WIDTH_M = 800
HEIGHT_M = 600
WIDTH_S = WIDTH_M/2
HEIGHT_S = HEIGHT_M/2
WIDTH_L = WIDTH_M * 1.5
HEIGHT_L = HEIGHT_M * 1.5

# Standard enhet i spillet (stoerrelse av segmenter, forflytning m.m.)
UNIT = 20

# OPPSETT fra MENY foer turtle-vinduet aapner
width = 0
height = 0
fortsett = True
menu.printStartMenu()
choice = menu.choose()
while fortsett: # Meny
    if choice == '0':
        menu.printStartMenu()
        choice = menu.choose()
    elif choice == '1':
        width = WIDTH_S
        height = HEIGHT_S
        fortsett = False
    elif choice == '2':
        width = WIDTH_M
        height = HEIGHT_M
        fortsett = False
    elif choice == '3':
        width = WIDTH_L
        height = HEIGHT_L
        fortsett = False
    

    else: 
        choice = menu.newChoice()


# Definere ytterkanter som x- og y-koordinater
XBORDER = width/2
YBORDER = height/2

# Creating a window screen with frame
wn = turtle.Screen() # singleton instance of a Screen object
wor = world.World(wn, width, height) # initielle verdier (som ikke bestemmes av game)
wor.makeFrame(XBORDER, YBORDER) # frame

# Creating a game (in world)
gm = game.Game(wor, UNIT)
head = gm.pl1

# assigning key directions
# general method
def heading(newDir, illegalDir):
    global paused
    if paused:
        paused = False
    # DESIGN-valg: her vil trykk paa retning-tast foere til start av spill,
    # men IKKE til endring av retningen slangen gikk i foer pausen
    else: 
        if head.getDirection() != illegalDir: 
            head.setDirection(newDir)

# specific methods
def goup():
    heading("up", "down")

def godown():
    heading("down", "up")

def goleft():
    heading("left", "right")
    
def goright():
    heading("right", "left")

def grow(snake): # vekst (generalisere på sikt)
    # Adding segment
    global delay
    snake.addSegment()
    delay -= 0.001

def scoring(food): # poeng
    gm.updateScore(food.get_points())
    gm.printScore()

# hente tilfeldige koordinater innenfor spilleområdet
def getRndX():    
    x = random.randint(-(XBORDER - 30), (XBORDER - 30))
    return x
def getRndY():
    y = random.randint(-(YBORDER - 30), (YBORDER - 30))
    return y

# flytter enkeltobjekter (mat)
def moveFood(food):
    fortsett = True
    while fortsett:    
        x = getRndX()
        y = getRndY()

        # TODO: denne maa SKRIVES OM til ny design!
        # Maal: sjekke at maten ikke havner under slangehalen
        # tryAgain = False
        # for segment in segments:
        #     xcor = segment.xcor()
        #     ycor = segment.ycor()
        #     # MERK: mulig jeg kan bruke verdien +- 10 her?!
        #     if ((x+20) > xcor and (x-20) < xcor and (y+20) > ycor and (y-20) < ycor):
        #         tryAgain = True
        #         break

        # check for food near snake's head
        xcor = head.xcor()
        ycor = head.ycor()
        if ((x + UNIT) > xcor and (x - UNIT) < xcor and (y + UNIT) > ycor and (y - UNIT) < ycor):
            continue # food is too close
        else: # ok, move food to the free position (x, y)
            food.goto(x, y) 
            fortsett = False

# "The kitchen": sjekker hver enkelt mat om det er på tide å gjemme/vise mat
def foodAppearance(food): 
    global seconds
    if seconds > food.get_timer(): # sammenligner spilltid med timeren fra objektet
        if food.xcor() < XBORDER: # sjekke om maten er på brettet 
            food.goto(XBORDER + 500, YBORDER + 500)
            food.set_timer(food.get_hidden()) # endrer timer med hvor lenge den skal skjules 
        else: # hvis ikke, flytt inn på brettet
            moveFood(food)
            food.set_timer(food.get_visible()) # endrer timer med hvor lenge den skal vises 

# reset mellom hver runde: flytte slangehode i midten, miste hale, poengtavle, mat tilfeldig sted
def reset():
    pauseGame()
    global score
    global delay
    global startTime
    global seconds
    global pausedTime
    delay = START_DELAY
    time.sleep(1)
    head.goto(0, 0)
    head.setDirection("right")

    for food in allFood:
        food.goto(XBORDER + 500, YBORDER + 500)  # Mat flytte seg unna vei (midlertidig)
        food.reset_timer() # resetter timer for hver food
        if food.get_type() == 1: # flytt på all mat av type 1
            moveFood(food)
    score = 0
    startTime = time.time() # resetting time
    seconds = 0
    pausedTime = 0

    # update scores and graphic
    gm.resetScore()
    gm.printScore()

def quitGame():
    global quit
    quit = True

def pauseGame(): # stopper/"fryser" spillet
    global paused
    paused = True

def stopPause(): # fortsetter spillet
    global paused
    paused = False

# food in the game
# ****************
# instillinger for antall objekter av hver type mat
t1 = 3 # antall av type 1
t2 = 2 # etc.
t3 = 1 
allFood = []
for i in range(0,t1,1): # lager mat av type tx
    allFood.append(fd.Food(getRndX(), getRndY(), 1))
for i in range(0,t2,1): # lager mat av type tx
    allFood.append(fd.Food((XBORDER + 500), (YBORDER + 500), 2)) # starter utenfor brettet
for i in range(0,t3,1): # lager mat av type tx
    allFood.append(fd.Food((XBORDER + 500), (YBORDER + 500), 3)) # starter utenfor brettet

# kontroll av slangen
wn.listen()
# merknad: case-sensitiv styring
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

# pause and quit
wn.onkeypress(quitGame, "Q") # Stanser spillet helt (men vinduet maa lukkes manuelt?)
wn.onkeypress(pauseGame, "q") # Pauser spillet (evt. kan avsluttes uten feilkommando naar spiller lukker vinduet)

# alternative taster
wn.onkeypress(goup, "Up")
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft, "Left")
wn.onkeypress(goright, "Right")

# Info in user terminal
print(f'Spillet har startet i eget vindu.\n\
Gaa til vinduet og trykk deretter paa en styringstast for aa starte.')

# Main Gameplay
# *************
while not quit:

    wn.update()
  
    while not paused:
        # Check events 
          
        # 1) Touching food 
        isEaten = head.isEating(allFood) # returns food-object if snake is eating, else False
        # Handle food
        if isinstance(isEaten, fd.Food):
            isEaten.goto(XBORDER + 500, YBORDER + 500) # move food temporarily away from the frame
            # setting the food's internal timer
            isEaten.set_timer(seconds - isEaten.get_timer() + isEaten.get_hidden()) 
            grow(head) # growing (TODO: which snake?)
            scoring(isEaten) # TODO: for which snake?
        
        # 2) Collision with border
        if (head.xcor() > (XBORDER-10) or head.xcor() < -(XBORDER-10)
            or head.ycor() > (YBORDER-10) or head.ycor() < -(YBORDER-10)):
            head.headTransformed()
            wn.update()
            reset() # resetting time and more
            time.sleep(1) # a short break
            gm.reset() # resetting game
            break
             
        # 3) Move snake. While doing so: checking for head collisions with own body segments
        if not head.move(): 
            # self-collision has appeared
            wn.update() # in order to show snake's head at collision site
            reset() # resetting time and more
            time.sleep(1)
            gm.reset() # resetting game
            break

        # 4) Check if colliding with the other snake in 2-player-mode
        # -- to be developed... --

        # Food disappear and reappear
        elapsed = time.time() - pausedTime - startTime
        tempSeconds = int(elapsed) # checking time temporarily
        if tempSeconds > seconds:
            seconds = tempSeconds # endres hvert sekund
            # print("seconds", seconds) # for DEBUGGING
            
            # check food Appearence
            for food in allFood:
                foodAppearance(food) # visit the "kitchen" :-)
        
            # Increase speed
            if seconds % 15 == 0: # fixed intervals
                delay = delay * game.factor(seconds) # increase speed (reduce delay)
        
        time.sleep(delay)
        wn.update()  
    
    pausedTime += delay
    time.sleep(delay)

wn.bye() # Avslutter spillet og lukker vinduet
wn.mainloop()
