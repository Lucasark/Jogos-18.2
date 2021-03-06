from PPlay.window import *
from PPlay.collision import *
from PPlay.mouse import *
from PPlay.gameimage import *
from PPlay.animation import *
from PPlay.sprite import *
import settings as s
#import options as o
#import classes as c

#janela
#from collision import Collision

#from gameimage import GameImage

janela = Window(s.WIDTH, s.HEIGHT)  # 720,480 - 1280,720
janela.set_background_color((255, 255, 255))
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

tile = 32

#SET_POSITION: PLAYER

direcao_player = 0
player = Animation(s.player[direcao_player],3)
player.set_total_duration(1000)
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
bloqueio1 = GameImage(s.borderEdge[1]) #Superior-Esq
bloqueio2 = GameImage(s.borderEdge[0]) #Lateral-Esq
bloqueio3 = GameImage(s.borderEdge[0]) #Lateral-Dir
bloqueio4 = GameImage(s.borderEdge[1])#Superior-Dir
bloqueio1.set_position(tile, 0)
bloqueio3.set_position(fundo.width-tile, 0)
bloqueio2.set_position(0, 0)
bloqueio4.set_position(bloqueio1.x+bloqueio1.width+tile*4,bloqueio1.y)


#gambiarra:
bloco_esquerda = GameImage(s.gambiarra_bloco)
bloco_direita = GameImage(s.gambiarra_bloco)

bloco_esquerda.set_position(bloqueio1.x+bloqueio1.width-tile,bloqueio1.y-tile)
bloco_direita.set_position(bloqueio4.x,bloqueio4.y)


#Grama
grama = GameImage(s.borderEdge[3])
grama.set_position(0, 0)

#Arvores
arvore_1 = GameImage(s.cenario[1])
arvore_2 = GameImage(s.cenario[2])
arvore_3 = GameImage(s.cenario[3])
arvore_4 = GameImage(s.cenario[2])
arvore_spawn = GameImage(s.cenario[1])

arvore_1.set_position(tile,bloqueio1.height)
arvore_2.set_position(tile,arvore_1.height)
arvore_3.set_position(fundo.width-tile*4,bloqueio1.height)
arvore_4.set_position(arvore_3.x,arvore_3.height)
arvore_spawn.set_position(fundo.width/2,arvore_4.y+arvore_4.height)

s.AUX_E[0] = 0
s.AUX_E[1] = 0
s.AUX_D[0] = janela.width
s.AUX_D[1] = janela.height

#----RECURSOS----#

def spawn(png,x,y):
    imagem = GameImage(png)
    imagem.set_position(x,y)
    return imagem


def spawn_madeira(arvore):
    a = s.recursos[3]
    x = arvore.x
    y = arvore.y
    madeiras = [spawn(a,x-tile,y-tile),spawn(a,x,y-tile),spawn(a,x+tile,y-tile),spawn(a,x+tile*2,y-tile),spawn(a,x+tile*3,y-tile),
                spawn(a,x-tile,y),spawn(a,x+tile*3,y),
                spawn(a, x - tile, y+tile), spawn(a, x + tile * 3, y+tile),
                spawn(a, x - tile, y + tile*2), spawn(a, x + tile * 3, y + tile*2),
                spawn(a, x - tile, y+tile*3), spawn(a, x + tile * 3, y+tile*3),
                spawn(a, x - tile, y+tile*4), spawn(a, x, y+tile*4), spawn(a, x + tile, y+tile*4),spawn(a, x + tile * 2, y+tile*4), spawn(a, x + tile * 3, y+tile*4)]
    for i in range(len(madeiras)):
      s.tempo_madeira[i] +=1
      if not colisao_pplay.collided(player,madeiras[i]) and s.estado_madeira[i] and s.tempo_madeira[i] > s.tempo_recurso_madeira[i]:# and tempo >:
        madeiras[i].draw()

        #break
      elif colisao_pplay.collided(player,madeiras[i]) and s.estado_madeira[i] and s.PODEMADEIRA:
          s.quantidade_de_recursos[3] += 1
          s.estado_madeira[i] = False
          s.tempo_madeira[i] = 0
      if not s.estado_madeira[i] and s.tempo_madeira[i] > s.loop_recursos[3]:
          s.estado_madeira[i] = True

def spawn_pedra(pedra):
    a = s.recursos[4]
    x = pedra.x
    y = pedra.y
    pedras = [spawn(a,x-tile,y-tile), spawn(a,x,y-tile),spawn(a,x+tile,y-tile),
              spawn(a,x-tile,y),spawn(a,x+tile,y),
              spawn(a,x-tile,y+tile),spawn(a,x,y+tile),spawn(a,x+tile,y+tile)]
    for i in range(len(pedras)):
        s.tempo_pedra[i] += 1
        if not colisao_pplay.collided(player,pedras[i]) and s.estado_pedra[i]  and s.tempo_pedra[i] > s.tempo_recurso_pedra[i]:
            pedras[i].draw()
        elif colisao_pplay.collided(player,pedras[i]) and s.estado_pedra[i] and s.PODEPEDRA:
            s.quantidade_de_recursos[4] += 1
            s.estado_pedra[i] = False
            s.tempo_pedra[i] =0
        if not s.estado_pedra[i] and s.tempo_pedra[i] > s.loop_recursos[4]:
            s.estado_pedra[i] = True




