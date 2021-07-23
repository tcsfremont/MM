import pgzrun 
from random import random
#player 
Game_over = False  
Game_start = False
Lives = 3

player = Actor("aliens")
player.x = 400 
player.y = 600 - player.height * 0.5 

speed = 8
cooldown = 0.5 
cooled = True
def cool():
    global cooled 
    cooled = True
lasers = [] 

#Spaceship
spaceships = []
def add_spaceship():
    spaceship = Actor("spaceship")  
    spaceship.x = 800 * random()
    spaceship.y = 0# spaceship.height * 0.5
    spaceships.append(spaceship)
def on_key_down(key):
    global Game_start
    if not Game_start:
        Game_start = True
        clock.schedule_interval(add_spaceship, 2)

add_spaceship()
def fire_laser():
    global cooled, cooldown
    if cooled:
        laser = Rect((player.x - 2, player.y),(5,10))
        lasers.append(laser)
        cooled = False 
        clock.schedule_unique(cool, cooldown) 

def update():
  
    
    global Game_over, Game_start, Lives
     
    if not Game_start: 
        return 

    if not Game_over :
        
        if keyboard.left and player.x > player.width * 0.5:
            player.x -= speed

        if keyboard.right and player.x < 800 - player.width * 0.5:
            player.x += speed 

        if keyboard.up: 
            pass 

        if keyboard.down:
            pass      

        if keyboard.space:
            fire_laser()

    for spaceship in spaceships:
        spaceship.y += 3
        if spaceship.y > 580:
            if Lives: 
                Lives -= 1
                spaceships.clear()
                player.x = 400
                Game_start = False
                clock.unschedule(add_spaceship)
            else:
                Game_over = True

    for laser in lasers:
        laser.y -= 10 
        for spaceship in spaceships:
             if laser.x > spaceship.x - spaceship.width * 0.5:
                 if laser.y > spaceship.y - spaceship.height * 0.5:
                     if laser.x < spaceship.x + spaceship.width * 0.5:
                         if laser.y < spaceship.y + spaceship.height * 0.5:
                            spaceships.remove(spaceship)

def draw():
    global Lives, Game_over
    screen.clear()

    player.draw()
    for spaceship in spaceships:   
       spaceship.draw()
    for laser in lasers:
      screen.draw.filled_rect(laser,(118,244,165)) 

    screen.draw.text("Lives: " + str(Lives), (0, 0)) 
    
    if Game_over:
        screen.draw.text("Game Over", (350, 300))

pgzrun.go()

