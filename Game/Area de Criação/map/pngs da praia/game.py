from PPlay.window import *
from PPlay.collision import *
from PPlay.gameimage import *
import settings as s

#janela
janela = Window(s.WIDTH, s.HEIGHT)  # 720,480 - 1280,720
janela.set_background_color((255,255,255))
janela.set_title(s.TITLE)
#janela.set_fullscreen()
background_da_janela = GameImage(s.background_do_background)

#mouse
mouse = janela.get_mouse()

#fundo
fundo = GameImage(s.bg)

#teclado
k = Window.get_keyboard()

#velocidade
velocidade = 250*janela.delta_time()

#colisao
colisao_pplay = Collision()



#TILE - o uso do numero 32, graças a sua motherfucking lógica de uso de tiles ta sendo bem conveniente, então pro professor não ficar "ui ta usando número absoluto" eu to declarando uma variavel
tile = 32

#SET_POSITION: PLAYER

player = GameImage(s.player)
player.set_position(s.WIDTH/2, s.HEIGHT/2)

#SET POSITIONS: BACKGROUD

#Monster Spawn
monster_spawn = GameImage(s.cenario[0])
monster_spawn.set_position(fundo.width-monster_spawn.width-tile,fundo.height/2)

#pedra de cenário
pedra_de_5_lados = GameImage(s.pedra)
pedra_de_5_lados.set_position(fundo.width/2+tile*3,fundo.height/2+tile*3)

#Agua
agua = GameImage(s.borderEdge[2])
agua.set_position(0, fundo.height-agua.height)

#Blogueio
bloqueio1 = GameImage(s.borderEdge[1]) #Superior
bloqueio2 = GameImage(s.borderEdge[0]) #Lateral-Esq
bloqueio3 = GameImage(s.borderEdge[0]) #Lateral-Dir
bloqueio1.set_position(tile, 0)
bloqueio3.set_position(fundo.width-tile, 0)
bloqueio2.set_position(0, 0)


#Grama
grama = GameImage(s.borderEdge[3])
grama.set_position(0, 0)

#Arvores
arvore_1 = GameImage(s.cenario[1])
arvore_2 = GameImage(s.cenario[2])
arvore_3 = GameImage(s.cenario[3])
arvore_4 = GameImage(s.cenario[2])

arvore_1.set_position(tile,bloqueio1.height)
arvore_2.set_position(tile,arvore_1.height)
arvore_3.set_position(fundo.width-tile*4,bloqueio1.height)
arvore_4.set_position(arvore_3.x,arvore_3.height)

#Appendes do BG:
nao_colidiveis = [fundo, grama,monster_spawn]
colidiveis_esq = [bloqueio2]
colidiveis_dir = [bloqueio3]
colidiveis_cima = [bloqueio1]
colidiveis_baixo = [agua]
colidiveis = [arvore_1, arvore_2, arvore_3, arvore_4, pedra_de_5_lados]
bg_total = nao_colidiveis + colidiveis + colidiveis_cima + colidiveis_baixo + colidiveis_dir + colidiveis_esq

#Button
def butao_click(mouse, butao):
    if mouse[0] >= butao.x and mouse[0] <= butao.x + butao.width and mouse[1] >= butao.y and mouse[1] <= butao.y + butao.height:
        return True

#Click "Pause"
def click_pause(wait):
    if s.CLICK_SIGNAL and s.CLICK_TIME == 0:
        s.CLICK_SIGNAL = False
        s.CLICK_TIME = wait
        return True
    return False

def click_call():
    if s.CLICK_TIME == 0 and not s.CLICK_SIGNAL:
        s.CLICK_SIGNAL = True
    if s.CLICK_TIME != 0:
        if not s.CLICK_SIGNAL:
            s.CLICK_TIME -= 1
        else:
            s.CLICK_TIME = 20

#Collisions
def colisao_direita(atr,player):
    for i in range(len(atr)):
        if colisao_pplay.collided_perfect(player, atr[i]):
            s.andar_direita = False
            s.andar_baixo = True
            s.andar_cima = True
            s.andar_esquerda = True
            return True
    s.andar_direita = True
    s.andar_baixo = True
    s.andar_cima = True
    s.andar_esquerda = True
    return False

#Obejto_1 colide com objeto_2 pela esqueda no proximo loop?:
def range_esq(obj_1, obj_2, time):
    if obj_1.x-time >= obj_2.x+obj_2.width:
        return True
    return False