#-------------------------------------------------HUD--------------------------------------#
HP = [spawn(s.hud[0],0,0),spawn(s.hud[0],tile,0),spawn(s.hud[0],tile*2,0),spawn(s.hud[0],tile*3,0),spawn(s.hud[0],tile*4,0)]


quantidade_HUD_madeira = Sprite(s.hud[1])
quantidade_HUD_madeira.set_position(0+quantidade_HUD_madeira.width,0+tile*2-(quantidade_HUD_madeira.height/2))

madeira_HUD = Sprite(s.hud[2])
madeira_HUD.set_position(quantidade_HUD_madeira.x+quantidade_HUD_madeira.width-tile,quantidade_HUD_madeira.y)

ouro_HUD = Sprite(s.hud[3])
ouro_HUD.set_position(madeira_HUD.x,madeira_HUD.y+madeira_HUD.height+tile/2)

quantidade_HUD_ouro = Sprite(s.hud[1])
quantidade_HUD_ouro.set_position(quantidade_HUD_madeira.x,quantidade_HUD_madeira.y+quantidade_HUD_madeira.height+tile/2)

quantidade_HUD_pedra_coletavel = Sprite(s.hud[1])
quantidade_HUD_pedra_coletavel.set_position(ouro_HUD.x+ouro_HUD.width,ouro_HUD.y+ouro_HUD.height+tile/2)

pedra_coletavel_HUD = Sprite(s.hud[5])
pedra_coletavel_HUD.set_position(ouro_HUD.x,ouro_HUD.y+ouro_HUD.height+tile/2)

ferro_HUD = Sprite(s.hud[4])
ferro_HUD.set_position(pedra_coletavel_HUD.x,pedra_coletavel_HUD.y+pedra_coletavel_HUD.height+tile/2)

quantidade_HUD_ferro = Sprite(s.hud[1])
quantidade_HUD_ferro.set_position(ouro_HUD.x+ouro_HUD.width,pedra_coletavel_HUD.y+pedra_coletavel_HUD.height+tile/2)

cobre_HUD = Sprite(s.hud[6])
cobre_HUD.set_position(ferro_HUD.x,ferro_HUD.y+ferro_HUD.height+tile/2)

quantidade_HUD_cobre = Sprite(s.hud[1])
quantidade_HUD_cobre.set_position(cobre_HUD.x+cobre_HUD.width,ferro_HUD.y+ferro_HUD.height+tile/2)

madeira_refinada_HUD = Sprite(s.recursos[5])
madeira_refinada_HUD.set_position(cobre_HUD.x,cobre_HUD.y+cobre_HUD.height+tile/2)

quantidade_HUD_madeira_refinada = Sprite(s.hud[1])
quantidade_HUD_madeira_refinada.set_position(ouro_HUD.x+ouro_HUD.width,cobre_HUD.y+cobre_HUD.height+tile/2)

pedra_refinada_HUD = Sprite(s.recursos[6])
pedra_refinada_HUD.set_position(cobre_HUD.x,madeira_refinada_HUD.y+madeira_refinada_HUD.height+tile/2)

quantidade_HUD_pedra_refinada = Sprite(s.hud[1])
quantidade_HUD_pedra_refinada.set_position(ouro_HUD.x+ouro_HUD.width,madeira_refinada_HUD.y+madeira_refinada_HUD.height+tile/2)

pm_HUD = Sprite(s.recursos[7])
pm_HUD.set_position(ouro_HUD.x,pedra_refinada_HUD.y+pedra_refinada_HUD.height+tile/2)

quantidade_HUD_pm = Sprite(s.hud[1])
quantidade_HUD_pm.set_position(ouro_HUD.x+ouro_HUD.width,pedra_refinada_HUD.y+pedra_refinada_HUD.height+tile/2)


HUD_materials = [quantidade_HUD_ouro,quantidade_HUD_madeira,quantidade_HUD_pedra_coletavel,madeira_HUD,ouro_HUD,pedra_coletavel_HUD,
                 ferro_HUD,quantidade_HUD_ferro,quantidade_HUD_cobre,cobre_HUD,madeira_refinada_HUD,quantidade_HUD_madeira_refinada
                 ,pedra_refinada_HUD,quantidade_HUD_pedra_refinada,quantidade_HUD_pm,pm_HUD]


