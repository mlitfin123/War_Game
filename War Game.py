import turtle
import os
import math
import random
import time

turtle.setup(800, 620)
wn = turtle.Screen()
wn.bgcolor("brown")
game_start_pen = turtle.Turtle()
game_start_pen.speed(0)
game_start_pen.color("black")
game_start_pen.penup()
game_start_pen.setposition(-80, 0)
game_start_string = "Begin Game!"
game_start_pen.write(game_start_string, False, align="left", font=("Arial", "26", "normal"))
game_start_pen.hideturtle()
wn.delay()
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("green")
#draw top border
border_pen.penup()
border_pen.setposition(-350, 260)
border_pen.pendown()
border_pen.pensize(5)
for side in range(4):
    border_pen.fd(900)
    border_pen.lt(90)
    border_pen.hideturtle()
#draw bottom border
border_pen.penup()
border_pen.setposition(-350, -250)
border_pen.pendown()
border_pen.pensize(5)
for side in range(4):
    border_pen.fd(900)
    border_pen.lt(90)
    border_pen.hideturtle()

#Set the score
score = 0

#Set the level
level = 1

#Set Player Lives
player_lives = 3

#Draw player lives
player_lives_pen = turtle.Turtle()
player_lives_pen.speed(0)
player_lives_pen.color("white")
player_lives_pen.penup()
player_lives_pen.setposition(-60, 280)
player_livesstring = "Lives: %s" %player_lives
player_lives_pen.write(player_livesstring, False, align="left", font=("Arial", "14", "normal"))
player_lives_pen.hideturtle()

#Draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
score_pen.hideturtle()

#Draw level
level_pen = turtle.Turtle()
level_pen.speed(0)
level_pen.color("white")
level_pen.penup()
level_pen.setposition(-170, 280)
levelstring = "Level: %s" %level
level_pen.write(levelstring, False, align="left", font=("Arial", "14", "normal"))
level_pen.hideturtle()

#Draw controls
controls_pen = turtle.Turtle()
controls_pen.speed(0)
controls_pen.color("black")
controls_pen.penup()
controls_pen.setposition(-330, -280)
controls_string = "Controls::   Move Player Up: Up Arrow-----Move Player Down: Down Arrow-----Shoot: Space"
controls_pen.write(controls_string, False, align="left", font=("Arial", "11", "normal"))
controls_pen.hideturtle()

#Register the images
turtle.register_shape("Soldier-shoot.gif")
turtle.register_shape("shooting-machine-gun(1).gif")
turtle.register_shape("sherman_tank.gif")
turtle.register_shape("gun-shot-clipart-animated.gif")
turtle.register_shape("army-clipart-animated-21.gif")
turtle.register_shape("shooter.gif")
        
#create player
player = turtle.Turtle()
player.color("blue")
player.shape("shooting-machine-gun(1).gif")
player.penup()
player.speed(0)
player.setposition(-300, 0)
playerspeed = 30

#create ally list

number_of_allies = 0
allies = []
for i in range(number_of_allies):
    allies.append(turtle.Turtle())
    
#create enemies list
number_of_enemies = 1
enemies = []
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

number_of_soldiers = 0
soldiers = []
for i in range(number_of_soldiers):
    soldiers.append(turtle.Turtle())

number_of_tanks = 0
tanks = []
for i in range(number_of_tanks):
    tanks.append(turtle.Turtle())

#Double
number_of_allies1 = 0
allies1 = []
for i in range(number_of_allies1):
    allies1.append(turtle.Turtle())
    
number_of_enemies1 = 0
enemies1 = []
for i in range(number_of_enemies1):
    enemies1.append(turtle.Turtle())

number_of_soldiers1 = 0
soldiers1 = []
for i in range(number_of_soldiers1):
    soldiers1.append(turtle.Turtle())

number_of_tanks1 = 0
tanks1 = []
for i in range(number_of_tanks1):
    tanks1.append(turtle.Turtle())

# Number of Bullets

number_of_bullets = 1
bullets = []
for i in range(number_of_bullets):
    bullets.append(turtle.Turtle())
    
number_of_allybullets = 1
allybullets = []
for i in range(number_of_allybullets):
    allybullets.append(turtle.Turtle())
    
number_of_enemybullets = 1
enemybullets = []
for i in range(number_of_enemybullets):
    enemybullets.append(turtle.Turtle())

number_of_soldierbullets = 1
soldierbullets = []
for i in range(number_of_soldierbullets):
    soldierbullets.append(turtle.Turtle())

number_of_tankbullets = 1
tankbullets = []
for i in range(number_of_tankbullets):
    tankbullets.append(turtle.Turtle())

#Double
number_of_bullets1 = 1
bullets1 = []
for i in range(number_of_bullets1):
    bullets1.append(turtle.Turtle())
    
number_of_allybullets1 = 1
allybullets1 = []
for i in range(number_of_allybullets1):
    allybullets1.append(turtle.Turtle())
    
number_of_enemybullets1 = 1
enemybullets1 = []
for i in range(number_of_enemybullets1):
    enemybullets1.append(turtle.Turtle())

number_of_soldierbullets1 = 1
soldierbullets1 = []
for i in range(number_of_soldierbullets1):
    soldierbullets1.append(turtle.Turtle())

number_of_tankbullets1 = 1
tankbullets1 = []
for i in range(number_of_tankbullets1):
    tankbullets1.append(turtle.Turtle())
    
