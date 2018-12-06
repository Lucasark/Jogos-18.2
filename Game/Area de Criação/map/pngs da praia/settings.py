import pygame

#Titulo
TITLE = 'Teste de Game'

#Dificuldade
DIFICULDADE_GAME = 1


#Tela
# Suporte no 16:9 -> 720,480 - 1280,720
WIDTH = 900
HEIGHT = 700

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

#Bloqueado
SNH = ['SNH0.png', 'SNH1.png', 'SNH2.png', 'SNH3.png', 'SNH4.png', 'SNH5.png', 'SNH6.png',
       'SNHD.png', 'SNHD.png', 'SNHD.png', 'SNHD.png', 'SNHD.png', 'SNHD.png', 'SNHD.png',
       'SNHD.png', 'SNHD.png', 'SNHD.png', 'SNHD.png', 'SNHD.png', 'SNHD.png', 'SNHD.png']
#Comprados
CIH = ['CIH0.png', 'CIH1.png', 'CIH2.png', 'CIH3.png', 'CIH4.png', 'CIH5.png', 'CIH6.png',
       'CIHD.png', 'CIHD.png', 'CIHD.png', 'CIHD.png', 'CIHD.png', 'CIHD.png', 'CIHD.png',
       'CIHD.png', 'CIHD.png', 'CIHD.png', 'CIHD.png', 'CIHD.png', 'CIHD.png', 'CIHD.png']

#Livres
COH = ['COH0.png', 'COH1.png', 'COH2.png', 'COH3.png', 'COH4.png', 'COH5.png', 'COH6.png',
       'COHD.png', 'COHD.png', 'COHD.png', 'COHD.png', 'COHD.png', 'COHD.png', 'COHD.png',
       'COHD.png', 'COHD.png', 'COHD.png', 'COHD.png', 'COHD.png', 'COHD.png', 'COHD.png']

HABILIDADE_STATUS = [0, -1, -1, -1, -1, -1,
                     -1, -1, -1, -1, -1, -1,
                     -1, -1, -1, -1, -1, -1, -1]

HABILIDADE_LIBERAR = [[1,2,3],[4,5],[6,7],[8,9],[10,11],[11,12],[13,14],[14,15],[16,17],[17,18],
                      [],[],[],[],[],[],[],[],[]]

#HABILIDADE_TURN = [False, False, False, False]


#FERRAMENTAS:
bg_ferramenta = "bg_ferramentas.png"
ferramenta_press = False
FERRAMENTAS_OPEN = [False,False,False,False,False]
#0 -> BOMBA
#1 -> REFINADOR 1 (MADEIRA LASCADA)
#2 -> REFINADOR 2 (PEDRA LASCADA)
#3 -> REFINADOR 3 (MADEIRA L. + PEDRA L.)
#4 -> RADIO LVL1
FERRAMENTAS_BUTTON = ['F1.png', 'F2.png', 'F3.png', 'F4.png', 'F5.png']
#----PAGINA-1-----#
FPAGINA1 = True
#----PAGINA-2-----#
FPAGINA2 = False
FERRRAMENTA_JANELA = ['FIR.png','FVOLTAR.png']

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
VIDA = 5
VIDA_LOOK = False
VIDA_TIME = 30
EXPERIENCIA = 100
TIME_TO_EXPERIENCIA = 50
LOOK_EXPERIENCIA = 50 #pode multiplar pela dificuldade

#-------------------------MATERIAIS---------------------------------------#
PODEMADEIRA = False
PODEPEDRA = False
PODEFERRO = False

recursos = ['ferro.png','ouro.png','cobre.png','madeira.png','pedra_coletavel.png']
#0-> FERRO
#1-> OURO
#2-> COBRE
#3-> MADEIRA
#4-> PEDRA
#5-> MADEIRA_REFINADA
#6-> PEDRA_REFINADA
#7-> P+M
quantidade_de_recursos = [0,0,0,100000,200,200,200,200]


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
MAQUINAS = []
duracao_tempo = 10

monstro = []
tem_monstro = []
tem_construcao = []

aranha = 'bee.png'
ARANHA = []
POS_ARANHA = []
TIME_ARANHA = []
TIME_ALL_ARANHA = 20
LOCK_ARANHA = []

#-----------------MÁQUINA---------------#
TIPO_CONSTRUCAO = []

maquina = 'alavanca2.png'
MAQUINA_REFINADORA_MADEIRA = False
POS_MADEIRA = []
TIME_MADEIRA = []
TIME_ALL_MADEIRA = 20
LOCK_MADEIRA = []

maquina2 = 'CIH2.png'
MAQUINA_REFINADORA_PEDRA = False
POS_PEDRA = []
TIME_PEDRA = []
TIME_ALL_PEDRA = 20
LOCK_PEDRA = []

maquina3 = 'CIH2.png'
MAQUINA_REFINADORA_PM = False
POS_MD = []
TIME_PM = []
TIME_ALL_PM = 20
LOCK_PM = []

#-----------------OBEJTOS-------------#
bomba = 'bomba.png'
BOMBA = False
POS_BOMBA = []
TIME_BOMBA = []
TIME_ALL_BOMBA = 100
LOCK_BOMBA = []

radio1 = 'radio.png'
RADIO1 = False

#---------------TELA-----------#
INICIAR = 'iniciar.png'
NOME = 'Nome.png'
MENU = True
GAME = False