# making a game
import snakes

# factor for controlling game speed (lower delay = higher speed)
# [developing idea: might be used for changing game difficulty based on speed]
def factor(sec):
    progress = 1 + int(sec/90)
    f = 0.75 + progress * 0.05
    if f < 1: 
        return f
    return 1 # max speed (lowest possible delay in game)

class Game:
    wld = None # world
    score = 0
    highScore = 0
    snakeCount = 1
    pl1 = None # player 1
    pl2 = None # player 2 (when implemented)
    # player 1 starts here
    start1_X_units = 0
    start1_Y_units = 0
    # made ready for player 2...
    start2_X_units = 0
    start2_Y_units = -5

    def __init__(self, world, unit) -> None:
        self.wld = world
        self.wld.printScore(self.score, self.highScore)
        self.pl1 = snakes.Snakes(self.start1_X_units, self.start1_Y_units, unit)

    def updateScore(self, addPoints):
        self.score += addPoints
        if self.score > self.highScore:
            self.highScore = self.score

    def resetScore(self):
        self.score = 0

    def printScore(self):
        self.wld.printScore(self.score, self. highScore)

    # resetting between games (with no change in game mode)
    def reset(self):
        self.pl1.reset(self.start1_X_units, self.start1_Y_units)
        if self.pl2:
            self.pl2.reset(self.start2_X_units, self.start2_Y_units)