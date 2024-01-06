# making a world

import turtle

class World:
    # variabler
    width = 0
    height = 0
    xBorder = 0
    yBorder = 0
    pen = None

    def __init__(self, win, width, height) -> None:
        self.width = width
        self.height = height

        win.title("Snake Game")
        win.bgcolor("blue")
        win.setup(width = self.width + 120, height = self.height + 120)
        win.tracer(0)

        # pen/text configuration in general
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()

    # Tegne en ramme
    def makeFrame(self, xBorder, yBorder):
        self.xBorder = xBorder
        self.yBorder = yBorder
        frame = turtle.Turtle()
        frame.pen(pencolor="white", pensize=5)
        frame.penup()
        frame.goto(-(xBorder+8), -(yBorder+8))
        frame.pendown()
        for _ in range(2):
            frame.forward(self.width+16)
            frame.left(90)
            frame.forward(self.height+16)
            frame.left(90)
        frame.hideturtle()

    def printScore(self, score, highScore):
        self.pen.clear()
        self.pen.goto(0, self.yBorder + 8) # position
        self.pen.write(f"Score : {score}      High Score : {highScore}", align="center",
                font=("candara", 22, "bold"))
