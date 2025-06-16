#Turtle Graphics Game
import turtle
import math
import random

#Set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor("mediumpurple")

# Draw border
mypen = turtle.Turtle()
mypen.pu()
mypen.setpos(-300,-300)
mypen.pd()
mypen.pensize(5)
mypen.pencolor('black')
mypen.speed(0)
for side in range(4):
        mypen.forward(600)
        mypen.left(90)
mypen.hideturtle()

#Create player turtle
player = turtle.Turtle()
player.color('darkviolet')
player.shape('turtle')
player.pencolor('aqua')
player.pensize(3)
player.penup()
player.speed(0)

# Create food
food = turtle.Turtle()
food.color('lightgreen')
food.shape('circle')
food.pu()
food.speed(0)
food.setpos(random.randint(-290, 290), random.randint(-290, 290))

#Set speed variable
speed = 1

# Define functions

def turn_right():
    if player.heading()!=0:
        player.setheading(0)

def turn_up():
    if player.heading()!=90:
        player.setheading(90)

def turn_left():
    if player.heading()!=180:
        player.setheading(180)

def turn_down():
    if player.heading()!=270:
        player.setheading(270)

def increase_speed():
    global speed
    speed += 1

def decrease_speed():
    global speed
    speed -= 1

def use_pen():
    #changes between up and down with the same button being clicked
    if player.isdown():
        player.penup()
    else:
        player.pd()

def isCollision(t1, t2):
       d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
       if d < 20:
           return True
       else:
           return False

# Set keyboard binding
turtle.listen()
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(turn_up, 'Up')
turtle.onkey(turn_down, 'Down')
turtle.onkey(increase_speed, 'a')
turtle.onkey(decrease_speed, 's')
turtle.onkey(use_pen, 'space')

while True:
    player.forward(speed)

    # Boundary Player Checking x coordinate
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)

    # Boundary Player Checking y coordinate
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)

    # Move food around
    food.forward(3)

    # Boundary Food Checking x coordinate
    if food.xcor() > 290 or food.xcor() < -290:
        food.right(180)

    # Boundary Food Checking y coordinate
    if food.ycor() > 290 or food.ycor() < -290:
        food.right(120)

# Collision checking
    if isCollision(player, food):
        food.setposition(random.randint(-290, 290), random.randint(-290, 290))
        food.right(random.randint(0,360))

#Part 7 
#More cabbage, more!