def colisao_esquerda(atr, player):
    #vel = 350 * janela.delta_time()
    for i in range(len(atr)):
        if colisao_pplay.collided_perfect(player, atr[i]):
            s.andar_direita = True
            s.andar_baixo = True
            s.andar_cima = True
            s.andar_esquerda = False
            return True
    s.andar_direita = True
    s.andar_baixo = True
    s.andar_cima = True
    s.andar_esquerda = True
    return False

def range_cima(obj_1, obj_2):
    print(obj_1.y, " ", obj_2.y, " ", obj_2.height)
    if obj_1.y-5 <= obj_2.y+obj_2.height:
        return True
    return False

def colisao_cima(atr, player):
    for i in range(len(atr)):
        if colisao_pplay.collided_perfect(player, atr[i]):
            s.andar_direita = True
            s.andar_baixo = True
            s.andar_cima = False
            s.andar_esquerda = True
            return True
    s.andar_direita = True
    s.andar_baixo = True
    s.andar_cima = True
    s.andar_esquerda = True
    return False

def colisao_baixo(atr,player):
    for i in range(len(atr)):
        if colisao_pplay.collided_perfect(player, atr[i]):
            s.andar_direita = True
            s.andar_baixo = False
            s.andar_cima = True
            s.andar_esquerda = True
            return True
    s.andar_direita = True
    s.andar_baixo = True
    s.andar_cima = True
    s.andar_esquerda = True
    return False

#Appendes do Cenario:


def draw_sprite(atr):
    for i in range(len(atr)):
        atr[i].draw()

def movimento_objet(atr, mov, orien):
    velocidade = 350 * janela.delta_time()
    if mov == 1 and orien == 'x':
        for i in range(len(atr)):
            atr[i].x += velocidade
        #res.x -= velocidade

    elif mov == -1 and orien == 'x':
        for i in range(len(atr)):
            atr[i].x -= velocidade
        #res.x += velocidade

    elif mov == 1 and orien == 'y':
        for i in range(len(atr)):
            atr[i].y -= velocidade
        #res.y += velocidade

    elif mov == -1 and orien == 'y':
        for i in range(len(atr)):
            atr[i].y += velocidade
        #res.y -= velocidade

def andar():
    if k.key_pressed("A") or k.key_pressed("LEFT") and s.andar_esquerda: #<-
        if not colisao_esquerda(colidiveis+colidiveis_esq,player):
            movimento_objet(bg_total, 1, 'x')
        else:
            movimento_objet(bg_total, -1,'x')


    elif k.key_pressed("D") or k.key_pressed("RIGHT") and s.andar_direita: #->
        if not colisao_direita(colidiveis+colidiveis_dir,player):
            movimento_objet(bg_total, -1, 'x')
        else:
            movimento_objet(bg_total, 1,'x')

    elif k.key_pressed("S") or k.key_pressed("DOWN") and s.andar_baixo: #\/
        if not colisao_baixo(colidiveis+colidiveis_baixo, player):
            movimento_objet(bg_total, 1, 'y')
        else:
            movimento_objet(bg_total,-1,'y')

    elif k.key_pressed("W") or k.key_pressed("UP") and s.andar_cima: #/\
        if not colisao_cima(colidiveis+colidiveis_cima, player):
            movimento_objet(bg_total, -1, 'y')
        else:
            movimento_objet(bg_total,1 ,'y')

def opcoes():
    if k.key_pressed("F") and click_pause(s.CLICK_TIME_WAIT):
        print("FERRAMENTAS")
    elif k.key_pressed("E") and click_pause(s.CLICK_TIME_WAIT):
        print("HABILIDADES")
    elif k.key_pressed("ESC") and click_pause(s.CLICK_TIME_WAIT):
        print("sair")
        janela.close()


#print(player.x, ":X - Y:", player.y,"     ",s.WIDTH,":S.W  -  F.W",fundo.width,"         ",fundo.x,":f.x   -  f.y",fundo.y)

def update():
    janela.set_title(str(janela.delta_time()))
    andar()
    opcoes()
    player.draw()
    janela.update()

while True:
    click_call()
    background_da_janela.draw()
    draw_sprite(bg_total)
    #print("E: ",s.andar_esquerda,"D: ",s.andar_direita,"C: ",s.andar_cima,"B: ",s.andar_baixo)
    update()
