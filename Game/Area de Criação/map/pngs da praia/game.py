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



#TILE - o uso do numero 32, graças a sua motherfucking lógica de uso de tiles ta sendo bem conveniente, então pro professor não ficar "ui ta usando número absoluto" eu to declarando uma variavel
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


#gambiarra_foda:
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

#----RECURSOS----#

def spawn(png,x,y):
    imagem = GameImage(png)
    imagem.set_position(x,y)
    return imagem




def vetor_de_madeira(arvore,tempo):
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
      if not colisao_pplay.collided(player,madeiras[i]) and s.estado_madeira[i]:
        madeiras[i].draw()
      elif colisao_pplay.collided(player,madeiras[i]) and s.estado_madeira[i]:
          s.quantidade_de_recursos[3] += 1
          s.estado_madeira[i] = False
      if not s.estado_madeira[i] and tempo > s.loops:
          s.estado_madeira[i] = True



#-------------------------------------------------HUD--------------------------------------#
HP = Animation(s.hud[0],11)
HP.set_total_duration(1000)
HP.set_position(0,0)

quantidade_HUD_madeira = Sprite(s.hud[1])
quantidade_HUD_madeira.set_position(HP.x+quantidade_HUD_madeira.width,HP.y+HP.height+tile-(quantidade_HUD_madeira.height/2))

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

HUD_materials = [quantidade_HUD_ouro,quantidade_HUD_madeira,quantidade_HUD_pedra_coletavel,madeira_HUD,ouro_HUD,pedra_coletavel_HUD,ferro_HUD,quantidade_HUD_ferro,quantidade_HUD_cobre,cobre_HUD]


#mostrar o HUD ao teclar 0
def show_hud(pedra,madeira,ferro,cobre,ouro):
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


#Habilidades:
"""

[-1]    ->  Bloqueados: Imagem preta [SN1], e não está disponivel para compra
[1]     ->  Comprados: Imagem Cinza [CI] , já foi adquirido
[0]     ->  Liberados: Imagem Colorida [CO], liberado para compra

"""
habilidade_atual = [GameImage(s.COH[0]), GameImage(s.SNH[1]), GameImage(s.SNH[2]), GameImage(s.SNH[4]), GameImage(s.SNH[5]), GameImage(s.SNH[6]),
                    GameImage(s.SNH[7]), GameImage(s.SNH[8]), GameImage(s.SNH[9]), GameImage(s.SNH[10]), GameImage(s.SNH[11]), GameImage(s.SNH[12]),
                    GameImage(s.SNH[13]), GameImage(s.SNH[14]), GameImage(s.SNH[15]), GameImage(s.SNH[16]), GameImage(s.SNH[17]), GameImage(s.SNH[18])]

#Appendes do BG:
nao_colidiveis = [fundo, grama,monster_spawn]
colidiveis = [bloqueio1, bloqueio2, bloqueio3,bloqueio4,arvore_1,arvore_2,agua,arvore_3,arvore_4,pedra_de_5_lados,bloco_esquerda,bloco_direita,arvore_spawn]
colidiveis_esquerda = [arvore_1,arvore_2,pedra_de_5_lados,bloqueio2,bloco_esquerda,bloqueio1,arvore_spawn]
colidiveis_baixo =[agua,pedra_de_5_lados,arvore_spawn]
colidiveis_direita =[arvore_3,arvore_4,bloqueio3,pedra_de_5_lados,bloco_direita,bloqueio4,arvore_spawn]
colidiveis_cima =[pedra_de_5_lados,bloqueio1,arvore_2,arvore_4,bloqueio4,arvore_spawn]
bg_total = nao_colidiveis + colidiveis

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
#habilidade_atual[8].set_position()
#habilidade_atual[9].set_position()
#habilidade_atual[10].set_position()
#habilidade_atual[11].set_position()
#habilidade_atual[12].set_position()
habilidade_atual[13].set_position(pos_relativo_w(habilidade_atual[6], 32), habilidade_atual[6].y)
habilidade_atual[14].set_position(habilidade_atual[6].x + (habilidade_atual[6].width)/2, habilidade_atual[7].y + (habilidade_atual[7].height)/2)
habilidade_atual[15].set_position(habilidade_atual[7].x, pos_relativo_h(habilidade_atual[7], 32))
#habilidade_atual[16].set_position()
#habilidade_atual[17].set_position()
#habilidade_atual[18].set_position()

#FERRAMENTAS POSIÇÃO

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

def trocar_sprite_hab(old, pos ,op):
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

