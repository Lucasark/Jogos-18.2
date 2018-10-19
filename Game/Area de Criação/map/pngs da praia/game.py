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
colidiveis = [bloqueio1, bloqueio2, bloqueio3,arvore_1,arvore_2,agua,arvore_3,arvore_4,pedra_de_5_lados]
bg_total = nao_colidiveis + colidiveis

#colisões:



#Seguinte meu bruxo, eu dividi as colisões em 4 e adicionei um valor booleano correspondente a cada direção na função andar()
#não é nem de longe a melhor solução, mas como a gente ta meio sem tempo eu já rushei isso aí, vê o que que vc acha e me da o feedback




pode_andar_direita = pode_andar_cima = pode_andar_esquerda = pode_andar_baixo = True


def colisao_direita(atr,player):
    global pode_andar_direita
    global pode_andar_cima
    global pode_andar_esquerda
    global pode_andar_baixo
    for i in range(len(atr)):
        if colisao_pplay.collided_perfect(player,atr[i]):
            pode_andar_direita = False
            pode_andar_baixo = False
            pode_andar_cima = False
            pode_andar_esquerda = True
            return True
    pode_andar_direita = True
    pode_andar_baixo = True
    pode_andar_cima = True
    pode_andar_esquerda = True
    return False

def colisao_esquerda(atr,player):
    global pode_andar_direita
    global pode_andar_cima
    global pode_andar_esquerda
    global pode_andar_baixo
    for i in range(len(atr)):
        if colisao_pplay.collided_perfect(player,atr[i]):
            pode_andar_direita = True
            pode_andar_baixo = False
            pode_andar_cima = False
            pode_andar_esquerda = False
            return True
    pode_andar_direita = True
    pode_andar_baixo = True
    pode_andar_cima = True
    pode_andar_esquerda = True
    return False

def colisao_cima(atr,player):
    global pode_andar_direita
    global pode_andar_cima
    global pode_andar_esquerda
    global pode_andar_baixo
    for i in range(len(atr)):
        if colisao_pplay.collided_perfect(player,atr[i]):
            pode_andar_direita = False
            pode_andar_baixo = True
            pode_andar_cima = False
            pode_andar_esquerda = False
            return True
    pode_andar_direita = True
    pode_andar_baixo = True
    pode_andar_cima = True
    pode_andar_esquerda = True
    return False

def colisao_baixo(atr,player):
    global pode_andar_direita
    global pode_andar_cima
    global pode_andar_esquerda
    global pode_andar_baixo
    for i in range(len(atr)):
        if colisao_pplay.collided_perfect(player,atr[i]):
            pode_andar_direita = False
            pode_andar_baixo = False
            pode_andar_cima = True
            pode_andar_esquerda = False
            return True
    pode_andar_direita = True
    pode_andar_baixo = True
    pode_andar_cima = True
    pode_andar_esquerda = True
    return False







# def colisao(atr,player):
#     for i in range(0,len(atr)):
#         if player.x+1 == atr[i].x:
#             return True
#         elif player.x-1 == atr[i].x:
#             return True
#         elif player.y+1 == atr[i].y:
#             return True
#         elif player.y-1 == atr[i].y:
#             return True
#     return False

#Appendes do Cenario:




def draw_sprite(atr):
    for i in range(len(atr)):
        atr[i].draw()

def movimento_objet(atr, mov, orien):
    velocidade = 250 * janela.delta_time()
    if mov == 1 and orien == 'x':
        for i in range(len(atr)):
            atr[i].x += velocidade

    elif mov == -1 and orien == 'x':
        for i in range(len(atr)):
            atr[i].x -= velocidade

    elif mov == 1 and orien == 'y':
        for i in range(len(atr)):
            atr[i].y -= velocidade

    elif mov == -1 and orien == 'y':
        for i in range(len(atr)):
            atr[i].y += velocidade

def andar():
    if k.key_pressed("A") or k.key_pressed("LEFT") and pode_andar_esquerda: #<-

        '''
        if (fundo.x + player.x >= 0):
            player.x -= 1
        else:
        '''
        if not colisao_esquerda(colidiveis,player):
            movimento_objet(bg_total, 1, 'x')
        else:
            movimento_objet(bg_total, -1,'x')


    elif k.key_pressed("D") or k.key_pressed("RIGHT") and pode_andar_direita: #->
        '''
        if (fundo.x + player.x <= 0 ):
            player.x += 1
        else:
        '''
        if not colisao_direita(colidiveis,player):
            movimento_objet(bg_total, -1, 'x')
        else:
            movimento_objet(bg_total, 1,'x')

    elif k.key_pressed("S") or k.key_pressed("DOWN") and pode_andar_baixo:
        if not colisao_baixo(colidiveis, player):
            movimento_objet(bg_total, 1, 'y')
        else:
            movimento_objet(bg_total,-1,'y')
    elif k.key_pressed("W") or k.key_pressed("UP") and pode_andar_cima:
        if not colisao_cima(colidiveis, player):
            movimento_objet(bg_total, -1, 'y')
        else:
            movimento_objet(bg_total,1,'y')

#print(player.x, ":X - Y:", player.y,"     ",s.WIDTH,":S.W  -  F.W",fundo.width,"         ",fundo.x,":f.x   -  f.y",fundo.y)

def update():
    janela.set_title(str(janela.delta_time()))
    andar()
    player.draw()
    janela.update()

while True:
    background_da_janela.draw()
    draw_sprite(bg_total)
    update()