#mostrar o HUD ao teclar 0
def show_hud(pedra,madeira,ferro,cobre,ouro,madeira_refinada,pedra_refinada,pm):
    if k.key_pressed("0"):
        draw_sprite(HUD_materials)
        janela.draw_text(str(madeira), quantidade_HUD_madeira.x + quantidade_HUD_madeira.width, quantidade_HUD_madeira.y,
                     s.text[1], s.text[0], s.text[2])
        janela.draw_text(str(ouro), quantidade_HUD_ouro.x + quantidade_HUD_ouro.width, quantidade_HUD_ouro.y, s.text[1],
                     s.text[0], s.text[2])
        janela.draw_text(str(pedra), quantidade_HUD_pedra_coletavel.x + quantidade_HUD_pedra_coletavel.width, quantidade_HUD_pedra_coletavel.y, s.text[1],
                         s.text[0], s.text[2])
        janela.draw_text(str(ferro), quantidade_HUD_ferro.x + quantidade_HUD_ferro.width,
                         quantidade_HUD_ferro.y, s.text[1],
                         s.text[0], s.text[2])
        janela.draw_text(str(cobre), quantidade_HUD_cobre.x + quantidade_HUD_cobre.width,
                         quantidade_HUD_cobre.y, s.text[1],
                         s.text[0], s.text[2])
        janela.draw_text(str(madeira_refinada), quantidade_HUD_madeira_refinada.x + quantidade_HUD_madeira_refinada.width,
                         quantidade_HUD_madeira_refinada.y, s.text[1],
                         s.text[0], s.text[2])
        janela.draw_text(str(pedra_refinada), quantidade_HUD_pedra_refinada.x + quantidade_HUD_pedra_refinada.width,
                         quantidade_HUD_pedra_refinada.y, s.text[1],
                         s.text[0], s.text[2])
        janela.draw_text(str(pm), quantidade_HUD_pm.x + quantidade_HUD_pm.width,
                         quantidade_HUD_pm.y, s.text[1],
                         s.text[0], s.text[2])

        janela.draw_text("Experiencia :" +str(s.EXPERIENCIA),HP[-1].x+HP[-1].width,HP[-1].y,32,
                         s.text[0], s.text[2])

def show_HP(hp):
    for i in range(s.VIDA):
        hp[i].draw()


#Habilidades:
"""

[-1]    ->  Bloqueados: Imagem preta [SN1], e não está disponivel para compra
[1]     ->  Comprados: Imagem Cinza [CI] , já foi adquirido
[0]     ->  Liberados: Imagem Colorida [CO], liberado para compra

"""
habilidade_atual = [GameImage(s.COH[0]), GameImage(s.SNH[1]), GameImage(s.SNH[2]), GameImage(s.SNH[3]), GameImage(s.SNH[4]), GameImage(s.SNH[5]), GameImage(s.SNH[6]),
                    GameImage(s.SNH[7]), GameImage(s.SNH[8]), GameImage(s.SNH[9]), GameImage(s.SNH[10]), GameImage(s.SNH[11]), GameImage(s.SNH[12]),
                    GameImage(s.SNH[13]), GameImage(s.SNH[14]), GameImage(s.SNH[15]), GameImage(s.SNH[16]), GameImage(s.SNH[17]), GameImage(s.SNH[18])]
ferramenta_pagina_1 = [GameImage(s.FERRAMENTAS_BUTTON[0]), GameImage(s.FERRAMENTAS_BUTTON[1]), GameImage(s.FERRAMENTAS_BUTTON[2])]
ferramenta_pagina_2 = [GameImage(s.FERRAMENTAS_BUTTON[3]), GameImage(s.FERRAMENTAS_BUTTON[4])]
ferramenta_button = [GameImage(s.FERRRAMENTA_JANELA[0]), GameImage(s.FERRRAMENTA_JANELA[1])]

#Appendes do BG:
construcao = []
monstros = []
bomba = []
radio = []
nao_colidiveis = [fundo, grama, monster_spawn]
colidiveis = [bloqueio1, bloqueio2, bloqueio3,bloqueio4,arvore_1,arvore_2,agua,arvore_3,arvore_4,pedra_de_5_lados,bloco_esquerda,bloco_direita,arvore_spawn]
colidiveis_esquerda = [arvore_1,arvore_2,pedra_de_5_lados,bloqueio2,bloco_esquerda,bloqueio1,arvore_spawn]
colidiveis_baixo =[agua,pedra_de_5_lados,arvore_spawn]
colidiveis_direita =[arvore_3,arvore_4,bloqueio3,pedra_de_5_lados,bloco_direita,bloqueio4,arvore_spawn]
colidiveis_cima =[pedra_de_5_lados,bloqueio1,arvore_2,arvore_4,bloqueio4,arvore_spawn]


nome = GameImage(s.NOME)
butao_inicar = GameImage(s.INICIAR)


#centralizar objeto em relacao a janela
def centralizar_w(obj, quadro):
    return quadro.width/2 - (obj.width/2)

def centralizar_h(obj, quadro):
    return quadro.height/2 - (obj.height/2)

#Habilidades:
habilidade = GameImage(s.bg_habilidades)
habilidade.set_position(centralizar_w(habilidade, janela), centralizar_h(habilidade, janela))

#Ferramentas:
ferramenta = GameImage(s.bg_ferramenta)
ferramenta.set_position(centralizar_w(ferramenta, janela), centralizar_h(ferramenta, janela))

#posicionar objeto Xp abaixo em relativo a outro obj
def pos_relativo_h(rel, y):
    return rel.y + rel.height + y

def pos_relativo_w(rel, x):
    return rel.x + rel.width + x

def pos_relativo_h_neg(rel, obj, y):
    return rel.y - obj.height - y

def pos_relativo_w_neg(rel, obj, x):
    return rel.x - obj.width - x

