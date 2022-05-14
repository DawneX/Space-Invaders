# Space Invaders
import turtle
import os
import math
from random import random,randint,randrange,getrandbits
import winsound

# Set-up the screen
win = turtle.Screen()
win.bgcolor("black")
win.title("Space Invaders")
win.bgpic("space_invaders_background.gif")

# Register the shapes
win.register_shape("invader.gif")
win.register_shape("player.gif")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Create the Player Turtle
player = turtle.Turtle()
player.color("red")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
# Player  movement speed
player.speed = 0

# Choose the number of enemys
number_of_enemies = 5
# Create an empty list of enemies
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
    # Create enemies
    enemies.append(turtle.Turtle())

# Addding enemies to the enemies list
for enemy in enemies:
    enemy.color("orange")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = randint(-200,200)
    y = randint(100,250)
    enemy.setposition(x,y)

# Enemy speed
enemy_speed = 2

# Creating weapons for the player
bullet = turtle.Turtle()
bullet.color("green")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bullet_speed = 20

bullet_state = "ready"

# Set the Player score to 0
score = 0

# Draw the score on the screen
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
score_string = "Score : {}" .format(score)
score_pen.write(score_string,False, align='left', font=("Arial",14,"normal"))
score_pen.hideturtle()

# Moving player left and right
def move_player():
    x = player.xcor()
    x += player.speed
    if x > 280:
        x = 280
    if x < -280:
        x = -280
    player.setx(x)

def move_left():
    player.speed = -15

def move_right():
    player.speed = 15

# Bullet state
def fire_bullet():
    # Declare bulletstate as a global if it needs to be changed
    global bullet_state
    if bullet_state == "ready":
        winsound.PlaySound("laser.wav",winsound.SND_ASYNC)
        bullet_state = "fire"
         # Move the bullet just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1,t2):
    if t1.distance (t2) <20:
        return True
    else:
        return False
# Create key bindings
win.listen()
win.onkeypress(move_left,"Left")
win.onkeypress(move_right,"Right")
win.onkeypress(fire_bullet,"space")


# Main game loop:
while True:

    move_player()

    for enemy in enemies:
        # Moving the enemy 
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)
        
        # Moving the enemy back and down
        if enemy.xcor() > 280:
            #Moves all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 20
                e.sety(y)
            # Change enemy direction
            enemy_speed *= -1
            
        if enemy.xcor() < -280:
            # Moves all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 20
                e.sety(y)
            # Change enemy direction
            enemy_speed *= -1
        
        # Collision between bullet and the enemy
        if isCollision(bullet,enemy):
            winsound.PlaySound("explosion.wav",winsound.SND_ASYNC)
            # Reset the bullet
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.setposition(0,-400)
            # Reset the enemy
            x = randint(-200,200)
            y = randint(100,250)
            enemy.setposition(x,y)
            score += 1
            score_string = "Score : {}" .format(score)
            score_pen.clear()
            score_pen.write(score_string,False, align='left', font=("Arial",14,"normal"))

         # Collision between player and enemy
        if isCollision(player,enemy):
            winsound.PlaySound("explosion.wav",winsound.SND_ASYNC)
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    # Move the bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"