class Inimigo():
    imagem = ""
    vida = 100
    x = 0
    y = 0
    dano = 0

    def __init__(self, imagem, x , y, dano):
        self.x = x
        self.y = y
        self.imagem = imagem
        self.vida = 100
        self.dano = dano

    def perdeVida(self, remove):
        self.vida -= remove

    def moveX(self, x):
        self.x += x

    def moveY(self, y):
        self.y += y
