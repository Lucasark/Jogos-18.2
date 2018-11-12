import settings as s
from PPlay.gameimage import *

#----------Funções Auxiliar-----


#PNG:

#----------HABILIDADES----------

"""

[-1]    ->  Bloqueados: Imagem preta [SN1], e não está disponivel para compra
[1]     ->  Comprados: Imagem Cinza [CI] , já foi adquirido
[0]     ->  Liberados: Imagem Colorida [CO], liberado para compra

"""

#SNH = [GameImage(s.SNH[0]), GameImage(s.SNH[1]), GameImage(s.SNH[2]), GameImage(s.SNH[3])]
#CIH = [GameImage(s.CIH[0]), GameImage(s.CIH[1]), GameImage(s.CIH[2]), GameImage(s.CIH[3])]
#COH = [GameImage(s.COH[0]), GameImage(s.COH[1]), GameImage(s.COH[2]), GameImage(s.COH[3])]
SNH = [GameImage(s.SNH),GameImage(s.SNH),GameImage(s.SNH),GameImage(s.SNH)]
#---0 -> Iniciar o Game

#H0 = Habilidade(0, SNH[0], 32, 32)
SNH[0].set_position(32, 32)
H0 = SNH[0]
def hab_0():
    print("0")
#---1 ->
#H1 = Habilidade(0, SNH[1], 64, 64)
SNH[1].set_position(32, 32)
H1 = SNH[1]
def hab_1():
    print("1")

#---2 ->
#H2 = Habilidade(0, SNH[2], 128, 128)
SNH[2].set_position(128, 128)
H2 = SNH[2]

def hab_2():
    print("2")

#---3 ->
#H3 = Habilidade(0, SNH[3], 256, 256)
SNH[3].set_position(256, 256)
H3 = SNH[3]
def hab_3():
    print("3")

#---4 ->


#---5 ->

#---6 ->

#---7 ->

HABILIDADES = [H0, H1, H2, H3]

def printarHabs():
    for i in range(len(HABILIDADES)-1):
        HABILIDADES[i].draw()

#----------FERRAMENTAS----------