#create ally    
for ally in allies:
    ally.color("blue")
    ally.shape("shooter.gif")
    ally.penup()
    ally.speed(0)
    ally.setposition(-300, 100)

allyspeed = 10
    
for enemy in enemies:
    enemy.color("red")
    enemy.shape("gun-shot-clipart-animated.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(200, 300)
    y = random.randint(-250, 260)
    enemy.setposition(x, y)

enemyspeed = 3

for soldier in soldiers:
    soldier.color("red")
    soldier.shape("Soldier-shoot.gif")
    soldier.penup()
    soldier.speed(0)
    x = random.randint(200, 300)
    y = random.randint(-250, 260)
    soldier.setposition(x, y)

soldierspeed = 2

for tank in tanks:
    tank.color("red")
    tank.shape("sherman_tank.gif")
    tank.penup()
    tank.speed(0)
    x = random.randint(200, 300)
    y = random.randint(-250, 260)
    tank.setposition(x, y)

tankspeed = 5

#Double
for ally1 in allies1:
    ally1.color("blue")
    ally1.shape("shooter.gif")
    ally1.penup()
    ally1.speed(0)
    ally1.setposition(-300, 100)

ally1speed = 10
    
for enemy1 in enemies1:
    enemy1.color("red")
    enemy1.shape("gun-shot-clipart-animated.gif")
    enemy1.penup()
    enemy1.speed(0)
    x = random.randint(200, 300)
    y = random.randint(-250, 260)
    enemy1.setposition(x, y)

enemy1speed = 3

for soldier1 in soldiers1:
    soldier1.color("red")
    soldier1.shape("Soldier-shoot.gif")
    soldier1.penup()
    soldier1.speed(0)
    x = random.randint(200, 300)
    y = random.randint(-250, 260)
    soldier1.setposition(x, y)

soldier1speed = 2

for tank1 in tanks1:
    tank1.color("red")
    tank1.shape("sherman_tank.gif")
    tank1.penup()
    tank1.speed(0)
    x = random.randint(200, 300)
    y = random.randint(-250, 260)
    tank1.setposition(x, y)

tank1speed = 5

#create weapons
for bullet in bullets:
    bullet.color("black")
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(0)
    bullet.shapesize(0.5, 0.5)
    bullet.hideturtle()

bulletspeed = 50

bulletstate = "ready"

for allybullet in allybullets:
    allybullet.color("black")
    allybullet.penup()
    allybullet.speed(0)
    allybullet.setheading(0)
    allybullet.shapesize(0.5, 0.5)
    allybullet.hideturtle()

allybulletspeed = 50

allybulletstate = "ready"

for enemybullet in enemybullets:
    enemybullet.color("gray")
    enemybullet.penup()
    enemybullet.speed(0)
    enemybullet.setheading(180)
    enemybullet.shapesize(0.7, 0.7)
    enemybullet.hideturtle()

enemybulletspeed = 10

enemybulletstate = "ready"

for soldierbullet in soldierbullets:
    soldierbullet.color("gray")
    soldierbullet.penup()
    soldierbullet.speed(0)
    soldierbullet.setheading(180)
    soldierbullet.shapesize(0.4, 0.4)
    soldierbullet.hideturtle()

soldierbulletspeed = 25

soldierbulletstate = "ready"

for tankbullet in tankbullets:
    tankbullet.color("gray")
    tankbullet.penup()
    tankbullet.speed(0)
    tankbullet.setheading(180)
    tankbullet.shapesize(1, 1)
    tankbullet.hideturtle()

tankbulletspeed = 30

tankbulletstate = "ready"

#Double
for bullet1 in bullets1:
    bullet1.color("black")
    bullet1.penup()
    bullet1.speed(0)
    bullet1.setheading(0)
    bullet1.shapesize(0.5, 0.5)
    bullet1.hideturtle()

bullet1speed = 50

bullet1state = "ready"

for allybullet1 in allybullets1:
    allybullet1.color("black")
    allybullet1.penup()
    allybullet1.speed(0)
    allybullet1.setheading(0)
    allybullet1.shapesize(0.5, 0.5)
    allybullet1.hideturtle()

allybullet1speed = 50

allybullet1state = "ready"

for enemybullet1 in enemybullets1:
    enemybullet1.color("gray")
    enemybullet1.penup()
    enemybullet1.speed(0)
    enemybullet1.setheading(180)
    enemybullet1.shapesize(0.7, 0.7)
    enemybullet1.hideturtle()

enemybullet1speed = 10

enemybullet1state = "ready"

for soldierbullet1 in soldierbullets1:
    soldierbullet1.color("gray")
    soldierbullet1.penup()
    soldierbullet1.speed(0)
    soldierbullet1.setheading(180)
    soldierbullet1.shapesize(0.4, 0.4)
    soldierbullet1.hideturtle()

soldierbullet1speed = 25

soldierbullet1state = "ready"

for tankbullet1 in tankbullets1:
    tankbullet1.color("gray")
    tankbullet1.penup()
    tankbullet1.speed(0)
    tankbullet1.setheading(180)
    tankbullet1.shapesize(1, 1)
    tankbullet1.hideturtle()

tankbullet1speed = 30

tankbullet1state = "ready"

def next_level():
    global level_up

def another_level():
    global level_up
    
def move_up():
    y = player.ycor()
    y -= playerspeed
    if y < -260:
        y = - 260
    player.sety(y)
    
def move_down():
    y = player.ycor()
    y += playerspeed
    if y > 260:
        y = 260
    player.sety(y)    

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bullet.goto(-1000, 1000)
        bulletstate = "fire"
        x = player.xcor() + 10
        y = player.ycor()
        bullet.setposition(x, y)
        bullet.showturtle()

def fire_allybullet():
    global allybulletstate
    if allybulletstate == "ready":
        allybullet.goto(-1000, 1000)
        allybulletstate = "fire"
        x = ally.xcor() + 10
        y = ally.ycor()
        allybullet.setposition(x, y)
        allybullet.showturtle()

def fire_enemybullet():
    global enemybulletstate
    if enemybulletstate == "ready":
        enemybullet.goto(-1000, 1000)
        enemybulletstate = "fire"
        x = enemy.xcor() - 10
        y = enemy.ycor()
        enemybullet.setposition(x, y)
        enemybullet.showturtle()

def fire_soldierbullet():
    global soldierbulletstate
    if soldierbulletstate == "ready":
        soldierbullet.goto(-1000, 1000)
        soldierbulletstate = "fire"
        x = soldier.xcor()
        y = soldier.ycor() +15
        soldierbullet.setposition(x, y)
        soldierbullet.showturtle()

def fire_tankbullet():
    global tankbulletstate
    if tankbulletstate == "ready":
        tankbullet.goto(-1000, 1000)
        tankbulletstate = "fire"
        x = tank.xcor() - 20
        y = tank.ycor()
        tankbullet.setposition(x, y)
        tankbullet.showturtle()
#Double
def fire_bullet1():
    global bullet1state
    if bullet1state == "ready":
        bullet1.goto(-1000, 1000)
        bullet1state = "fire"
        x = player.xcor() + 10
        y = player.ycor()
        bullet1.setposition(x, y)
        bullet1.showturtle()

def fire_allybullet1():
    global allybullet1state
    if allybullet1state == "ready":
        allybullet1.goto(-1000, 1000)
        allybullet1state = "fire"
        x = ally1.xcor() + 10
        y = ally1.ycor()
        allybullet1.setposition(x, y)
        allybullet1.showturtle()

def fire_enemybullet1():
    global enemybullet1state
    if enemybullet1state == "ready":
        enemybullet1.goto(-1000, 1000)
        enemybullet1state = "fire"
        x = enemy1.xcor() - 10
        y = enemy1.ycor()
        enemybullet1.setposition(x, y)
        enemybullet1.showturtle()

def fire_soldierbullet1():
    global soldierbullet1state
    if soldierbullet1state == "ready":
        soldierbullet1.goto(-1000, 1000)
        soldierbullet1state = "fire"
        x = soldier1.xcor()
        y = soldier1.ycor() +15
        soldierbullet1.setposition(x, y)
        soldierbullet1.showturtle()

def fire_tankbullet1():
    global tankbullet1state
    if tankbullet1state == "ready":
        tankbullet1.goto(-1000, 1000)
        tankbullet1state = "fire"
        x = tank1.xcor() - 20
        y = tank1.ycor()
        tankbullet1.setposition(x, y)
        tankbullet1.showturtle()
        
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 30:
        return True
    else:
        return False
        
turtle.listen()
turtle.onkey(move_up, "Down")
turtle.onkey(move_down, "Up")
turtle.onkey(fire_bullet, "space")
turtle.onkey(fire_bullet1, "a")

game_start_pen.clear()

while True:

    turtle.update()
    time.sleep(0.10)
    
    for ally in allies:
        y = ally.ycor()
        y += allyspeed
        ally.sety(y)

        #turn at the border
        if ally.ycor() > 250:
            ally.sety(250)
            y = ally.ycor()
            allyspeed *= -1

        #turn at the border
        if ally.ycor() < -250:
            ally.sety(-250)
            y = ally.ycor()
            allyspeed *= -1

        if isCollision(enemybullet, ally):
            enemybullet.hideturtle()
            enemybulletstate = "ready"
            enemybullet.setposition(1100, 0)
            ally.hideturtle()
            ally.setposition(-1100, 0)
            allies.remove(ally)
        elif isCollision(soldierbullet, ally):
            soldierbullet.hideturtle()
            soldierbulletstate = "ready"
            soldierbullet.setposition(1100, 0)
            ally.hideturtle()
            ally.setposition(-1100, 0)
            allies.remove(ally)
        elif isCollision(tankbullet, ally):
            tankbullet.hideturtle()
            tankbulletstate = "ready"
            tankbullet.setposition(1100, 0)
            ally.hideturtle()
            ally.setposition(-1100, 0)
            allies.remove(ally)
        elif isCollision(enemybullet1, ally):
            enemybullet1.hideturtle()
            enemybullet1state = "ready"
            enemybullet1.setposition(1100, 0)
            ally.hideturtle()
            ally.setposition(-1100, 0)
            allies.remove(ally)
        elif isCollision(soldierbullet1, ally):
            soldierbullet1.hideturtle()
            soldierbullet1state = "ready"
            soldierbullet1.setposition(1100, 0)
            ally.hideturtle()
            ally.setposition(-1100, 0)
            allies.remove(ally)
        elif isCollision(tankbullet1, ally):
            tankbullet1.hideturtle()
            tankbullet1state = "ready"
            tankbullet1.setposition(1100, 0)
            ally.hideturtle()
            ally.setposition(-1100, 0)
            allies.remove(ally)

#Double
    for ally1 in allies1:
        y = ally1.ycor()
        y += ally1speed
        ally1.sety(y)

        #turn at the border
        if ally1.ycor() > 250:
            ally1.sety(250)
            y = ally1.ycor()
            ally1speed *= -1

        #turn at the border
        if ally1.ycor() < -250:
            ally1.sety(-250)
            y = ally1.ycor()
            ally1speed *= -1

        if isCollision(enemybullet, ally1):
            enemybullet.hideturtle()
            enemybulletstate = "ready"
            enemybullet.setposition(1100, 0)
            ally1.hideturtle()
            ally1.setposition(-1100, 0)
            allies1.remove(ally1)
        elif isCollision(soldierbullet, ally1):
            soldierbullet.hideturtle()
            soldierbulletstate = "ready"
            soldierbullet.setposition(1100, 0)
            ally1.hideturtle()
            ally1.setposition(-1100, 0)
            allies1.remove(ally1)
        elif isCollision(tankbullet, ally1):
            tankbullet.hideturtle()
            tankbulletstate = "ready"
            tankbullet.setposition(1100, 0)
            ally1.hideturtle()
            ally1.setposition(-1100, 0)
            allies1.remove(ally1)
        elif isCollision(enemybullet1, ally1):
            enemybullet1.hideturtle()
            enemybullet1state = "ready"
            enemybullet1.setposition(1100, 0)
            ally1.hideturtle()
            ally1.setposition(-1100, 0)
            allies1.remove(ally1)
        elif isCollision(soldierbullet1, ally1):
            soldierbullet1.hideturtle()
            soldierbullet1state = "ready"
            soldierbullet1.setposition(1100, 0)
            ally1.hideturtle()
            ally1.setposition(-1100, 0)
            allies1.remove(ally1)
        elif isCollision(tankbullet1, ally1):
            tankbullet1.hideturtle()
            tankbullet1state = "ready"
            tankbullet1.setposition(1100, 0)
            ally1.hideturtle()
            ally1.setposition(-1100, 0)
            allies1.remove(ally1)
            
    for enemy in enemies:
        y = enemy.ycor()
        y += enemyspeed
        enemy.sety(y)
        
        #turn at the border
        if enemy.ycor() > 250:
            enemy.sety(250)
            y = enemy.ycor()
            enemyspeed *= -1

        #turn at the border
        if enemy.ycor() < -250:
            enemy.sety(-250)
            y = enemy.ycor()
            enemyspeed *= -1

        #destroy the enemy    
        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(1100, 0)
            enemy.hideturtle()
            enemy.setposition(-1100, 0)
            enemies.remove(enemy)
            score += 5
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
        elif isCollision(allybullet, enemy):
            allybullet.hideturtle()
            allybulletstate = "ready"
            allybullet.setposition(1100, 0)
            enemy.hideturtle()
            enemy.setposition(-1100, 0)
            enemies.remove(enemy)
            score += 2
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))          
        elif isCollision(bullet1, enemy):
            bullet1.hideturtle()
            bullet1state = "ready"
            bullet1.setposition(1100, 0)
            enemy.hideturtle()
            enemy.setposition(-1100, 0)
            enemies.remove(enemy)
            score += 5
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
        elif isCollision(allybullet1, enemy):
            allybullet1.hideturtle()
            allybullet1state = "ready"
            allybullet1.setposition(1100, 0)
            enemy.hideturtle()
            enemy.setposition(-1100, 0)
            enemies.remove(enemy)
            score += 2
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
            