#HABILIDAEDES POSIÇÃO:
habilidade_atual[0].set_position(centralizar_w(habilidade_atual[0],janela), centralizar_h(habilidade_atual[0], janela))
habilidade_atual[1].set_position(habilidade_atual[0].x, pos_relativo_h_neg(habilidade_atual[0], habilidade_atual[1], 32))
habilidade_atual[2].set_position(pos_relativo_w(habilidade_atual[0], 16), pos_relativo_h(habilidade_atual[0], 16))
habilidade_atual[3].set_position(pos_relativo_w_neg(habilidade_atual[0],habilidade_atual[3], 16), pos_relativo_h(habilidade_atual[0], 16))
habilidade_atual[4].set_position(habilidade_atual[3].x, pos_relativo_h_neg(habilidade_atual[1], habilidade_atual[4], 32))
habilidade_atual[5].set_position(habilidade_atual[2].x, pos_relativo_h_neg(habilidade_atual[1], habilidade_atual[4], 32))
habilidade_atual[6].set_position(pos_relativo_w(habilidade_atual[2], 32), habilidade_atual[2].y)
habilidade_atual[7].set_position(habilidade_atual[2].x, pos_relativo_h(habilidade_atual[2], 32))
habilidade_atual[8].set_position(habilidade_atual[3].x, habilidade_atual[7].y)
habilidade_atual[9].set_position(pos_relativo_w_neg(habilidade_atual[3], habilidade_atual[9], 32), habilidade_atual[3].y)
habilidade_atual[10].set_position(pos_relativo_w_neg(habilidade_atual[4], habilidade_atual[10], 16), pos_relativo_h_neg(habilidade_atual[4], habilidade_atual[10], 16),)
habilidade_atual[11].set_position(habilidade_atual[0].x, habilidade_atual[10].y)
habilidade_atual[12].set_position(pos_relativo_w(habilidade_atual[5], 16),pos_relativo_h_neg(habilidade_atual[5], habilidade_atual[12], 16))
habilidade_atual[13].set_position(pos_relativo_w(habilidade_atual[6], 32), habilidade_atual[6].y)
habilidade_atual[14].set_position(habilidade_atual[6].x + (habilidade_atual[6].width)/2, habilidade_atual[7].y + (habilidade_atual[7].height)/2)
habilidade_atual[15].set_position(habilidade_atual[7].x, pos_relativo_h(habilidade_atual[7], 32))
habilidade_atual[16].set_position(habilidade_atual[3].x, habilidade_atual[15].y)
habilidade_atual[18].set_position(pos_relativo_w_neg(habilidade_atual[9],habilidade_atual[18],32), habilidade_atual[9].y)
habilidade_atual[17].set_position(habilidade_atual[18].x + (habilidade_atual[18].width), habilidade_atual[8].y + (habilidade_atual[8].height)/2)

#FERRAMENTAS POSIÇÃO
#PAGINA 1
ferramenta_pagina_1[0].set_position(centralizar_w(ferramenta_pagina_1[0], janela), ferramenta.y + 100)
ferramenta_pagina_1[1].set_position(ferramenta_pagina_1[0].x, pos_relativo_h(ferramenta_pagina_1[0], 32))
ferramenta_pagina_1[2].set_position(ferramenta_pagina_1[0].x, pos_relativo_h(ferramenta_pagina_1[1], 32))
#PAGINA 2
ferramenta_pagina_2[0].set_position(centralizar_w(ferramenta_pagina_2[0], janela), ferramenta.y + 100)
ferramenta_pagina_2[1].set_position(ferramenta_pagina_2[0].x, pos_relativo_h(ferramenta_pagina_2[0], 32))
#ferramenta_pagina_2[1].set_position(ferramenta_pagina_2[0].x, pos_relativo_h(ferramenta_pagina_2[0], 32))

ferramenta_button[0].set_position(ferramenta.x, ferramenta.height-ferramenta_button[0].height)
ferramenta_button[1].set_position(ferramenta.width-ferramenta_button[1].width, ferramenta_button[0].y)

#MENU
nome.set_position(centralizar_w(nome, janela), centralizar_h(nome, janela))
butao_inicar.set_position(centralizar_w(butao_inicar, janela), pos_relativo_h(nome, 32))

#Experiencia loop
def exp_time():
    if s.TIME_TO_EXPERIENCIA == 0:
        s.TIME_TO_EXPERIENCIA = s.LOOK_EXPERIENCIA*1.02
        s.EXPERIENCIA += 1
    else:
        s.TIME_TO_EXPERIENCIA -= 1

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

def trocar_sprite_hab(old, pos, op):
    if op == 1:
        aux = GameImage(s.COH[pos])
        aux.set_position(old.x, old.y)
        return aux
    elif op == 0:
        aux = GameImage(s.CIH[pos])
        aux.set_position(old.x, old.y)
        return aux
    elif op == -1:
        aux = GameImage(s.SNH[pos])
        aux.set_position(old.x, old.y)
        return aux
    else:
        return 0

#-----Collisions----#

s.andar_cima = s.andar_cima = s.andar_esquerda = s.andar_baixo = True

def colisao_direita(atr, player):
    s.andar_direita = s.andar_cima = s.andar_esquerda = s.andar_baixo = True
    for i in range(0,len(atr)):
        if (player.y >= atr[i].y or player.y+player.height > atr[i].y) and  player.y < atr[i].y+atr[i].height and atr[i].x-player.x >=0:
            if player.x+player.width+350*janela.delta_time() >= atr[i].x:
                s.andar_direita = False
                return True
            #else:
                 #print(i)
                 #print("Object x:",atr[i].x,"object y:", atr[i].y,"player x and y:", player.x, player.y,"object height and width:", atr[i].height,atr[i].width)
    s.andar_direita = True
    return False

