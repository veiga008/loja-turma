
# Importa a classe Comprovante, que define as regras para gerar comprovantes.
from models.comprovante import Comprovante

# Importa a classe abstrata Pagamento.
from models.pagamento import Pagamento


# A classe Pix herda de Pagamento e Comprovante.
class Pix(Pagamento, Comprovante):

    """
    HERANÇA: Pix é uma forma de Pagamento.
    HERANÇA MÚLTIPLA: também utiliza o contrato Comprovante.
    """

    # Constante que representa 5% de desconto no pagamento via Pix.
    DESCONTO = 0.05

    # Implementa o cálculo do pagamento via Pix.
    def calcular_total(self):

        # Aplica 5% de desconto sobre o valor original.
        # 1 - 0.05 significa que o cliente paga 95% do valor.
        # round arredonda o resultado para duas casas decimais.
        return round(self._valor * (1 - Pix.DESCONTO), 2)

    # Retorna a descrição da forma de pagamento.
    def descricao(self):
        return "Pix (5% de desconto)"

    # Implementa a geração do comprovante de pagamento.
    def gerar_comprovante(self):

        # Exibe o valor final pago, já com o desconto aplicado.
        return f"Comprovante Pix: R$ {self.calcular_total():.2f} pagos à vista."
