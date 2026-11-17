
from models.carrinho import Carrinho


class Cliente:
    """Representa uma pessoa que compra na loja."""

    def __init__(self, nome, email):
        # Armazena o nome do cliente
        self.__nome = nome

        # Inicializa o e-mail vazio
        self.__email = ""

        # Define o e-mail usando a validação do método atualizar_email()
        self.atualizar_email(email)

        # Cria um carrinho associado ao cliente
        self.__carrinho = Carrinho()

        # Cria uma lista vazia para guardar os pedidos confirmados
        self.__pedidos = []

    @property
    def nome(self):
        # Permite consultar o nome do cliente
        return self.__nome

    @property
    def email(self):
        # Permite consultar o e-mail do cliente
        return self.__email

    @property
    def carrinho(self):
        # Permite acessar o carrinho do cliente
        return self.__carrinho

    @property
    def pedidos(self):
        # Retorna uma cópia da lista para proteger a lista original
        return list(self.__pedidos)

    def atualizar_email(self, valor):
        # Remove espaços do início e do final do e-mail
        valor = valor.strip()

        # Verifica se o e-mail possui o caractere @
        if "@" not in valor:
            raise ValueError(f"E-mail inválido: {valor}")

        # Armazena o e-mail em letras minúsculas
        self.__email = valor.lower()

    def adicionar_pedido(self, pedido):
        # Adiciona um pedido confirmado à lista do cliente
        self.__pedidos.append(pedido)

    def __str__(self):
        # Define como as informações do cliente serão exibidas
        return f"{self.__nome} <{self.__email}>"