#Double
    for enemy1 in enemies1:
        y = enemy1.ycor()
        y += enemy1speed
        enemy1.sety(y)
        
        #turn at the border
        if enemy1.ycor() > 250:
            enemy1.sety(250)
            y = enemy1.ycor()
            enemy1speed *= -1

        #turn at the border
        if enemy1.ycor() < -250:
            enemy1.sety(-250)
            y = enemy1.ycor()
            enemy1speed *= -1

        #destroy the enemy    
        if isCollision(bullet, enemy1):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(1100, 0)
            enemy1.hideturtle()
            enemy1.setposition(-1100, 0)
            enemies1.remove(enemy1)
            score += 5
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
        elif isCollision(allybullet, enemy1):
            allybullet.hideturtle()
            allybulletstate = "ready"
            allybullet.setposition(1100, 0)
            enemy1.hideturtle()
            enemy1.setposition(-1100, 0)
            enemies1.remove(enemy1)
            score += 2
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
        elif isCollision(bullet1, enemy1):
            bullet1.hideturtle()
            bullet1state = "ready"
            bullet1.setposition(1100, 0)
            enemy1.hideturtle()
            enemy1.setposition(-1100, 0)
            enemies1.remove(enemy1)
            score += 5
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
        elif isCollision(allybullet1, enemy1):
            allybullet1.hideturtle()
            allybullet1state = "ready"
            allybullet1.setposition(1100, 0)
            enemy1.hideturtle()
            enemy1.setposition(-1100, 0)
            enemies1.remove(enemy1)
            score += 2
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
            
    for soldier in soldiers:
        y = soldier.ycor()
        y += soldierspeed
        soldier.sety(y)

        #turn at the border
        if soldier.ycor() > 250:
            soldier.sety(250)
            y = soldier.ycor()
            soldierspeed *= -1

        #turn at the border
        if soldier.ycor() < -250:
            soldier.sety(-250)
            y = soldier.ycor()
            soldierspeed *= -1

        #destroy the soldier    
        if isCollision(bullet, soldier):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(1100, 0)
            soldier.hideturtle()
            soldier.setposition(-1100, 0)
            soldiers.remove(soldier)
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
        elif isCollision(allybullet, soldier):
            allybullet.hideturtle()
            allybulletstate = "ready"
            allybullet.setposition(1100, 0)
            soldier.hideturtle()
            soldier.setposition(-1100, 0)
            soldiers.remove(soldier)
            score += 5
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
        elif isCollision(bullet1, soldier):
            bullet1.hideturtle()
            bullet1state = "ready"
            bullet1.setposition(1100, 0)
            soldier.hideturtle()
            soldier.setposition(-1100, 0)
            soldiers.remove(soldier)
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
        elif isCollision(allybullet1, soldier):
            allybullet1.hideturtle()
            allybullet1state = "ready"
            allybullet1.setposition(1100, 0)
            soldier.hideturtle()
            soldier.setposition(-1100, 0)
            soldiers.remove(soldier)
            score += 5
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))    
#Double

    for soldier1 in soldiers1:
        y = soldier1.ycor()
        y += soldier1speed
        soldier1.sety(y)
        
        if soldier1.ycor() > 250:
            soldier1.sety(250)
            y = soldier1.ycor()
            soldier1speed *= -1

        #turn at the border
        if soldier1.ycor() < -250:
            soldier1.sety(-250)
            y = soldier1.ycor()
            soldier1speed *= -1

        #destroy the soldier    
        if isCollision(bullet, soldier1):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(1100, 0)
            soldier1.hideturtle()
            soldier1.setposition(-1100, 0)
            soldiers1.remove(soldier1)
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
        elif isCollision(allybullet, soldier1):
            allybullet.hideturtle()
            allybulletstate = "ready"
            allybullet.setposition(1100, 0)
            soldier1.hideturtle()
            soldier1.setposition(-1100, 0)
            soldiers1.remove(soldier1)
            score += 5
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
        elif isCollision(bullet1, soldier1):
            bullet1.hideturtle()
            bullet1state = "ready"
            bullet1.setposition(1100, 0)
            soldier1.hideturtle()
            soldier1.setposition(-1100, 0)
            soldiers1.remove(soldier1)
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
        elif isCollision(allybullet1, soldier1):
            allybullet1.hideturtle()
            allybullet1state = "ready"
            allybullet1.setposition(1100, 0)
            soldier1.hideturtle()
            soldier1.setposition(-1100, 0)
            soldiers1.remove(soldier1)
            score += 5
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
            
            
    for tank in tanks:
        y = tank.ycor()
        y += tankspeed
        tank.sety(y)

        #turn at the border
        if tank.ycor() > 250:
            tank.sety(250)
            y = tank.ycor()
            tankspeed *= -1

        #turn at the border
        if tank.ycor() < -250:
            tank.sety(-250)
            y = tank.ycor()
            tankspeed *= -1

        #destroy the tank    
        if isCollision(bullet, tank):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(1100, 0)
            tank.hideturtle()
            tank.setposition(-1100, 0)
            tanks.remove(tank)
            score += 15
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
        elif isCollision(allybullet, tank):
            allybullet.hideturtle()
            allybulletstate = "ready"
            allybullet.setposition(1100, 0)
            tank.hideturtle()
            tank.setposition(-1100, 0)
            tanks.remove(tank)
            score += 8
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
        if isCollision(bullet1, tank):
            bullet1.hideturtle()
            bullet1state = "ready"
            bullet1.setposition(1100, 0)
            tank.hideturtle()
            tank.setposition(-1100, 0)
            tanks.remove(tank)
            score += 15
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
        elif isCollision(allybullet1, tank):
            allybullet1.hideturtle()
            allybullet1state = "ready"
            allybullet1.setposition(1100, 0)
            tank.hideturtle()
            tank.setposition(-1100, 0)
            tanks.remove(tank)
            score += 8
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
#Double
    for tank1 in tanks1:
        y = tank1.ycor()
        y += tank1speed
        tank1.sety(y)
        
        if tank1.ycor() > 250:
            tank1.sety(250)
            y = tank1.ycor()
            tank1speed *= -1

        #turn at the border
        if tank1.ycor() < -250:
            tank1.sety(-250)
            y = tank1.ycor()
            tank1speed *= -1

        #destroy the tank
        if isCollision(bullet, tank1):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(1100, 0)
            tank1.hideturtle()
            tank1.setposition(-1100, 0)
            tanks1.remove(tank1)
            score += 15
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
        elif isCollision(allybullet, tank1):
            allybullet.hideturtle()
            allybulletstate = "ready"
            allybullet.setposition(1100, 0)
            tank1.hideturtle()
            tank1.setposition(-1100, 0)
            tanks1.remove(tank1)
            score += 8
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
        if isCollision(bullet1, tank1):
            bullet1.hideturtle()
            bullet1state = "ready"
            bullet1.setposition(1100, 0)
            tank1.hideturtle()
            tank1.setposition(-1100, 0)
            tanks1.remove(tank1)
            score += 15
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
        elif isCollision(allybullet1, tank1):
            allybullet1.hideturtle()
            allybullet1state = "ready"
            allybullet1.setposition(1100, 0)
            tank1.hideturtle()
            tank1.setposition(-1100, 0)
            tanks1.remove(tank1)
            score += 8
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
            

    #destroy the player
    if isCollision(enemybullet, player):
        player.hideturtle()
        enemybullet.hideturtle()
        enemybulletstate = "ready"
        enemybullet.setposition(1100, 0)
        player_lives -= 1
        player_livesstring = "Lives: %s" %player_lives
        player_lives_pen.clear()
        player_lives_pen.write(player_livesstring, False, align="left", font=("Arial", "14", "normal"))
        turtle.delay(20)
        player.showturtle()
    elif isCollision(soldierbullet, player):
        player.hideturtle()
        soldierbullet.hideturtle()
        soldierbulletstate = "ready"
        soldierbullet.setposition(1100, 0)
        player_lives -= 1
        player_livesstring = "Lives: %s" %player_lives
        player_lives_pen.clear()
        player_lives_pen.write(player_livesstring, False, align="left", font=("Arial", "14", "normal"))
        turtle.delay(20)
        player.showturtle()
    elif isCollision(tankbullet, player):
        player.hideturtle()
        tankbullet.hideturtle()
        tankbulletstate = "ready"
        tankbullet.setposition(1100, 0)
        player_lives -= 1
        player_livesstring = "Lives: %s" %player_lives
        player_lives_pen.clear()
        player_lives_pen.write(player_livesstring, False, align="left", font=("Arial", "14", "normal"))
        turtle.delay(20)
        player.showturtle()
    elif isCollision(enemybullet1, player):
        player.hideturtle()
        enemybullet1.hideturtle()
        enemybullet1state = "ready"
        enemybullet1.setposition(1100, 0)
        player_lives -= 1
        player_livesstring = "Lives: %s" %player_lives
        player_lives_pen.clear()
        player_lives_pen.write(player_livesstring, False, align="left", font=("Arial", "14", "normal"))
        turtle.delay(20)
        player.showturtle()
    elif isCollision(soldierbullet1, player):
        player.hideturtle()
        soldierbullet1.hideturtle()
        soldierbullet1state = "ready"
        soldierbullet1.setposition(1100, 0)
        player_lives -= 1
        player_livesstring = "Lives: %s" %player_lives
        player_lives_pen.clear()
        player_lives_pen.write(player_livesstring, False, align="left", font=("Arial", "14", "normal"))
        turtle.delay(20)
        player.showturtle()
    elif isCollision(tankbullet1, player):
        player.hideturtle()
        tankbullet1.hideturtle()
        tankbullet1state = "ready"
        tankbullet1.setposition(1100, 0)
        player_lives -= 1
        player_livesstring = "Lives: %s" %player_lives
        player_lives_pen.clear()
        player_lives_pen.write(player_livesstring, False, align="left", font=("Arial", "14", "normal"))
        turtle.delay(20)
        player.showturtle()
    elif player_lives <= 0:
        player.hideturtle()
        scoretable = open("war_games_high_scores.txt", "w")
        scoretable.write(str(score))
        scoretable.close()
        wn.clear()
        game_over_pen = turtle.Turtle()
        game_over_pen.speed(0)
        game_over_pen.color("black")
        game_over_pen.penup()
        game_over_pen.setposition(-80, 0)
        game_over_string = "Game Over"
        game_over_pen.write(game_over_string, False, align="left", font=("Arial", "26", "normal"))
        game_over_pen.hideturtle()
        print ("Game Over")
        break

    if enemies + soldiers + tanks + enemies1 + soldiers1 + tanks1 == []:
        level += 1
        levelstring = "Level: %s" %level
        level_pen.clear()
        level_pen.write(levelstring, False, align="left", font=("Arial", "14", "normal"))

    if level == 2 or level == 4 or level == 6 or level == 8 or level == 10 or level == 12 or level == 14 or level == 16 or level == 18 or level == 20:
        add_ally = True
    else:
        add_ally = False

    if level == 3 or level == 5 or level == 7 or level == 9 or level == 11 or level == 13 or level == 15 or level == 17 or level == 19 or level == 21:
        add_ally1 = True
    else:
        add_ally1 = False
        
    if add_ally == True and enemies + soldiers + tanks + enemies1 + soldiers1 + tanks1 == []:
        number_of_allies += 1
        for i in range(number_of_allies):
            allies.append(turtle.Turtle())
        for ally in allies:
            ally.color("blue")
            ally.shape("shooter.gif")
            ally.penup()
            ally.speed(0)
            x = -300
            y = random.randint(-250, 260)
            ally.setposition(x, y)
            y = ally.ycor()
            y += allyspeed
            ally.sety(y)
        add_ally = False

    if add_ally1 == True and enemies + soldiers + tanks + enemies1 + soldiers1 + tanks1 == []:
        number_of_allies1 += 1
        for i in range(number_of_allies1):
            allies1.append(turtle.Turtle())
        for ally1 in allies1:
            ally1.color("blue")
            ally1.shape("shooter.gif")
            ally1.penup()
            ally1.speed(0)
            x = -300
            y = random.randint(-250, 260)
            ally1.setposition(x, y)
            y = ally1.ycor()
            y += ally1speed
            ally1.sety(y)
        add_ally1 = False
        
    if enemies + soldiers + tanks + enemies1 + soldiers1 + tanks1 == [] and level < 9:
        next_level = True
        turtle.delay(10)
        number_of_enemies = level - 1
        for i in range(number_of_enemies):
            enemies.append(turtle.Turtle())
        for enemy in enemies:
            enemy.color("red")
            enemy.shape("gun-shot-clipart-animated.gif")
            enemy.penup()
            enemy.speed(0)
            x = random.randint(200, 300)
            y = random.randint(-250, 260)
            enemy.setposition(x, y)
            y = enemy.ycor()
            y += enemyspeed
            enemy.sety(y)
        number_of_enemies1 = level - 3
        for i in range(number_of_enemies1):
            enemies1.append(turtle.Turtle())
        for enemy1 in enemies1:
            enemy1.color("red")
            enemy1.shape("gun-shot-clipart-animated.gif")
            enemy1.penup()
            enemy1.speed(0)
            x = random.randint(200, 300)
            y = random.randint(-250, 260)
            enemy1.setposition(x, y)
            y = enemy1.ycor()
            y += enemy1speed
            enemy1.sety(y)
        enemybulletspeed = level * 5
        enemybullet1speed = level * 5
    elif enemies + soldiers + tanks + enemies1 + soldiers1 + tanks1 == [] and level >= 9:
        next_level = True
        number_of_enemies = 5
        turtle.delay(10)
        for i in range(number_of_enemies):
            enemies.append(turtle.Turtle())
        for enemy in enemies:
            enemy.color("red")
            enemy.shape("gun-shot-clipart-animated.gif")
            enemy.penup()
            enemy.speed(0)
            x = random.randint(200, 300)
            y = random.randint(-250, 260)
            enemy.setposition(x, y)
            y = enemy.ycor()
            y += enemyspeed
            enemy.sety(y)
        number_of_enemies1 = 5
        for i in range(number_of_enemies1):
            enemies1.append(turtle.Turtle())
        for enemy1 in enemies1:
            enemy1.color("red")
            enemy1.shape("gun-shot-clipart-animated.gif")
            enemy1.penup()
            enemy1.speed(0)
            x = random.randint(200, 300)
            y = random.randint(-250, 260)
            enemy1.setposition(x, y)
            y = enemy1.ycor()
            y += enemy1speed
            enemy1.sety(y)
        enemybulletspeed = level * 5
        enemybullet1speed = level * 5

    if next_level == True and level > 3 and level < 9:
        another_level = True
        turtle.delay(10)
        number_of_soldiers = level - 2
        for i in range(number_of_soldiers):
            soldiers.append(turtle.Turtle())
        for soldier in soldiers:
            soldier.color("red")
            soldier.shape("Soldier-shoot.gif")
            soldier.penup()
            soldier.speed(0)
            x = random.randint(200, 300)
            y = random.randint(-250, 260)
            soldier.setposition(x, y)
            y = soldier.ycor()
            y += soldierspeed
            soldier.sety(y)
        number_of_soldiers1 = level - 3
        for i in range(number_of_soldiers1):
            soldiers1.append(turtle.Turtle())
        for soldier1 in soldiers1:
            soldier1.color("red")
            soldier1.shape("Soldier-shoot.gif")
            soldier1.penup()
            soldier1.speed(0)
            x = random.randint(200, 300)
            y = random.randint(-250, 260)
            soldier1.setposition(x, y)
            y = soldier1.ycor()
            y += soldier1speed
            soldier1.sety(y)
        soldierbulletspeed = level * 6
        soldierbullet1speed = level * 6
        next_level = False
    elif next_level == True and level >= 9:
        another_level = True
        number_of_soldiers = 4
        turtle.delay(10)
        for i in range(number_of_soldiers):
            soldiers.append(turtle.Turtle())
        for soldier in soldiers:
            soldier.color("red")
            soldier.shape("Soldier-shoot.gif")
            soldier.penup()
            soldier.speed(0)
            x = random.randint(200, 300)
            y = random.randint(-250, 260)
            soldier.setposition(x, y)
            y = soldier.ycor()
            y += soldierspeed
            soldier.sety(y)
        number_of_soldiers1 = 4
        for i in range(number_of_soldiers1):
            soldiers1.append(turtle.Turtle())
        for soldier1 in soldiers1:
            soldier1.color("red")
            soldier1.shape("Soldier-shoot.gif")
            soldier1.penup()
            soldier1.speed(0)
            x = random.randint(200, 300)
            y = random.randint(-250, 260)
            soldier1.setposition(x, y)
            y = soldier1.ycor()
            y += soldier1speed
            soldier1.sety(y)
        soldierbulletspeed = level * 6
        soldierbullet1speed = level * 6
        next_level = False
        
    if another_level == True and level > 4 and level < 9:
        turtle.delay(10)
        number_of_tanks = level - 4
        for i in range(number_of_tanks):
            tanks.append(turtle.Turtle())
        for tank in tanks:
            tank.color("red")
            tank.shape("sherman_tank.gif")
            tank.penup()
            tank.speed(0)
            x = random.randint(200, 300)
            y = random.randint(-250, 260)
            tank.setposition(x, y)
            y = tank.ycor()
            y += tankspeed
            tank.sety(y)
        number_of_tanks1 = level - 5
        for i in range(number_of_tanks1):
            tanks1.append(turtle.Turtle())
        for tank1 in tanks1:
            tank1.color("red")
            tank1.shape("sherman_tank.gif")
            tank1.penup()
            tank1.speed(0)
            x = random.randint(200, 300)
            y = random.randint(-250, 260)
            tank1.setposition(x, y)
            y = tank1.ycor()
            y += tank1speed
            tank1.sety(y)
        tankbulletspeed = level * 8
        tankbullet1speed = level * 8
        another_level = False
    elif another_level == True and level >= 9:
        number_of_tanks = 3
        turtle.delay(10)
        for i in range(number_of_tanks):
            tanks.append(turtle.Turtle())
        for tank in tanks:
            tank.color("red")
            tank.shape("sherman_tank.gif")
            tank.penup()
            tank.speed(0)
            x = random.randint(200, 300)
            y = random.randint(-250, 260)
            tank.setposition(x, y)
            y = tank.ycor()
            y += tankspeed
            tank.sety(y)
        number_of_tanks1 = 3
        for i in range(number_of_tanks1):
            tanks1.append(turtle.Turtle())
        for tank1 in tanks1:
            tank1.color("red")
            tank1.shape("sherman_tank.gif")
            tank1.penup()
            tank1.speed(0)
            x = random.randint(200, 300)
            y = random.randint(-250, 260)
            tank1.setposition(x, y)
            y = tank1.ycor()
            y += tank1speed
            tank1.sety(y)
        tankbulletspeed = level * 8
        tankbullet1speed = level * 8
        another_level = False

    #FirePlayerBullet
    if bulletstate == "fire":
        x = bullet.xcor()
        x += bulletspeed
        bullet.setx(x)
            
    if bullet.xcor() > 320:
        bullet.hideturtle()
        bulletstate = "ready"

    if bullet1state == "fire":
        x = bullet1.xcor()
        x += bullet1speed
        bullet1.setx(x)
            
    if bullet1.xcor() > 320:
        bullet1.hideturtle()
        bullet1state = "ready"

    #Fire AllyBullet
    if number_of_allies >= 1 and allybulletstate == "ready":
        allybulletstate = "fire"
        x = ally.xcor() - 10
        y = ally.ycor()
        allybullet.setposition(x, y)
        allybullet.showturtle()

    if allybulletstate == "fire":
        x = allybullet.xcor()
        x += allybulletspeed
        allybullet.setx(x)

    if allybullet.xcor() > 320:
        allybullet.hideturtle()
        allybulletstate = "ready"
        
    if number_of_allies1 >= 1 and allybullet1state == "ready":
        allybullet1state = "fire"
        x = ally1.xcor() - 10
        y = ally1.ycor()
        allybullet1.setposition(x, y)
        allybullet1.showturtle()

    if allybullet1state == "fire":
        x = allybullet1.xcor()
        x += allybullet1speed
        allybullet1.setx(x)

    if allybullet1.xcor() > 320:
        allybullet1.hideturtle()
        allybullet1state = "ready"

    #Fire EnemyBullet
    if number_of_enemies >= 1 and enemybulletstate == "ready":
        enemybulletstate = "fire"
        x = enemy.xcor() - 10
        y = enemy.ycor()
        enemybullet.setposition(x, y)
        enemybullet.showturtle()
        
    if enemybulletstate == "fire":
        x = enemybullet.xcor()
        x -= enemybulletspeed
        enemybullet.setx(x)

    if enemybullet.xcor() < -320:
        enemybullet.hideturtle()
        enemybulletstate = "ready"

    if number_of_enemies1 >= 1 and enemybullet1state == "ready":
        enemybullet1state = "fire"
        x = enemy1.xcor() - 10
        y = enemy1.ycor()
        enemybullet1.setposition(x, y)
        enemybullet1.showturtle()
        
    if enemybullet1state == "fire":
        x = enemybullet1.xcor()
        x -= enemybullet1speed
        enemybullet1.setx(x)

    if enemybullet1.xcor() < -320:
        enemybullet1.hideturtle()
        enemybullet1state = "ready"
        
    #Fire SoldierBullet
    if number_of_soldiers >= 1 and soldierbulletstate == "ready":
        soldierbulletstate = "fire"
        x = soldier.xcor()
        y = soldier.ycor() + 15
        soldierbullet.setposition(x, y)
        soldierbullet.showturtle()

    if soldierbulletstate == "fire":
        x = soldierbullet.xcor()
        x -= soldierbulletspeed
        soldierbullet.setx(x)

    if soldierbullet.xcor() < -320:
        soldierbullet.hideturtle()
        soldierbulletstate = "ready"

    if number_of_soldiers1 >= 1 and soldierbullet1state == "ready":
        soldierbullet1state = "fire"
        x = soldier1.xcor()
        y = soldier1.ycor() + 15
        soldierbullet1.setposition(x, y)
        soldierbullet1.showturtle()

    if soldierbullet1state == "fire":
        x = soldierbullet1.xcor()
        x -= soldierbullet1speed
        soldierbullet1.setx(x)

    if soldierbullet1.xcor() < -320:
        soldierbullet1.hideturtle()
        soldierbullet1state = "ready"

    #Fire TankBullet        
    if number_of_tanks >= 1 and tankbulletstate == "ready":
        tankbulletstate = "fire"
        x = tank.xcor() - 20
        y = tank.ycor()
        tankbullet.setposition(x, y)
        tankbullet.showturtle()
        
    if tankbulletstate == "fire":
        x = tankbullet.xcor()
        x -= tankbulletspeed
        tankbullet.setx(x)

    if tankbullet.xcor() < -320:
        tankbullet.hideturtle()
        tankbulletstate = "ready"

    if number_of_tanks1 >= 1 and tankbullet1state == "ready":
        tankbullet1state = "fire"
        x = tank1.xcor() - 20
        y = tank1.ycor()
        tankbullet1.setposition(x, y)
        tankbullet1.showturtle()
        
    if tankbullet1state == "fire":
        x = tankbullet1.xcor()
        x -= tankbullet1speed
        tankbullet1.setx(x)

    if tankbullet1.xcor() < -320:
        tankbullet1.hideturtle()
        tankbullet1state = "ready"
