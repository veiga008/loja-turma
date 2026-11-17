
from models.comprovante import Comprovante
from models.pagamento import Pagamento


class Cartao(Pagamento, Comprovante):
    """
    Classe responsável por realizar pagamentos com cartão.
    Herda características de Pagamento e Comprovante.
    """

    JUROS = 0.10  # Define uma taxa de juros de 10%

    def __init__(self, valor, parcelas=1):
        # Aproveita a inicialização da classe Pagamento
        super().__init__(valor)

        # Verifica se a quantidade de parcelas está entre 1 e 12
        if parcelas < 1 or parcelas > 12:
            raise ValueError("O cartão aceita de 1 a 12 parcelas.")

        # Armazena a quantidade de parcelas escolhida
        self.__parcelas = parcelas

    @property
    def parcelas(self):
        # Permite consultar a quantidade de parcelas
        return self.__parcelas

    def calcular_total(self):
        # Aplica juros quando o pagamento ultrapassa 3 parcelas
        if self.__parcelas > 3:
            return round(self._valor * (1 + Cartao.JUROS), 2)

        # Mantém o valor original quando são até 3 parcelas
        return round(self._valor, 2)

    def descricao(self):
        # Retorna uma descrição da forma de pagamento
        return f"Cartão em {self.__parcelas}x"

    def gerar_comprovante(self):
        # Calcula o valor de cada parcela
        valor_parcela = round(
            self.calcular_total() / self.__parcelas, 2
        )

        # Monta o comprovante com os valores do pagamento
        return (
            f"Comprovante Cartão: R$ {self.calcular_total():.2f} "
            f"em {self.__parcelas}x de R$ {valor_parcela:.2f}."
        )
