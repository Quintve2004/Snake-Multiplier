import time
import turtle

# Window Setup
wd = turtle.Screen()
wd.setup(width=580, height=580)
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

# StartButton
startbutton = turtle.Turtle()
startbutton.penup()
startbutton.speed(0)
startbutton.hideturtle()
startbutton.color("white")
startbutton.write("Tap Spacebar To Begin", align="center", font=("Courier", 15, "normal"))

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
    player_a.direction = "up"


def downA():
    player_a.direction = "down"


def leftA():
    player_a.direction = "left"


def rightA():
    player_a.direction = "right"

def upB():
    player_b.direction = "up"


def downB():
    player_b.direction = "down"


def leftB():
    player_b.direction = "left"


def rightB():
    player_b.direction = "right"

def startButton():
    player_a.direction = "left"
    player_b.direction = "right"
    startbutton.clear()
    startbutton.goto(1000,1000)


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
