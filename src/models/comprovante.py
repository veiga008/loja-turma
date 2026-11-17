
from abc import ABC, abstractmethod


class Comprovante(ABC):
    """
    Define um contrato para as classes que geram comprovantes.
    """

    # Obriga as classes que implementarem esse contrato
    # a criarem o método gerar_comprovante()
    @abstractmethod
    def gerar_comprovante(self):
        # Define que o método deve retornar o texto do comprovante
        pass