def colisao_esquerda(atr,player):
    s.andar_direita = s.andar_cima = s.andar_esquerda = s.andar_baixo = True
    for i in range(len(atr)):
        if (player.y >= atr[i].y or player.y+player.height > atr[i].y) and player.y <= atr[i].y + atr[i].height: # Player está entre o objeto(eixo vertical)
            if atr[i].x+atr[i].width <= player.x: # o ponto mais a direita(que é o que pode colidir com player) é menor que a posição atual de player(o que deve acontecer, porque se isso da false é pq o objeto está a direita de player,logo, não pode colidir pela esquerda)
                if player.x-350*janela.delta_time() <= atr[i].x+atr[i].width:
                    s.andar_esquerda = False
                    #print(atr[i].x,atr[i].y,player.x+player.width,player.y,atr[i].height)
                    return True
            #else:
                 #print(i)
                 #print("Object x:",atr[i].x,"object y:", atr[i].y,"player x and y:", player.x, player.y,"object height and width:", atr[i].height,atr[i].width)
    s.andar_esquerda = True
    return False


def colisao_cima(atr,player):
    s.andar_direita = s.andar_cima = s.andar_esquerda = s.andar_baixo = True
    for i in range(0,len(atr)):
        if player.x+player.width >= atr[i].x and player.x <= atr[i].x+atr[i].width and player.y >= atr[i].y+atr[i].height:
            if player.y-350*janela.delta_time() <= atr[i].y+atr[i].height:
                s.andar_cima = False
                return True
            #else:
                 #print(i)
                 #print("Object x:",atr[i].x,"object y:", atr[i].y,"player x and y:", player.x, player.y,"object height and width:", atr[i].height,atr[i].width)
    s.andar_cima = True
    return False

def colisao_baixo(atr,player):
    s.andar_direita = s.andar_cima = s.andar_esquerda = s.andar_baixo= True
    for i in range(0,len(atr)):
        if player.x >= atr[i].x and player.x <= atr[i].x+atr[i].width and player.y+player.height < atr[i].y :
            if player.y+player.height+350*janela.delta_time() >= atr[i].y:
                s.andar_baixo = False
                return True
            #else:
                 #print(i)
                 #print("Object x:",atr[i].x,"object y:", atr[i].y,"player x and y:", player.x, player.y,"object height and width:", atr[i].height,atr[i].width)
    s.andar_baixo = True
    return False


#------MONSTROS-----#

def monster_move(monstro):
    if monstro.x > s.AUX_D[0]:
        if monstro.y-2 > s.AUX_D[1]: #teste
            monstro.x -= 1
            monstro.y -= 1
            monstro.update()
        elif monstro.y+2 < s.AUX_D[1]:
            monstro.x -= 1
            monstro.y += 1
            monstro.update()
        else:
            monstro.x -= 1
            monstro.update()

    #elif monstro.x > s.AUX_E[0]:
    #    if monstro.y+2 > s.AUX_E[1]:
    #         monstro.x += 1
    #         monstro.y -= 1
    #         monstro.update()
    #    elif monstro.y-2 < s.AUX_E[1]:
    #         monstro.x -= 1
    #         monstro.y += 1
    #         monstro.update()
    #    else:
    #         monstro.x += 1
    #         monstro.update()

    else:
        if s.AUX_E[1] < monstro.y and s.AUX_D[1] < monstro.y:
             monstro.y -= 1
             monstro.update()
        elif s.AUX_D[1] < monstro.y and s.AUX_D[1] < monstro.y:
             monstro.y += 1
             monstro.update()
        else: #dentro da tela
            if len(bomba) != 0:
                if bomba[0].x < monstro.x and bomba[0].y < monstro.y:
                    monstro.x -= 1
                    monstro.y -= 1
                elif bomba[0].x > monstro.x and bomba[0].y < monstro.y:
                    monstro.x += 1
                    monstro.y -= 1
                elif bomba[0].x > monstro.x and bomba[0].y > monstro.y:
                    monstro.x += 1
                    monstro.y += 1
                elif bomba[0].x < monstro.x and bomba[0].y > monstro.y:
                    monstro.x -= 1
                    monstro.y += 1
                monstro.update()

            elif len(construcao) != 0:
                if construcao[0].x < monstro.x and construcao[0].y < monstro.y:
                    monstro.x -= 1
                    monstro.y -= 1
                elif construcao[0].x > monstro.x and construcao[0].y < monstro.y:
                    monstro.x += 1
                    monstro.y -= 1
                elif construcao[0].x > monstro.x and construcao[0].y > monstro.y:
                    monstro.x += 1
                    monstro.y += 1
                elif construcao[0].x < monstro.x and construcao[0].y > monstro.y:
                    monstro.x -= 1
                    monstro.y += 1
                monstro.update()
            else:
                if player.x < monstro.x and player.y < monstro.y:
                    monstro.x -= 1
                    monstro.y -= 1
                elif player.x > monstro.x and player.y < monstro.y:
                    monstro.x += 1
                    monstro.y -= 1
                elif player.x > monstro.x and player.y > monstro.y:
                    monstro.x += 1
                    monstro.y += 1
                elif player.x < monstro.x and player.y > monstro.y:
                    monstro.x -= 1
                    monstro.y += 1
                monstro.update()
                if colisao_pplay.collided(monstro, player):
                    return 1

