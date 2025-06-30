from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def vendedor(self):
        pass

class ConcreteClass(AbstractClass):
    def vendedor(self):
        print(f"{self.nome} é um vendedor")

n1 = ConcreteClass("João")
n1.vendedor()

from dataclasses import dataclass

lista_clientes = []

@dataclass
class Clientes:
    nome: str
    cpf: str

    def exibir(self):
        print(f"NOME: {self.nome}, CPF: {self.cpf}")

@dataclass
class Cadastro:
    Clientes: Clientes
    numero: int
    email: str

    def cadastrar_clientes(self, nome, cpf):
        novo_cliente = Clientes(nome=nome, cpf=cpf)

        lista_clientes.append(novo_cliente)
        return novo_cliente

    def exibir(self):
        for cliente in lista_clientes:
            print(cliente)

livia = Clientes(nome="livia", cpf="17440528755")
livia.exibir()

cadastro = Cadastro(livia.nome, numero="2342354245", email="gouveia@gmail.com")
cadastro.exibir()

natalia = Clientes(nome="natalia", cpf="16459923931")
cadastro = Cadastro(natalia.nome, numero="02323402340", email="natalia@gmail.com")
cadastro.exibir()

cadastro.cadastrar_clientes(nome="douglas", cpf="234234354234")
cadastro.cadastrar_clientes(nome="livia", cpf="2314324234")
cadastro.exibir()
