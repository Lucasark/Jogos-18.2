
class Medalha():
    def __init__(self, n, o, p, b):
        self.nome = n
        self.ouro = int(o)
        self.prata = int(p)
        self.bronze = int(b)

#implementar o reverse False

N = int(input())
quadro = []
for i in range(N):
    nome, O, P, B = map(str, input().split())
    quadro.append(Medalha(nome, O, P, B))

q_final = sorted(quadro, key=lambda medalha : (medalha.ouro, medalha.prata, medalha.bronze, medalha.nome), reverse=True)

#print(q_final)
for i in range(N):
    print(q_final[i].nome, q_final[i].ouro, q_final[i].prata, q_final[i].bronze)

def getOuro(vec):
    return vec

N = int(input())
quadro = []
for i in range(N):
    nome, O, P, B = map(str, input().split())
    aux_quadro = []
    aux_quadro.append(nome)
    aux_quadro.append(int(O))
    aux_quadro.append(int(P))
    aux_quadro.append(int(B))
    quadro.append(aux_quadro)

quadro_aux = sorted(quadro, key =lambda quadro: (quadro[1], quadro[2], quadro[3]), reverse=True)

for i in range(N):
    print(quadro_aux[i][0], quadro_aux[i][1], quadro_aux[i][2], quadro_aux[i][3])