def destroi_construcao(atual, mons):
    if colisao_pplay.perfect_collision(atual, mons):
        if s.duracao_tempo == 0:
            s.duracao_tempo = 10
            #print()
            return True
        else:
            s.duracao_tempo -= 1
            return False
    return False
#--------------------CONSTRUÇÃO--------------------#

def constroi_maquina(x,y, op):
    if op == 0:
        bomba.append(spawn(s.bomba, x, y))
    if op == 1:
        aux = Animation(s.maquina, 3)
        aux.set_position(x,y)
        construcao.append(aux)
    if op == 2:
        aux = Animation(s.maquina2, 3)
        aux.set_position(x, y)
        construcao.append(aux)
    if op == 3:
        aux = Animation(s.maquina3, 3)
        aux.set_position(x, y)
        construcao.append(aux)

#Appendes do Cenario:

def draw_sprite(atr):
    for i in range(len(atr)):
        atr[i].draw()

def movimento_objet(atr, mov, orien):
    velocidade = 350 * janela.delta_time()
    if mov == 1 and orien == 'x':
        for i in range(len(atr)):
            atr[i].x += velocidade
        s.AUX_D[0] -= velocidade
        s.AUX_E[0] -= velocidade
    elif mov == -1 and orien == 'x':
        for i in range(len(atr)):
            atr[i].x -= velocidade
        s.AUX_D[0] += velocidade
        s.AUX_E[0] += velocidade
    elif mov == 1 and orien == 'y':
        for i in range(len(atr)):
            atr[i].y -= velocidade

    elif mov == -1 and orien == 'y':
        for i in range(len(atr)):
            atr[i].y += velocidade

def andar(direcao_player):
    if k.key_pressed("A") or k.key_pressed("LEFT") and s.andar_esquerda: #<-

        if not colisao_esquerda(colidiveis_esquerda, player):
            movimento_objet(bg_total, 1, 'x')
            #ANIMAR O PLAYER
            player.update()
        else:
            movimento_objet(bg_total, -1,'x')
            s.andar_esquerda = False


    elif k.key_pressed("D") or k.key_pressed("RIGHT") and s.andar_direita: #->
        if not colisao_direita(colidiveis_direita,player):
            movimento_objet(bg_total, -1, 'x')
            direcao_player = 1
            player.update()
        else:
            movimento_objet(bg_total, 1,'x')
            s.andar_direita = False

    elif k.key_pressed("S") or k.key_pressed("DOWN") and s.andar_baixo:
        if not colisao_baixo(colidiveis_baixo, player):
            movimento_objet(bg_total, 1, 'y')
            direcao_player = 0
            player.update()
        else:
            movimento_objet(bg_total,-1,'y')
            s.andar_baixo = False

    elif k.key_pressed("W") or k.key_pressed("UP") and s.andar_cima:
        if not colisao_cima(colidiveis_cima, player):
            movimento_objet(bg_total, -1, 'y')
            direcao_player = 3
            player.update()
        else:
            movimento_objet(bg_total,1,'y')
            s.andar_cima = False

def liberar_habilidade(hab):
    for i in range(len(hab)):
        if s.HABILIDADE_STATUS[hab[i]] == -1:
            print("Habilidade",hab[i],"Liberada")
            habilidade_atual[hab[i]] = trocar_sprite_hab(habilidade_atual[hab[i]], hab[i], 1)
            s.HABILIDADE_STATUS[hab[i]] = 0

def ferramentas_action(act):
    #BOMBA = MADEIRA 5 + PEDRA 5
    if act == 0 and s.quantidade_de_recursos[3] >= 10 and s.quantidade_de_recursos[4] >= 10 and s.FERRAMENTAS_OPEN[0]:
        print("FERRAMENTA 0")
        s.quantidade_de_recursos[3] -= 10
        s.quantidade_de_recursos[4] -= 10
        constroi_maquina(player.x, player.y, 0)
        s.TIME_BOMBA.append(500)

    #MAQUINA MADEIRA REFINAR = MADEIRA 30
    if act == 1 and s.quantidade_de_recursos[3] >= 30 and s.FERRAMENTAS_OPEN[1]:
        s.quantidade_de_recursos[3] -= 30
        print("FERRAMENTA 1")
        constroi_maquina(player.x, player.y, 1)
        s.TIPO_CONSTRUCAO.append(1)

    #MAQUINA PEDRA REFINAR = PEDRA 30
    if act == 2 and s.quantidade_de_recursos[4] >= 30:
        s.quantidade_de_recursos[4] -= 30
        print("FERRAMENTA 2")
        constroi_maquina(player.x, player.y, 2)
        s.TIPO_CONSTRUCAO.append(2)

    #MAQUINA M+P = MR 20 + PR 20
    if act == 3 and s.quantidade_de_recursos[5] >= 20 and s.quantidade_de_recursos[6] >= 20:
        s.quantidade_de_recursos[5] -= 20
        s.quantidade_de_recursos[6] -= 20
        print("FERRAMENTA 3")
        constroi_maquina(player.x, player.y, 3)
        s.TIPO_CONSTRUCAO.append(3)

    #RADIO = M+P 20 + MR 10 + PR 10
    if act == 4 and s.quantidade_de_recursos[5] >= 10 and s.quantidade_de_recursos[6] >= 10 and s.quantidade_de_recursos[7] >= 20:
        s.quantidade_de_recursos[5] -= 10
        s.quantidade_de_recursos[6] -= 10
        s.quantidade_de_recursos[7] -= 20
        print("FERRAMENTA 4")

