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
player = ['personagem_baixo.png','personagem_direita.png','personagem_esquerda.png','personagem_cima.png']
andar_cima = True
andar_baixo = True
andar_esquerda = True
andar_direita = True

#direção_player define qual animação deveria ser usada no movimento
direcao_player = 0

#CLICK:
CLICK_TIME = 0
CLICK_TIME_WAIT = 30
CLICK_ANDAR_WAIT = 20
CLICK_SIGNAL = True #True -> Pode clickar -- False-> Nao pode clickar

#PLAYER PARAMETROS:
VIDA = 0
EXPERIENCIA = 0
TIME_TO_EXPERIENCIA = 0


#------ISAAC-----#

#-------------------------MATERIAIS---------------------------------------#

recursos = ['ferro.png','ouro.png','cobre.png','madeira.png','pedra_coletavel.png']

quantidade_de_recursos = [0,0,0,0,0]


estado_madeira = [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]
loops = 2000



#---cantinho exclusivo da gambiarra----#

gambiarra_bloco = "player_rect.png"

#--------------------HUD--------------------#

hud =['hud_hp.png','hud_X.png','madeira_HUD.png','ouro_HUD.png','ferro_HUD.png','pedra_coletavel_HUD.png','cobre_HUD.png']


#TEXTO
text =[(255,255,255),16,"Space Mono"]
# text = [ cor, tamanho da fonte, tipo da fonte ]


#-----------------MONSTRO---------------#

duracao_tempo = 2000


monstro = []
tem_monstro = []
tem_construcao = []

#-----------------MÁQUINA---------------#

maquina = 'alavanca2.png'


