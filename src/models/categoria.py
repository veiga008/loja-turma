
class Categoria:
    """
    Classe responsável por organizar os produtos
    em grupos, como Eletrônicos e Livros.
    """

    def __init__(self, nome):
        # Cria o nome da categoria inicialmente vazio
        self.__nome = ""

        # Define o nome utilizando a validação do método renomear
        self.renomear(nome)

    @property
    def nome(self):
        # Permite consultar o nome armazenado na categoria
        return self.__nome

    def renomear(self, nome):
        # Remove espaços desnecessários do início e do final
        nome = nome.strip()

        # Impede que a categoria fique sem um nome válido
        if nome == "":
            raise ValueError(
                "O nome da categoria não pode ser vazio."
            )

        # Salva o novo nome da categoria
        self.__nome = nome

    def __str__(self):
        # Define como o nome será exibido quando usamos print()
        return self.__nome
