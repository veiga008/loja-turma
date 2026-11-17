
# Importa ferramentas para criar classes abstratas.
from abc import ABC, abstractmethod


# Classe abstrata Pagamento.
# ABC indica que esta classe é abstrata.
class Pagamento(ABC):

    """
    Esta classe funciona como um modelo para as formas de pagamento.
    Não podemos criar um objeto diretamente dessa classe.
    As classes filhas, como Pix e Cartao, devem implementar seus métodos.
    """

    # Método construtor: recebe o valor do pagamento.
    def __init__(self, valor):

        # Verifica se o valor é maior que zero.
        if valor <= 0:
            raise ValueError("O valor do pagamento precisa ser maior que zero.")

        # Atributo protegido: pode ser utilizado pela classe
        # e também pelas classes filhas.
        self._valor = float(valor)

    # @property permite consultar o valor do pagamento.
    @property
    def valor(self):
        return self._valor

    # Método abstrato: cada classe filha deve implementar
    # sua própria forma de calcular o pagamento.
    @abstractmethod
    def calcular_total(self):
        pass

    # Método abstrato: cada classe filha deve informar
    # o nome ou a descrição da forma de pagamento.
    @abstractmethod
    def descricao(self):
        pass
