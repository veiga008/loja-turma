
# Classe Produto: representa um produto que está à venda na loja.
class Produto:

    # Método construtor: executado quando criamos um novo produto.
    # Recebe nome, preço, estoque e categoria.
    def __init__(self, nome, preco, estoque, categoria):

        # Atributos privados: armazenam os dados do produto.
        # Os dois sublinhados indicam que são atributos privados.
        self.__nome = nome

        # Inicializa o preço com zero.
        # O preço será definido depois pelo método alterar_preco().
        self.__preco = 0.0

        # Guarda o objeto Categoria associado ao produto.
        self.__categoria = categoria

        # Define o preço utilizando um método que valida o valor.
        self.alterar_preco(preco)

        # Verifica se o estoque é negativo.
        if estoque < 0:
            raise ValueError("O estoque não pode ser negativo.")

        # Guarda a quantidade disponível no estoque.
        self.__estoque = estoque

    # @property permite consultar o nome do produto.
    @property
    def nome(self):
        return self.__nome

    # Permite consultar o preço do produto.
    @property
    def preco(self):
        return self.__preco

    # Permite consultar a quantidade disponível no estoque.
    @property
    def estoque(self):
        return self.__estoque

    # Permite consultar a categoria do produto.
    @property
    def categoria(self):
        return self.__categoria

    # Método responsável por alterar o preço do produto.
    def alterar_preco(self, valor):

        # Verifica se o preço é maior que zero.
        # Se não for, apresenta uma mensagem de erro.
        if valor <= 0:
            raise ValueError(
                f"Preço inválido para {self.__nome}: "
                "precisa ser maior que zero."
            )

        # Converte o preço para número decimal.
        self.__preco = float(valor)

    # Verifica se existe quantidade suficiente no estoque.
    def tem_estoque(self, quantidade):

        # Retorna True se houver estoque suficiente.
        # Retorna False se não houver.
        return self.__estoque >= quantidade

    # Método para retirar produtos do estoque quando alguém compra.
    def baixar_estoque(self, quantidade):

        # Primeiro verifica se existe estoque suficiente.
        if not self.tem_estoque(quantidade):
            raise ValueError(
                f"Estoque insuficiente de {self.__nome}: "
                f"há {self.__estoque} unidade(s)."
            )

        # Diminui a quantidade disponível no estoque.
        self.__estoque -= quantidade

    # Método para adicionar produtos de volta ao estoque.
    def repor_estoque(self, quantidade):

        # Verifica se a quantidade informada é maior que zero.
        if quantidade <= 0:
            raise ValueError(
                "A quantidade para repor precisa ser maior que zero."
            )

        # Aumenta a quantidade disponível no estoque.
        self.__estoque += quantidade

    # Define como o produto será apresentado quando utilizarmos print().
    def __str__(self):

        # Retorna nome, preço, estoque e categoria em formato de texto.
        return (
            f"{self.__nome} - R$ {self.__preco:.2f} "
            f"({self.__estoque} em estoque) [{self.__categoria}]"
        )
