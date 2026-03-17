import __main__

import numpy as np

class vetorordenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

#Notação = O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print("O vetor esta vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print("Posição do vetor:", i, " Número na posição:", self.valores[i])


    def insere(self, valor):
        if self.ultima_posicao == self.capacidade -1:
            print("Capacidade cheia")
            return
        
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
                
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[ x + 1 ] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

if __name__ == '__main__':

    vetor = vetorordenado(6)
    vetor.insere(6)
    vetor.insere(4)
    vetor.insere(3)
    vetor.insere(5)
    vetor.insere(1)
    vetor.insere(8)
    vetor.imprime()
 
