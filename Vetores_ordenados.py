import __main__

import numpy as np

class vetornaoordenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

#Notação = O(n)
    def mostrar(self):
        if self.ultima_posicao == -1:
            print("O vetor esta vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print("Posição do vetor:", i, " Número na posição:", self.valores[i])

#Notação = O(1) ou O(n) - Função constante
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print("Vetor com capacidade cheia")
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

#Notação = O(n)
    def pesquisa(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return - 1
    
    def exclui(self, valor):
        posicao = self.pesquisa(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]

if __name__ == '__main__':

    vetor = vetornaoordenado(5)
    vetor.insere(1)
    vetor.insere(2)
    vetor.insere(3)
    vetor.mostrar()

    print("Procurando valores...")
    print(vetor.pesquisa(3))

    vetor.exclui(2)