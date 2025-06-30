from abc import ABC, abstractmethod

class Clientes(ABC):
    def __init__(self, nome, tipo):
        tipos_validos = ['normal','fidelidade']
        if tipo not in tipos_validos:
            raise ValueError(f"Tipo inválido. Tipos válidos: {tipos_validos}")
        self.nome = nome
        self.tipo = tipo

    @abstractmethod
    def exibir(self):
        pass

class Cadastro(Clientes):
    def exibir(self):
        print(f"NOME: {self.nome}, TIPO: {self.tipo}")

class Cardapio(ABC):
    def __init__(self, nome, preco, tipo):
        self.nome = nome
        self.preco = preco
        self.tipo = tipo

    def menu(self):
        pass

class Menu(Cardapio):
    def menu(self):
        print(f"COMIDA: {self.nome}, PREÇO: {self.preco}, TIPO: {self.tipo}")

class Pedidos:
    def __init__(self):
        self.items = []

    def adicionar_item(self, item: Cardapio):
        self.items.append(item)

    def listar_itens(self):
        for item in self.items:
            print(f"{item.nome} - R$ {item.preco}")

class Pagamento(ABC):
    def __init__(self, cartao, pix, dinheiro):
        self.cartao = cartao
        self.pix = pix
        self.dinheiro = dinheiro

    def formas(self):
        pass

class Pagamento_formas(Pagamento):
    def formas(self):
        print(f"Meios de pagamento disponveis: Cartão: {self.cartao}, PIX: {self.pix}, Dinheiro: {self.dinheiro}")

clientes = Cadastro("livia", "fidelidade")
clientes.exibir()

comidas = Menu("pizza", "30", "lanche")
comidas2 = Menu("hamburguer", "20", "lanche")
comidas.menu()

pedido = Pedidos()
pedido.adicionar_item(comidas)
pedido.adicionar_item(comidas2)

pedido.listar_itens()
pagar = Pagamento_formas("40", "25", "20")
pagar.formas()