def habilidade_action(act):
    if act == 0:
        if s.EXPERIENCIA >= 5:
            print("HABILIDADE 0 EFTUADO")
            s.EXPERIENCIA -= 5
            s.PODEMADEIRA = True
            return True
        else:
            return False

    elif act == 1:
        if s.EXPERIENCIA >= 15:
            print("HABILIDADE 1 EFTUADO")
            s.PODEPEDRA = True
            s.EXPERIENCIA -= 15
            return True
        else:
            return False

    elif act == 2:
        if s.EXPERIENCIA >= 15:
            print("HABILIDADE 2 EFTUADO")
            s.BOMBA = True
            s.FERRAMENTAS_OPEN[0] = True
            s.EXPERIENCIA -= 15
            return True
        else:
            return False

    elif act == 3:
        if s.EXPERIENCIA >= 15:
            print("HABILIDADE 3 EFTUADO")
            s.MAQUINA_REFINADORA_PEDRA = True
            s.FERRAMENTAS_OPEN[2] = True
            s.EXPERIENCIA -= 15
            return True
        else:
            return False

    elif act == 4:
        if s.EXPERIENCIA >= 30:
            print("HABILIDADE 4 EFTUADO")
            s.MAQUINA_REFINADORA_PM = True
            s.FERRAMENTAS_OPEN[3] = True
            s.EXPERIENCIA -= 30
            return True
        else:
            return False
    elif act == 5:
        if s.EXPERIENCIA >= 30:
            print("HABILIDADE 5 EFTUADO")
            s.MAQUINA_REFINADORA_MADEIRA = True
            s.FERRAMENTAS_OPEN[1] = True
            s.EXPERIENCIA -= 30
            return True
        else:
            return False

    elif act == 6:
        if s.EXPERIENCIA >= 30:
            print("HABILIDADE 5 EFTUADO")
            s.RADIO1 = True
            s.FERRAMENTAS_OPEN[4] = True
            s.EXPERIENCIA -= 30
            return True
        else:
            return False

    elif act == 7:
        print("HABILIDADE 7 EFTUADO")
        return True
    elif act == 8:
        print("HABILIDADE 8 EFTUADO")
        return True
    elif act == 9:
        print("HABILIDADE 9 EFTUADO")
        return True
    elif act == 10:
        print("HABILIDADE 10 EFTUADO")
        return True
    elif act == 11:
        print("HABILIDADE 11 EFTUADO")
        return True
    elif act == 12:
        print("HABILIDADE 12 EFTUADO")
        return True
    elif act == 13:
        print("HABILIDADE 13 EFTUADO")
        return True
    elif act == 14:
        print("HABILIDADE 14 EFTUADO")
        return True
    elif act == 15:
        print("HABILIDADE 15 EFTUADO")
        return True
    elif act == 16:
        print("HABILIDADE 16 EFTUADO")
        return True
    elif act == 17:
        print("HABILIDADE 17 EFTUADO")
        return True
    elif act == 18:
        print("HABILIDADE 18 EFTUADO")
        return True
    else:
        print("ZUOU")
        return False

def opcoes(bg):
    if k.key_pressed("F") and click_pause(s.CLICK_TIME_WAIT) and not s.ferramenta_press:
        print("HABILIDADES")
        if (not s.habilidade_press):
            s.habilidade_press = True
        else:
            s.habilidade_press = False

    elif k.key_pressed("E") and click_pause(s.CLICK_TIME_WAIT) and not s.habilidade_press:
        print("FERRAMENTAS")
        if (not s.ferramenta_press):
            s.ferramenta_press = True
        else:
            s.ferramenta_press = False

    elif k.key_pressed("ESC") and click_pause(s.CLICK_TIME_WAIT):
        print("sair")
        janela.close()

    if s.habilidade_press:
        habilidade.draw()
        draw_sprite(habilidade_atual)
        for l in range(len(habilidade_atual)):
            if butao_click(m, habilidade_atual[l]):  # 1
                #printar balão
                if mouse.is_button_pressed(1) and click_pause(s.CLICK_TIME_WAIT) and s.HABILIDADE_STATUS[l] == 0:
                    print("Habilidade", l,"Requisitado!")
                    if habilidade_action(l):
                        habilidade_atual[l] = trocar_sprite_hab(habilidade_atual[l], l, 0)
                        s.HABILIDADE_STATUS[l] = 1
                        liberar_habilidade(s.HABILIDADE_LIBERAR[l])
                        print(s.HABILIDADE_STATUS)

    if s.ferramenta_press:
        ferramenta.draw()
        if s.FPAGINA1:
            draw_sprite(ferramenta_pagina_1)
            ferramenta_button[0].draw()
            for i in range(len(ferramenta_pagina_1)):
                if butao_click(m, ferramenta_pagina_1[i]):
                    if mouse.is_button_pressed(1) and click_pause(s.CLICK_TIME_WAIT) and s.FERRAMENTAS_OPEN:
                        print("Ferramenta", i, "requisitado!")
                        ferramentas_action(i)
            if butao_click(m, ferramenta_button[0]):
                if mouse.is_button_pressed(1) and click_pause(s.CLICK_TIME_WAIT):
                    s.FPAGINA1 = False
                    s.FPAGINA2 = True

        if s.FPAGINA2:
            draw_sprite(ferramenta_pagina_2)
            ferramenta_button[1].draw()
            for t in range(len(ferramenta_pagina_2)):
                if butao_click(m, ferramenta_pagina_2[t]):
                    if mouse.is_button_pressed(1) and click_pause(s.CLICK_TIME_WAIT) and s.FERRAMENTAS_OPEN:
                        print("Ferramenta", t+3, "requisitado!")
                        ferramentas_action(t+3)

            if butao_click(m, ferramenta_button[1]):
                if mouse.is_button_pressed(1) and click_pause(s.CLICK_TIME_WAIT):
                    s.FPAGINA1 = True
                    s.FPAGINA2 = False

