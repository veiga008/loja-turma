
# Importa as classes responsáveis pelas formas de pagamento.
from models.cartao import Cartao
from models.pix import Pix


# Classe Pedido: representa a compra realizada por um cliente.
class Pedido:

    """
    AGREGAÇÃO: recebe os itens que já existem no carrinho.
    POLIMORFISMO: permite calcular o pagamento sem precisar
    saber todos os detalhes de cada forma de pagamento.
    """

    # Método construtor: recebe os dados necessários para criar o pedido.
    def __init__(self, numero, cliente, forma_pagamento, parcelas=1):

        # Verifica se o carrinho está vazio.
        # Se estiver vazio, gera um erro e impede a criação do pedido.
        if cliente.carrinho.esta_vazio():
            raise ValueError("O carrinho está vazio: não dá para fechar o pedido.")

        # Guarda as informações do pedido em atributos privados.
        self.__numero = numero
        self.__cliente = cliente

        # Recebe os itens que já foram criados pelo carrinho.
        self.__itens = cliente.carrinho.itens

        # Define o status inicial do pedido.
        self.__status = "aberto"

        # Verifica qual forma de pagamento o cliente escolheu.
        if forma_pagamento == "pix":

            # Cria um pagamento via Pix com o valor do subtotal.
            self.__pagamento = Pix(self.subtotal())

        elif forma_pagamento == "cartao":

            # Cria um pagamento com cartão e a quantidade de parcelas.
            self.__pagamento = Cartao(self.subtotal(), parcelas)

        else:
            # Se a forma de pagamento for inválida, gera um erro.
            raise ValueError("Forma de pagamento inválida: use 'pix' ou 'cartao'.")

    # Permite consultar o número do pedido.
    @property
    def numero(self):
        return self.__numero

    # Permite consultar o status do pedido.
    @property
    def status(self):
        return self.__status

    # Retorna uma cópia da lista de itens do pedido.
    @property
    def itens(self):
        return list(self.__itens)

    # Permite consultar a forma de pagamento utilizada.
    @property
    def pagamento(self):
        return self.__pagamento

    # Calcula a soma dos subtotais de todos os itens.
    def subtotal(self):
        soma = 0.0

        # Percorre todos os itens do pedido.
        for item in self.__itens:
            soma += item.subtotal()

        # Retorna o resultado arredondado para duas casas decimais.
        return round(soma, 2)

    # Calcula o valor final do pedido.
    # O método da forma de pagamento faz o cálculo.
    def total(self):
        return self.__pagamento.calcular_total()

    # Confirma o pedido e atualiza o estoque.
    def confirmar(self):

        # Só permite confirmar pedidos que estejam abertos.
        if self.__status != "aberto":
            raise ValueError(
                f"O pedido {self.__numero} já está {self.__status}."
            )

        # Primeiro verifica se todos os produtos possuem estoque suficiente.
        for item in self.__itens:
            if not item.produto.tem_estoque(item.quantidade):
                raise ValueError(
                    f"Estoque insuficiente de {item.produto.nome}."
                )

        # Depois de verificar tudo, retira os produtos do estoque.
        for item in self.__itens:
            item.produto.baixar_estoque(item.quantidade)

        # Atualiza o status do pedido.
        self.__status = "confirmado"

        # Limpa o carrinho depois da confirmação.
        self.__cliente.carrinho.limpar()

        # Adiciona o pedido ao histórico do cliente.
        self.__cliente.adicionar_pedido(self)

    # Cancela um pedido que já foi confirmado.
    def cancelar(self):

        # Verifica se o pedido está confirmado.
        if self.__status != "confirmado":
            raise ValueError("Só dá para cancelar um pedido confirmado.")

        # Devolve ao estoque as unidades que foram retiradas.
        for item in self.__itens:
            item.produto.repor_estoque(item.quantidade)

        # Atualiza o status do pedido.
        self.__status = "cancelado"

    # Transforma os dados do pedido em um texto organizado.
    def __str__(self):

        # Cria a primeira linha com número, status e nome do cliente.
        linhas = [
            f"Pedido {self.__numero} ({self.__status}) - {self.__cliente.nome}"
        ]

        # Percorre os itens e adiciona cada um à lista de linhas.
        for item in self.__itens:
            linhas.append(f"  {item}")

        # Adiciona o subtotal.
        linhas.append(f"  Subtotal: R$ {self.subtotal():.2f}")

        # Adiciona a descrição da forma de pagamento.
        linhas.append(f"  Pagamento: {self.__pagamento.descricao()}")

        # Adiciona o valor final.
        linhas.append(f"  TOTAL: R$ {self.total():.2f}")

        # Junta todas as linhas em um único texto.
        return "\n".join(linhas)
