from PPlay.window import *
from PPlay.collision import *
from PPlay.gameimage import *
import settings as s
#import options as o
#import classes as c

#janela
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
nao_colidiveis = [fundo, grama, monster_spawn]
colidiveis_esq = [bloqueio2]
colidiveis_dir = [bloqueio3]
colidiveis_cima = [bloqueio1]
colidiveis_baixo = [agua]
colidiveis = [arvore_1, arvore_2, arvore_3, arvore_4, pedra_de_5_lados]
bg_total = nao_colidiveis + colidiveis + colidiveis_cima + colidiveis_baixo + colidiveis_dir + colidiveis_esq

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
    andar()
    player.draw()
    opcoes()
    janela.update()

while True:
    click_call()
    background_da_janela.draw()
    draw_sprite(bg_total)
    #print("E: ",s.andar_esquerda,"D: ",s.andar_direita,"C: ",s.andar_cima,"B: ",s.andar_baixo)
    update()
