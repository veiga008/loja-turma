
from models.item_carrinho import ItemCarrinho


class Carrinho:
    """
    Classe que controla os produtos escolhidos pelo cliente.
    """

    def __init__(self):
        # Inicializa o carrinho sem nenhum produto
        self.__itens = []

    @property
    def itens(self):
        # Disponibiliza uma cópia dos produtos armazenados
        return list(self.__itens)

    def __buscar_item(self, produto):
        # Verifica se o produto já foi adicionado
        for item in self.__itens:
            if item.produto is produto:
                return item
        return None

    def adicionar(self, produto, quantidade=1):
        # Impede que seja adicionada uma quantidade inválida
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")

        # Confere se o produto já existe na lista
        item = self.__buscar_item(produto)
        quantidade_total = quantidade

        if item is not None:
            quantidade_total += item.quantidade

        # Confirma se há unidades suficientes no estoque
        if not produto.tem_estoque(quantidade_total):
            raise ValueError(
                f"Só há {produto.estoque} unidade(s) de {produto.nome} em estoque."
            )

        # Atualiza o produto existente ou adiciona um novo
        if item is not None:
            item.aumentar(quantidade)
        else:
            self.__itens.append(ItemCarrinho(produto, quantidade))

    def remover(self, produto):
        # Procura o produto que o cliente deseja retirar
        item = self.__buscar_item(produto)

        if item is None:
            raise ValueError(f"{produto.nome} não está no carrinho.")

        # Exclui o produto encontrado da lista
        self.__itens.remove(item)

    def total(self):
        # Calcula a soma dos valores dos produtos
        soma = 0.0

        for item in self.__itens:
            soma += item.subtotal()

        # Ajusta o resultado para duas casas decimais
        return round(soma, 2)

    def esta_vazio(self):
        # Retorna verdadeiro quando não existem produtos
        return len(self.__itens) == 0

    def limpar(self):
        # Deixa o carrinho completamente vazio
        self.__itens = []

    def __str__(self):
        # Verifica se existe algum produto no carrinho
        if self.esta_vazio():
            return "Carrinho vazio."

        # Organiza as informações dos produtos
        linhas = []

        for item in self.__itens:
            linhas.append(str(item))

        # Exibe o valor final da compra
        linhas.append(f"TOTAL: R$ {self.total():.2f}")

        return "\n".join(linhas)
