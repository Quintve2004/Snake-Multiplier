import time
import turtle
import random


# Window Setup
wd = turtle.Screen()
wd.setup(width=680, height=680)
wd.bgcolor("black")
wd.tracer(0)

# Characters Setup; We Need to Characters (two snakes)

# Player A
player_a = turtle.Turtle()
player_a.penup()
player_a.speed(0)
player_a.shape("square")
player_a.goto(300, 0)
player_a.color("yellow")
player_a.direction = "stop"

# Player B
player_b = turtle.Turtle()
player_b.penup()
player_b.speed(0)
player_b.shape("square")
player_b.goto(-300, 0)
player_b.color("blue")
player_b.direction = "stop"

# Food
food = turtle.Turtle()
food.penup()
food.speed(0)
food.shape("circle")
food.color("red")
food.goto(random.randint(-13,13) * 20, random.randint(-13,13) * 20)

food1 = turtle.Turtle()
food1.penup()
food1.speed(0)
food1.shape("circle")
food1.color("red")
food1.goto(random.randint(-13,13) * 20, random.randint(-13,13) * 20)

# Score
score_a = 0
score_b = 0

# StartButton
startbutton = turtle.Turtle()
startbutton.penup()
startbutton.speed(0)
startbutton.sety(300)
startbutton.setx(0)
startbutton.hideturtle()
startbutton.color("white")
startbutton.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 15, "normal"))

# Segments snake
segmentA = []
segmentB = []

# Movement Function
def move_player_a():
    if player_a.direction == "up":
        y = player_a.ycor() + 20
        player_a.sety(y)
    if player_a.direction == "down":
        y = player_a.ycor() - 20
        player_a.sety(y)
    if player_a.direction == "left":
        x = player_a.xcor() - 20
        player_a.setx(x)
    if player_a.direction == "right":
        x = player_a.xcor() + 20
        player_a.setx(x)


# Player B
def move_player_b():
    if player_b.direction == "up":
        y = player_b.ycor() + 20
        player_b.sety(y)
    if player_b.direction == "down":
        y = player_b.ycor() - 20
        player_b.sety(y)
    if player_b.direction == "left":
        x = player_b.xcor() - 20
        player_b.setx(x)
    if player_b.direction == "right":
        x = player_b.xcor() + 20
        player_b.setx(x)

def timeSleep():
    time.sleep(0.1)
    move_player_b()
    move_player_a()


# Key functions
def upA():
    if player_a.direction != "down":
        player_a.direction = "up"


def downA():
    if player_a.direction != "up":
        player_a.direction = "down"


def leftA():
    if player_a.direction != "right":
        player_a.direction = "left"


def rightA():
    if player_a.direction != "left":
        player_a.direction = "right"

def upB():
    if player_b.direction != "down":
        player_b.direction = "up"


def downB():
    if player_b.direction != "up":
        player_b.direction = "down"


def leftB():
    if player_b.direction != "right":
        player_b.direction = "left"


def rightB():
    if player_b.direction != "left":
        player_b.direction = "right"

def startButton():
    player_a.direction = "left"
    player_b.direction = "right"
    startbutton.clear()
    startbutton.goto(1000,1000)

def stop():
    player_a.goto(300, 0)
    player_b.goto(-300, 0)
    player_a.direction = "stop"
    player_b.direction = "stop"
    startbutton.clear()
    startbutton.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 15, "normal"))
    segmentA.clear()
    segmentB.clear()

def updateText():
    startbutton.clear()
    startbutton.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 15, "normal"))
# Key binding
wd.listen()
# Player A
wd.onkeypress(upA, "w")
wd.onkeypress(downA, "s")
wd.onkeypress(leftA, "a")
wd.onkeypress(rightA, "d")
# Player B
wd.onkeypress(upB, "Up")
wd.onkeypress(downB, "Down")
wd.onkeypress(leftB, "Left")
wd.onkeypress(rightB, "Right")
# Start Button
wd.onkeypress(startButton, "space")



# Main Game Loop
while True:
    wd.update()
    timeSleep()

    if player_a.xcor() == food.xcor()and player_a.ycor() == food.ycor():
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        food.goto(x,y)
        score_a += 1
        updateText()
        # Snake Body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color("grey")
        segmentA.append(new_segment)
    if player_b.xcor() == food.xcor()and player_b.ycor() == food.ycor():
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        food.goto(x,y)
        score_b += 1
        updateText()
        # Snake Body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color("grey")
        segmentB.append(new_segment)
    if player_a.xcor() == food1.xcor()and player_a.ycor() == food1.ycor():
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        food1.goto(x,y)
        score_a += 1
        updateText()
        # Snake Body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color("grey")
        segmentA.append(new_segment)
    if player_b.xcor() == food1.xcor()and player_b.ycor() == food1.ycor():
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        food1.goto(x,y)
        score_b += 1
        updateText()
        # Snake Body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color("grey")
        segmentB.append(new_segment)

    # Borders
    if player_a.xcor() >= 340:
        score_b = 0
        score_a = 0
        stop()

    if player_a.xcor() <= -340:
        score_b = 0
        score_a = 0
        stop()

    if player_a.ycor() >= 340:
        score_b = 0
        score_a = 0
        stop()

    if player_a.ycor() <= -340:
        score_b = 0
        score_a = 0
        stop()

    if player_b.xcor() >= 340:
        score_b = 0
        score_a = 0
        stop()
        segmentA.clear()
        segmentB.clear()

    if player_b.xcor() <= -340:
        score_b = 0
        score_a = 0
        stop()

    if player_b.ycor() >= 340:
        score_b = 0
        score_a = 0
        stop()

    if player_b.ycor() <= -340:
        score_b = 0
        score_a = 0
        stop()

    for index in range(len(segmentA)-1, 0, -1): #counts from end to first
        y = segmentA[index - 1].ycor()
        x = segmentA[index - 1].xcor()
        segmentA[index].goto(x, y)

    if len(segmentA) > 0: # Position first extra block, other blocks will be down above.
        x = player_a.xcor()
        y = player_a.ycor()
        if player_a.direction == "up":
            segmentA[0].goto(x, y-20)
        if player_a.direction == "down":
            segmentA[0].goto(x, y+20)
        if player_a.direction == "left":
            segmentA[0].goto(x+20, y)
        if player_a.direction == "right":
            segmentA[0].goto(x-20, y)

    for index in range(len(segmentB)-1, 0, -1): #counts from end to first
        y = segmentB[index - 1].ycor()
        x = segmentB[index - 1].xcor()
        segmentB[index].goto(x, y)

    if len(segmentB) > 0: # Position first extra block, other blocks will be down above.
        x = player_b.xcor()
        y = player_b.ycor()
        if player_b.direction == "up":
            segmentB[0].goto(x, y-20)
        if player_b.direction == "down":
            segmentB[0].goto(x, y+20)
        if player_b.direction == "left":
            segmentB[0].goto(x+20, y)
        if player_b.direction == "right":
            segmentB[0].goto(x-20, y)

