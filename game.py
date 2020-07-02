import random

WIDTH = 800
HEIGHT = 500

pinkthing = Actor("alien")
pinkthing.pos = 35,450

butt_on = Actor("butt_on")
butt_on.pos =(WIDTH/2, HEIGHT/2 +160)

score = 19

speed = 6

lives = 40

game_status = 1

hurt = ""

def draw():
    global game_status
    screen.clear()

    if game_status == 1:
        screen.clear()
        screen.fill((6, 209, 255))
        screen.blit('lvl_2_mucode_game', (0, -200))
        screen.draw.text("Alien Clicker", (5,25), angle = 5, color="red", fontname="blob", fontsize=40, background = (255,191,0), owidth = 2, ocolor = "yellow")
        screen.draw.text("made by aarav", (5, 90), angle = -5, color="red", fontname="blob", fontsize=20, background = (255,191,0), owidth = 2, ocolor = "yellow")
        pinkthing.draw()
        screen.draw.text(f'Score: {str(score)}', (600, 10), color = "orange", fontsize=40)
        screen.draw.text(f'Speed: {str(speed)}', (600, 50), color = "orange", fontsize=40)
        screen.draw.text(f'Lives: {str(lives)}', (600, 90), color = "orange", fontsize=40)
        screen.draw.text('Reach score 20 to win!!!', (560, 130), color = "red", fontsize=25)

        if hurt=='hurt':
            screen.draw.text("STOP TOUCHING ME!!!", center = (WIDTH/2, HEIGHT/2), color = "blue", fontname="pencil", fontsize=30)
        elif hurt == 'miss':
            screen.draw.text("HAHAHA u didnt touch me", center = (WIDTH/2, HEIGHT/2), color = "blue", fontname="pencil", fontsize=30)

        if lives == 0:
            game_status = 0

        if score == 20:
            game_status = 2

    elif game_status == 0:
        screen.clear()
        sounds.splat.stop()
        screen.fill((0,0,0))
        screen.draw.text('GAME OVER', center = (WIDTH/2, HEIGHT/2), color = "red", fontsize=150, fontname="scaryfont")
        screen.draw.text('Click me to play again!!', center = (WIDTH/2, HEIGHT/2 +80), color = "blue", fontsize=40, fontname="starwars")
        butt_on.draw()

    elif game_status == 2:
        screen.clear()
        screen.fill((0,238,255))
        screen.draw.text('You Win!!!', center = (WIDTH/2, HEIGHT/2), color = "red", fontsize=150, fontname="cartoonblocks")
        butt_on.draw()

def update():
    global speed
    if speed < 0:
        speed = 0
    pinkthing.left +=speed
    print(pinkthing.left)
    if pinkthing.left > 800:
        pinkthing.left = 0
        pinkthing.pos=35,random.randint(250,450)

def on_mouse_down(pos,button):
    global hurt, score, speed, lives,game_status
    if button == mouse.LEFT and pinkthing.collidepoint(pos):
        hurt = "hurt"
        score +=1
        speed +=1
        pinkthing.image = "alien_hurt"
        sounds.splat.play()
        clock.schedule_unique(set_pinkthing_normal, 0.6)
    else:
        hurt = "miss"
        score -=1
        speed -=1
        lives -=1
        clock.schedule_unique(set_miss_text, 0.5)

        if score < 0:
            score = 0
            speed = 6

    if lives <= 0 and game_status == 0 and button == mouse.LEFT and butt_on.collidepoint(pos):
        lives = 40
        speed = 6
        score = 0
        game_status = 1

    if game_status == 2 and button == mouse.LEFT and butt_on.collidepoint(pos):
        lives = 40
        speed = 6
        score = 0
        game_status = 1

def set_pinkthing_normal():
    global hurt
    pinkthing.image='alien'
    hurt =""

def set_miss_text():
    global hurt
    hurt =""
def on_mouse_move(pos,buttons):
    if mouse.LEFT in buttons:
        pinkthing.pos = pos
