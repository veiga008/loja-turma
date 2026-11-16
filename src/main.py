
"""
LOJA POO - ARQUIVO PRINCIPAL

# IMPORTAÇÃO DOS MÓDULOS
# Aqui importamos as classes que estão separadas na pasta models.
# Isso permite utilizar cada classe neste arquivo principal.

from models.cartao import Cartao
from models.categoria import Categoria
from models.cliente import Cliente
from models.pagamento import Pagamento
from models.pedido import Pedido
from models.pix import Pix
from models.produto import Produto


# ==================================================
# 1. PRODUTO - REGRAS DE NEGÓCIO RN1 E RN2
# ==================================================

print("--- Produto ---")

# Criamos uma categoria para organizar os produtos.
eletronicos = Categoria("Eletronicos")

# Criamos dois objetos da classe Produto.
# Cada produto possui nome, preço, estoque e categoria.
notebook = Produto("Notebook", 3500, 5, eletronicos)
mouse = Produto("Mouse", 100, 20, eletronicos)

# Exibimos os dados dos produtos.
print(notebook)
print(mouse)

# Retiramos duas unidades do estoque do notebook.
notebook.baixar_estoque(2)

# O estoque esperado é de 3 unidades.
print("Estoque depois de baixar 2 (esperado 3):", notebook.estoque)

# Recolocamos duas unidades no estoque.
notebook.repor_estoque(2)

# O estoque esperado volta para 5 unidades.
print("Estoque depois de repor 2 (esperado 5):", notebook.estoque)

# TESTES DE ERRO:
# RN1: verifica se o sistema impede um preço menor ou igual a zero.
# Produto("Brinde", -10, 1, eletronicos)

# RN2: verifica se o sistema impede um estoque negativo.
# Produto("Brinde", 10, -1, eletronicos)

# RN2: verifica se o sistema impede retirar mais produtos
# do que existem disponíveis no estoque.
# notebook.baixar_estoque(10)


# ==================================================
# 2. CATEGORIA - ASSOCIAÇÃO ENTRE OBJETOS
# ==================================================

print("--- Categoria ---")

# Mostramos a categoria associada ao notebook.
print("Categoria do notebook (esperado Eletronicos):", notebook.categoria)

# Alteramos o nome da categoria.
# Como o produto está associado ao objeto Categoria,
# ele passa a apresentar o novo nome da categoria.
eletronicos.renomear("Eletrônicos")

print("Depois de renomear (esperado Eletrônicos):", notebook.categoria)

# TESTE DE ERRO:
# Verifica se o sistema impede criar uma categoria sem nome.
# Categoria("")


# ==================================================
# 3. CLIENTE E CARRINHO - RN3, RN4 E RN5
# ==================================================

print("--- Cliente e Carrinho ---")

# Criamos um cliente com nome e e-mail.
# O cliente também possui um carrinho associado a ele.
maria = Cliente("Maria", "maria@email.com")

print(maria)

# Adicionamos um notebook ao carrinho.
maria.carrinho.adicionar(notebook, 1)

# Adicionamos um mouse ao carrinho.
maria.carrinho.adicionar(mouse, 1)

# Adicionamos novamente o mesmo mouse.
# RN5: o sistema deve aumentar a quantidade do produto,
# sem criar uma nova linha para o mesmo produto.
maria.carrinho.adicionar(mouse, 1)

# Exibimos os produtos que estão no carrinho.
print(maria.carrinho)

# Devem existir duas linhas: uma para o notebook
# e outra para o mouse.
print("Linhas no carrinho (esperado 2):", len(maria.carrinho.itens))

# Calculamos o valor total dos produtos.
print("Total do carrinho (esperado 3700.0):", maria.carrinho.total())

# TESTES DE ERRO:

# RN3: verifica se o sistema impede um e-mail sem @.
# maria.atualizar_email("mariaemail.com")

# RN4: verifica se o sistema impede adicionar
# uma quantidade maior do que o estoque disponível.
# maria.carrinho.adicionar(notebook, 10)


# ==================================================
# 4. PAGAMENTO, PIX E CARTÃO - RN8, RN9 E RN10
# ==================================================

print("--- Pagamento ---")

# Criamos três objetos de pagamento.
# Todos utilizam o mesmo valor inicial de R$ 3.700.
pix = Pix(3700)
cartao_3x = Cartao(3700, 3)
cartao_6x = Cartao(3700, 6)

# O Pix aplica 5% de desconto.
print("RN8 - Pix (esperado 3515.0):", pix.calcular_total())

# O cartão em 3 parcelas não aplica juros.
print("RN9 - Cartão em 3x (esperado 3700.0):", cartao_3x.calcular_total())

# O cartão em 6 parcelas aplica juros.
print("RN9 - Cartão em 6x (esperado 4070.0):", cartao_6x.calcular_total())


# POLIMORFISMO:
# Colocamos diferentes formas de pagamento em uma mesma lista.
# O laço for percorre os pagamentos e chama o mesmo método
# gerar_comprovante() para cada objeto.
# Cada classe pode apresentar seu próprio comportamento.

pagamentos = [pix, cartao_3x, cartao_6x]

for pagamento in pagamentos:
    print(pagamento.gerar_comprovante())


# TESTES DE ERRO:

# RN10: verifica se o cartão impede mais de 12 parcelas.
# Cartao(3700, 13)

# A classe Pagamento é abstrata.
# Por isso, não deve ser criada diretamente.
# Pagamento(100)


# ==================================================
# 5. PEDIDO - RN6, RN7 E RN11
# ==================================================

print("--- Pedido ---")

# Criamos um pedido para a cliente Maria.
# O pagamento escolhido é Pix.
pedido = Pedido(1, maria, "pix")

# Calculamos o valor do pedido com o desconto do Pix.
print("Total do pedido com Pix (esperado 3515.0):", pedido.total())

# Confirmamos o pedido.
# A confirmação deve retirar os produtos do estoque.
pedido.confirmar()

# Exibimos os dados do pedido.
print(pedido)

# Conferimos o estoque depois da confirmação.
print("RN11 - Estoque do notebook depois de confirmar (esperado 4):", notebook.estoque)
print("RN11 - Estoque do mouse depois de confirmar (esperado 18):", mouse.estoque)

# Depois da confirmação, o carrinho deve ficar vazio.
print("RN7 - Carrinho depois do pedido (esperado Carrinho vazio.):", maria.carrinho)

# Cancelamos o pedido.
# O cancelamento deve devolver os produtos ao estoque.
pedido.cancelar()

# Conferimos se as quantidades voltaram aos valores iniciais.
print("RN11 - Estoque do notebook depois de cancelar (esperado 5):", notebook.estoque)
print("RN11 - Estoque do mouse depois de cancelar (esperado 20):", mouse.estoque)


# TESTE DE ERRO:
# RN6: verifica se o sistema impede criar um pedido
# quando o carrinho está vazio.
# Pedido(2, maria, "pix")