def colisao_direita(atr,player):
    s.andar_direita = s.andar_cima = s.andar_esquerda = s.andar_baixo = True
    for i in range(0,len(atr)):
        if (player.y >= atr[i].y or player.y+player.height > atr[i].y) and  player.y < atr[i].y+atr[i].height and atr[i].x-player.x >=0:
            if player.x+player.width+350*janela.delta_time() >= atr[i].x:
                s.andar_direita = False
                return True
            else:
                 print(i)
                 print("Object x:",atr[i].x,"object y:", atr[i].y,"player x and y:", player.x, player.y,"object height and width:", atr[i].height,atr[i].width)
    s.andar_direita = True
    return False

def colisao_esquerda(atr,player):
    s.andar_direita = s.andar_cima = s.andar_esquerda = s.andar_baixo = True
    for i in range(len(atr)):
        if (player.y >= atr[i].y or player.y+player.height > atr[i].y) and player.y <= atr[i].y + atr[i].height: # Player está entre o objeto(eixo vertical)
            if atr[i].x+atr[i].width <= player.x: # o ponto mais a direita(que é o que pode colidir com player) é menor que a posição atual de player(o que deve acontecer, porque se isso da false é pq o objeto está a direita de player,logo, não pode colidir pela esquerda)
                if player.x-350*janela.delta_time() <= atr[i].x+atr[i].width:
                    s.andar_esquerda = False
                    print(atr[i].x,atr[i].y,player.x+player.width,player.y,atr[i].height)
                    return True
            else:
                 print(i)
                 print("Object x:",atr[i].x,"object y:", atr[i].y,"player x and y:", player.x, player.y,"object height and width:", atr[i].height,atr[i].width)
    s.andar_esquerda = True
    return False


def colisao_cima(atr,player):
    s.andar_direita = s.andar_cima = s.andar_esquerda = s.andar_baixo = True
    for i in range(0,len(atr)):
        if player.x+player.width >= atr[i].x and player.x <= atr[i].x+atr[i].width and player.y >= atr[i].y+atr[i].height:
            if player.y-350*janela.delta_time() <= atr[i].y+atr[i].height:
                s.andar_cima = False
                return True
            else:
                 print(i)
                 print("Object x:",atr[i].x,"object y:", atr[i].y,"player x and y:", player.x, player.y,"object height and width:", atr[i].height,atr[i].width)
    s.andar_cima = True
    return False

def colisao_baixo(atr,player):
    s.andar_direita = s.andar_cima = s.andar_esquerda = s.andar_baixo= True
    for i in range(0,len(atr)):
        if player.x >= atr[i].x and player.x <= atr[i].x+atr[i].width and player.y+player.height < atr[i].y :
            if player.y+player.height+350*janela.delta_time() >= atr[i].y:
                s.andar_baixo = False
                return True
            else:
                 print(i)
                 print("Object x:",atr[i].x,"object y:", atr[i].y,"player x and y:", player.x, player.y,"object height and width:", atr[i].height,atr[i].width)
    s.andar_baixo = True
    return False




#------MONSTROS-----#

def monster_move(constru, monstro,player):
    if s.tem_construcao:
        if constru.x < monstro.x:
            if not colisao_esquerda(colidiveis_esquerda,monstro):
                monstro.x -= 1
            else:
                monstro.y += 1
        elif constru.x > monstro.x:
            if not colisao_direita(colidiveis_direita,monstro):
                monstro.x += 1
            else:
                monstro.y += 1
        else:
            if constru.y < monstro.y:
                monstro.y -= 1
            elif constru.y > monstro.y:
                monstro.y += 1
            else:
                return True
    else:
        if player.x < monstro.x:
            if not colisao_esquerda(colidiveis_esquerda,monstro):
                monstro.x -= 1
            else:
                monstro.y += 1
        elif player.x > monstro.x:
            if not colisao_direita(colidiveis_direita,monstro):
                monstro.x += 1
            else:
                monstro.y += 1
        else:
            if player.y < monstro.y:
                monstro.y -= 1
            elif player.y > monstro.y:
                monstro.y += 1


def destroi_construcao(atual):
    if monster_move(s.construcao,s.monstro[atual]):
        s.duracao_tempo -= 1
        if s.duracao_tempo == 0:
            s.tem_construcao = False

#--------------------CONSTRUÇÃO--------------------#

def constroi_maquina(x,y):
    if s.quantidade_de_recursos[3] >= 10:
        s.quantidade_de_recursos[3] -=10
        s.tem_construcao = True
        s.construcao = spawn(s.maquina,a,b)






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

