class Produto:
    def __init__(self, name, preco, categoria):
        self.id = None
        self.nome = name
        self.preco = preco
        self.cat = categoria
        
    def imprimir(self):
        print("---------------------------")
        print("Nome: ", self.nome)
        print("Preco: ", self.preco)
        print("Cat: ", self.cat.nome)