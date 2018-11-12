import pygame

#Titulo
TITLE = 'Teste de Game'

#Dificuldade
DIFICULDADE_GAME = 1


#Tela
# Suporte no 16:9 -> 720,480 - 1280,720
WIDTH = 1280
HEIGHT = 720

#PNG

#MENU

#CENARIO 1:
bg = 'bg_praia.png'
arvore = ['arvore1.png', 'arvore2.png', 'arvore3.png']
pedra = 'pedra_de_5_lados.png'
borderEdge = ['bloqueio_lateral.png', 'bloqueio_superior.png', 'agua_praia.png', 'grama_praia.png']
cenario = ['monster_spawn.png', 'arvore1.png', 'arvore2.png', 'arvore3.png']
background_do_background = 'fundo_forcado.png'

#CENARIO 2:

#CENARIO 3:

#HABILIDAEDS:
bg_habilidades = "bg_habilidades.png"
habilidade_press = False
#SNH = 'SNH1.png'

#Bloqueado
SNH = ['SNH1.png', 'SNH1.png', 'SNH1.png', 'SNH1.png', 'SNH1.png', 'SNH1.png', 'SNH1.png',
       'SNH1.png', 'SNH1.png', 'SNH1.png', 'SNH1.png', 'SNH1.png', 'SNH1.png', 'SNH1.png',
       'SNH1.png', 'SNH1.png', 'SNH1.png', 'SNH1.png', 'SNH1.png', 'SNH1.png', 'SNH1.png']
#Comprados
CIH = ['CIH1.png', 'CIH1.png', 'CIH1.png', 'CIH1.png', 'CIH1.png', 'CIH1.png', 'CIH1.png',
       'CIH1.png', 'CIH1.png', 'CIH1.png', 'CIH1.png', 'CIH1.png', 'CIH1.png', 'CIH1.png',
       'CIH1.png', 'CIH1.png', 'CIH1.png', 'CIH1.png', 'CIH1.png', 'CIH1.png', 'CIH1.png']

#Livres
COH = ['COH1.png', 'COH1.png', 'COH1.png', 'COH1.png', 'COH1.png', 'COH1.png', 'COH1.png',
       'COH1.png', 'COH1.png', 'COH1.png', 'COH1.png', 'COH1.png', 'COH1.png', 'COH1.png',
       'COH1.png', 'COH1.png', 'COH1.png', 'COH1.png', 'COH1.png', 'COH1.png', 'COH1.png']

HABILIDADE_STATUS = [0, -1, -1, -1, -1, -1,
                     -1, -1, -1, -1, -1, -1,
                     -1, -1, -1, -1, -1, -1]

HABILIDADE_LIBERAR = [[1,2,3],[4,5],[6,7],[8,9],[10,11],[11,12],[13,14],[14,15],[16,17],[17,18],
                      [],[],[],[],[],[],[],[],[]]

HABILIDADE_TURN = [False, False, False, False]


#FERRAMENTAS:
bg_ferramenta = "bg_habilidades.png"
ferramenta_press = False


#Buttoes
#menus = ['iniciar.png', 'placar.png', 'dificuldade.png', 'sair.png']
#menusP = ['iniciarP.png', 'placarP.png', 'dificuldadeP.png', 'sairP.png']
#DIF = ['D1.png','D2.png','D3.png']
#DIFP = ['D1P.png','D2P.png','D3P.png']
#DIFS = ['D1S.png','D2S.png','D3S.png']
#VOLTAR = 'voltar.png'
#VOLTARP = 'voltarP.png'

#PLAYER SETTINGS:
player = 'tile001.png'
andar_cima = True
andar_baixo = True
andar_esquerda = True
andar_direita = True

#CLICK:
CLICK_TIME = 0
CLICK_TIME_WAIT = 30
CLICK_ANDAR_WAIT = 20
CLICK_SIGNAL = True #True -> Pode clickar -- False-> Nao pode clickar

#PLAYER PARAMETROS:
VIDA = 0
EXPERIENCIA = 0
TIME_TO_EXPERIENCIA = 0

