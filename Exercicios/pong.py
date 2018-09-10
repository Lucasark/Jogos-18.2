from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.collision import *

rebater = Collision()

altura = 600
largura = 800
janela = Window(largura, altura)
janela.set_title("jogo do pong")
janela.set_background_color((0, 0, 255))
bola = Sprite("pongBall.png", 1)
player = Sprite("pongPaddle.png", 1)
cpu = Sprite("pongPaddle.png",1)

player.set_position(10,altura/2)
cpu.set_position(largura-30,altura/2)

bola.set_position(largura/2, altura/2)
fundo = GameImage("pongTable.png")
playing = True

vx = 1
vy = cpuy = -1
lastImpact = True
acelerador =0.2

playerScore = cpuScore = 0


while playing:

    bola.x += vx
    bola.y -= vy

    cpu.move_y(-cpuy)

    if rebater.collided(player,bola):
        bola.set_position(bola.x+2,bola.y+2)
        vx += 0.010
        vx = -vx
        lastImpact = True
    elif rebater.collided(cpu,bola):
        bola.set_position(bola.x-3,bola.y-3)
        vx += 0.010
        vx = -vx
        lastImpact = False

    if cpu.y > altura or cpu.y < 0:
        cpuy = -cpuy

    if bola.x >= 780 or bola.x <= 0:
       bola.set_position(largura/2,altura/2)
       cpu.set_position(largura-30,altura/2)
       acelerador =-0.1
       vx = 1
       if lastImpact:
           playerScore +=1
           if playerScore == 10:
               print("PLAYER WINS!")
               playerScore = cpuScore = 0
       else:
           cpuScore +=1
           if cpuScore == 10:
               print("CPU WINS!")
               playerScore = cpuScore = 0
    if bola.y >= 580 or bola.y <= 0:
        vy = -vy

    player.move_key_y(1)

    fundo.draw()
    bola.draw()
    player.draw()
    cpu.draw()
    janela.update()







