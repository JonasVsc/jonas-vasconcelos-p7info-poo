class Pilha():

    def __init__(self):
        self.pilha = []

    def empilhar(self, elemento):
        self.pilha.append(elemento)

    def desempilhar(self):
        self.pilha.pop(len(self.pilha) - 1)

    def mostrar_pilha(self):
        return self.pilha

pilha = Pilha()

pilha.empilhar(32)
pilha.empilhar(23)
pilha.empilhar(66)
pilha.desempilhar()
print(pilha.mostrar_pilha())

