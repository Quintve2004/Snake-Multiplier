import time
import turtle
from random import randint


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
player_a.goto(20, 20)
player_a.color("yellow")
player_a.direction = "stop"

# Player B
player_b = turtle.Turtle()
player_b.penup()
player_b.speed(0)
player_b.shape("square")
player_b.goto(-20, -20)
player_b.color("blue")
player_b.direction = "stop"

# Food
food = turtle.Turtle()
food.penup()
food.speed(0)
food.shape("circle")
food.color("red")
food.goto(40, 40)

food1 = turtle.Turtle()
food1.penup()
food1.speed(0)
food1.shape("circle")
food1.color("red")
food1.goto(40, 40)

# StartButton
startbutton = turtle.Turtle()
startbutton.penup()
startbutton.speed(0)
startbutton.hideturtle()
startbutton.color("white")
startbutton.write("Tap Spacebar To Begin", align="center", font=("Courier", 15, "normal"))

# Segments snake
segmentA = []
segmentB = []

# Movement Function
def move_player_a():
    if player_a.direction == "up":
        y = player_a.ycor() + 20
        player_a.sety(y)
        time.sleep(0.05)
    if player_a.direction == "down":
        y = player_a.ycor() - 20
        player_a.sety(y)
        time.sleep(0.05)
    if player_a.direction == "left":
        x = player_a.xcor() - 20
        player_a.setx(x)
        time.sleep(0.05)
    if player_a.direction == "right":
        x = player_a.xcor() + 20
        player_a.setx(x)
        time.sleep(0.05)


# Player B
def move_player_b():
    if player_b.direction == "up":
        y = player_b.ycor() + 20
        player_b.sety(y)
        time.sleep(0.05)
    if player_b.direction == "down":
        y = player_b.ycor() - 20
        player_b.sety(y)
        time.sleep(0.05)
    if player_b.direction == "left":
        x = player_b.xcor() - 20
        player_b.setx(x)
        time.sleep(0.05)
    if player_b.direction == "right":
        x = player_b.xcor() + 20
        player_b.setx(x)
        time.sleep(0.05)


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
    player_a.goto(20, 20)
    player_b.goto(-20, -20)
    player_a.direction = "stop"
    player_b.direction = "stop"
    startbutton.write("Tap Spacebar To Begin", align="center", font=("Courier", 15, "normal"))

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
    move_player_a()
    move_player_b()

    # Borders
    if player_a.xcor() >= 320:
        stop()

    if player_a.xcor() <= -320:
        stop()

    if player_a.ycor() >= 320:
        stop()

    if player_a.ycor() <= -320:
        stop()

    if player_b.xcor() >= 320:
        stop()

    if player_b.xcor() <= -320:
        stop()

    if player_b.ycor() >= 320:
        stop()

    if player_b.ycor() <= -320:
        stop()

    if food.xcor() == player_a.xcor and food.ycor() == player_a.ycor():
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        print("1")
        food.goto(x, y)