def andar(direcao_player):
    if k.key_pressed("A") or k.key_pressed("LEFT") and s.andar_esquerda: #<-

        '''
        if (fundo.x + player.x >= 0):
            player.x -= 1
        else:
        '''
        if not colisao_esquerda(colidiveis_esquerda,player):
            movimento_objet(bg_total, 1, 'x')
            direcao_player = 2
            player.update()
        else:
            movimento_objet(bg_total, -1,'x')
            s.andar_esquerda = False


    elif k.key_pressed("D") or k.key_pressed("RIGHT") and s.andar_direita: #->
        '''
        if (fundo.x + player.x <= 0 ):
            player.x += 1
        else:
        '''
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

def habilidade_action(act):
    if act == 0:
        print("HABILIDADE 0 EFTUADO")
    elif act == 1:
        print("HABILIDADE 1 EFTUADO")
    elif act == 2:
        print("HABILIDADE 2 EFTUADO")
    elif act == 3:
        print("HABILIDADE 3 EFTUADO")
    elif act == 4:
        print("HABILIDADE 4 EFTUADO")
    elif act == 5:
        print("HABILIDADE 5 EFTUADO")
    elif act == 6:
        print("HABILIDADE 6 EFTUADO")
    elif act == 7:
        print("HABILIDADE 7 EFTUADO")
    elif act == 8:
        print("HABILIDADE 8 EFTUADO")
    elif act == 9:
        print("HABILIDADE 9 EFTUADO")
    elif act == 10:
        print("HABILIDADE 10 EFTUADO")
    elif act == 11:
        print("HABILIDADE 11 EFTUADO")
    elif act == 12:
        print("HABILIDADE 12 EFTUADO")
    elif act == 13:
        print("HABILIDADE 13 EFTUADO")
    elif act == 14:
        print("HABILIDADE 14 EFTUADO")
    elif act == 15:
        print("HABILIDADE 15 EFTUADO")
    elif act == 16:
        print("HABILIDADE 16 EFTUADO")
    elif act == 17:
        print("HABILIDADE 17 EFTUADO")
    elif act == 18:
        print("HABILIDADE 18 EFTUADO")
    else:
        print("ZUOU")

def opcoes():
    m = mouse.get_position()
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
        for i in range(len(habilidade_atual)):
            if butao_click(m, habilidade_atual[i]):  # 1
                #printar balão
                if mouse.is_button_pressed(1) and click_pause(s.CLICK_TIME_WAIT) and s.HABILIDADE_STATUS[i] == 0:
                    print("Habilidade", i,"Desloqueada")
                    habilidade_action(i)
                    habilidade_atual[i] = trocar_sprite_hab(habilidade_atual[i], i, 0)
                    s.HABILIDADE_STATUS[i] = -1
                    liberar_habilidade(s.HABILIDADE_LIBERAR[i])
                    print(s.HABILIDADE_STATUS)

    if s.ferramenta_press:
        ferramenta.draw()

#print(player.x, ":X - Y:", player.y,"     ",s.WIDTH,":S.W  -  F.W",fundo.width,"         ",fundo.x,":f.x   -  f.y",fundo.y)

def update():
    janela.set_title(str(janela.delta_time()))
    andar(direcao_player)
    player.draw()
    opcoes()
    janela.update()

#frame é nossa unidade de tempo, ela define quando damos spawn nas coisas
frame = 0
while True:
    frame += 1
    click_call()
    background_da_janela.draw()
    draw_sprite(bg_total)
    vetor_de_madeira(arvore_spawn, frame)
    if frame > 1001:
        frame = 0
        s.monstro.append(
            spawn('aranha.png', monster_spawn.x + monster_spawn.width / 2, monster_spawn.y + monster_spawn.height / 2))
        s.tem_monstro.append(True)

    HP.draw()
    show_hud(10, s.quantidade_de_recursos[3], 20, 30, 40)

    if s.tem_construcao:
        s.construcao.draw()


    if k.key_pressed("B"):
        constroi_maquina(arvore_spawn.x+tile,arvore_spawn.y+tile)

    for i in range(len(s.monstro)):
        if s.tem_monstro[i]:
            monster_move(arvore_1, s.monstro[i], player)
            s.monstro[i].draw()
    # print("E: ",s.andar_esquerda,"D: ",s.andar_direita,"C: ",s.andar_cima,"B: ",s.andar_baixo)

    update()
