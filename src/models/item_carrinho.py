
class ItemCarrinho:
    """
    Representa um item dentro do carrinho de compras.
    Armazena qual é o produto e a quantidade escolhida.
    """

    # Método construtor: executado quando criamos um novo item.
    def __init__(self, produto, quantidade):

        # Atributos privados: guardam os dados do item.
        self.__produto = produto
        self.__quantidade = quantidade

    # @property permite consultar o produto sem acessar diretamente o atributo privado.
    @property
    def produto(self):
        return self.__produto

    # Permite consultar a quantidade do produto.
    @property
    def quantidade(self):
        return self.__quantidade

    # Método para aumentar a quantidade de produtos no carrinho.
    def aumentar(self, quantidade):
        self.__quantidade += quantidade

    # Calcula o subtotal: preço do produto multiplicado pela quantidade.
    # round arredonda o resultado para duas casas decimais.
    def subtotal(self):
        return round(self.__produto.preco * self.__quantidade, 2)

    # Retorna uma representação do item em formato de texto.
    # f-string permite inserir valores dentro do texto.
    def __str__(self):
        return f"{self.__quantidade}x {self.__produto.nome} = R$ {self.subtotal():.2f}"