def update(bg):
    exp_time()
    janela.set_title(str(janela.delta_time()))
    andar(direcao_player)
    player.draw()
    opcoes(bg)
    janela.update()

frame = 0

def remove_construcao(obj):
    construcao.pop(obj)
    s.TIPO_CONSTRUCAO.pop(obj)

def vida_ciclo():
    if not s.VIDA_LOOK:
        s.VIDA_TIME -= 1

    if s.VIDA_TIME == 0:
        s.VIDA_LOOK = True
        s.VIDA_TIME = 30

def bomba_ciclo(b):
    for i in range(len(b)):
        if s.TIME_BOMBA[i] == 0:
            s.TIME_BOMBA.pop(i)
            b.pop(i)
            break
        else:
            s.TIME_BOMBA[i] -= 1

def reset():
    print("NÃO IMPLEMENTADO AINDA")

while True:
    #print("Exp:"+str(s.EXPERIENCIA))
    frame += 1
    click_call()
    vida_ciclo()
    background_da_janela.draw()
    m = mouse.get_position()

    if s.VIDA == 0:
        s.MENU = True
        s.GAME = False
        s.VIDA = 5
        reset()

    if s.GAME:
        bg_total = nao_colidiveis + colidiveis + construcao + monstros + bomba + radio
        draw_sprite(bg_total)
        show_HP(HP)
        spawn_madeira(arvore_spawn)
        spawn_pedra(pedra_de_5_lados)

        if frame > 1001:
            frame = 0
            aux = Animation(s.aranha, 3)
            aux.set_total_duration(1000)
            aux.set_position(monster_spawn.x + monster_spawn.width / 2, monster_spawn.y + monster_spawn.height / 2)
            monstros.append(aux)

        show_hud(s.quantidade_de_recursos[4], s.quantidade_de_recursos[3], s.quantidade_de_recursos[0], s.quantidade_de_recursos[2], s.quantidade_de_recursos[1],s.quantidade_de_recursos[5],s.quantidade_de_recursos[6],s.quantidade_de_recursos[7])

        draw_sprite(construcao)

        for i in range(len(construcao)):
            try:
                if butao_click(m, construcao[i]):
                    if mouse.is_button_pressed(1) and click_pause(s.CLICK_TIME_WAIT):
                        if s.TIPO_CONSTRUCAO[i] == 1:
                            s.quantidade_de_recursos[3] -= 5
                            s.quantidade_de_recursos[5] += 1

                        elif s.TIPO_CONSTRUCAO[i] == 2:
                            s.quantidade_de_recursos[4] -= 5
                            s.quantidade_de_recursos[6] += 1

                        elif s.TIPO_CONSTRUCAO[i] == 3:
                            s.quantidade_de_recursos[6] -= 5
                            s.quantidade_de_recursos[5] -= 5
                            s.quantidade_de_recursos[7] += 1
            except:
                print("PPLAY é uma MERDA")
                # print(i)
                # print(construcao[i])
                # print(len(construcao))
                # print(construcao)

            for j in range(len(monstros)):
                try:
                    if destroi_construcao(construcao[i], monstros[j]):
                        remove_construcao(i)
                except:
                    print("PPLAY É UMA MERDA")

        if len(bomba) != 0:
            bomba_ciclo(bomba)

        draw_sprite(monstros)

        for i in range(len(monstros)):
            monster_move(monstros[i])
            #print(i, monstros[i].x, monstros[i].y)


        if len(monstros) != 0:
            if colisao_pplay.collided(monstros[0], player) and s.VIDA_LOOK:
                s.VIDA_LOOK = False
                s.VIDA -= 1
            if len(bomba) != 0:
                for h in range(len(monstros)):
                    try:
                        if colisao_pplay.collided(monstros[h], bomba[0]):
                            try:
                                monstros.pop(0)
                            except:
                                print("PPLAY É UMA MERDA")
                    except:
                        print("PPLAY É UMA MERDA")

        #print(s.quantidade_de_recursos)
        #print(s.AUX_D, s.AUX_E)
        update(bg_total)

    if s.MENU:
        nome.draw()
        butao_inicar.draw()
        if butao_click(m, butao_inicar):
            if mouse.is_button_pressed(1) and click_pause(s.CLICK_TIME_WAIT):
                s.GAME = True
                s.MENU = False
        janela.update()
