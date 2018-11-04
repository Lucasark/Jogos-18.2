import pygame

#Titulo
TITLE = 'Teste de Game'

#Dificuldade
DIFICULDADE_GAME = 1

#Tela
# Suporte no 16:9 -> 720,480 - 1280,720
WIDTH = 720
HEIGHT = 480

#PNG

#MENU
bg = 'bg_praia.png'
arvore = ['arvore1.png', 'arvore2.png', 'arvore3.png']
pedra = 'pedra_de_5_lados.png'
borderEdge = ['bloqueio_lateral.png', 'bloqueio_superior.png', 'agua_praia.png', 'grama_praia.png']
cenario = ['monster_spawn.png', 'arvore1.png', 'arvore2.png', 'arvore3.png']
player = 'tile001.png'
background_do_background = 'fundo_forcado.png'

#Buttoes
#menus = ['iniciar.png', 'placar.png', 'dificuldade.png', 'sair.png']
#menusP = ['iniciarP.png', 'placarP.png', 'dificuldadeP.png', 'sairP.png']
#DIF = ['D1.png','D2.png','D3.png']
#DIFP = ['D1P.png','D2P.png','D3P.png']
#DIFS = ['D1S.png','D2S.png','D3S.png']
#VOLTAR = 'voltar.png'
#VOLTARP = 'voltarP.png'

#PLAYER SETTINGS:
andar_cima = True
andar_baixo = True
andar_esquerda = True
andar_direita = True

#CLICK:
CLICK_TIME = 0
CLICK_TIME_WAIT = 30
CLICK_ANDAR_WAIT = 20
CLICK_SIGNAL = True #True -> Pode clickar -- False-> Nao pode clickar


#PLAYER SETTINGS:
