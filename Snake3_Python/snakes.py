# Careful... Snakes!

import turtle

class Snakes(turtle.Turtle):
    length = 0 # length of the TAIL (all except head)
    START_LENGTH = 4
    segments = [] # tail segments
    tailColor1 = "orange"
    tailColor2 = "brown"
    direction = "right" # fixed direction at start
    unit = None

    def __init__(self, x, y, unit) -> None:
        # self.__type = type # Player or computer
        turtle.Turtle.__init__(self) 
        self.unit = unit
        self.penup()
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.speed(0)
        self.showturtle()
        # creating and placing tail segments left of the head
        self.placeSnake(x, y)
                   

    def addSegment(self):
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        if self.length % 2 == 0: # etter ide fra en elev
            new_segment.color(self.tailColor1)  
        else:
            new_segment.color(self.tailColor2)
        new_segment.penup()
        self.segments.append(new_segment)
        self.length += 1
    
    def placeSnake(self, x, y): # place the snake with tail at start position
        self.goto(x * self.unit, y * self.unit)
        for i in range(self.START_LENGTH):
            self.addSegment()
            self.segments[i].goto(self.unit * (x - i - 1), self.unit * y)

    def reset(self, x, y):
        for segment in self.segments:
           segment.goto(5000, 5000) # alternativt (XBORDER + 500, YBORDER + 500)
        self.segments.clear()
        self.length = 0
        self.setheading(0)
        self.shearfactor(0)
        self.placeSnake(x, y)        

    def headTransformed(self): # used when colliding
        self.setheading(5) # awkward orientation of head :-)
        self.shearfactor(-0.2) # more awkward layout

    def selfCollided(self, x, y):
        if (x - self.xcor() == 0) and (y - self.ycor() == 0):
            return True
        return False
    
    def move(self):    
        # move tail
        for index in range(self.length - 1, 0, -1): # iterate from last segm.
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()
            if not self.selfCollided(x, y):
                self.segments[index].goto(x, y)
            else:
                # hide tail-segment that collided in order to show head of snake
                self.segments[index-1].hideturtle()
                self.headTransformed()
                return False
            
        if len(self.segments) > 0: # first segm. gets head's coordinates
            x = self.xcor()
            y = self.ycor()
            self.segments[0].goto(x,y)
        
        # move head of snake
        if self.direction == "up":
            self.goto(x, y + self.unit)
        if self.direction == "down":
            self.goto(x, y - self.unit)
        if self.direction == "left":
            self.goto(x - self.unit, y)
        if self.direction == "right":
            self.goto(x + self.unit, y)
        return True

    def getDirection(self):
        return self.direction
    
    def setDirection(self, direction):
        self.direction = direction

    def isEating(self, allFood): # is the snake eating?
        for food in allFood:
            if self.distance(food) < self.unit:
                return food # if eating
        return False # if not eating
    