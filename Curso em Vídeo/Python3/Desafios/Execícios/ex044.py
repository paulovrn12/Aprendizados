# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista (dinheiro e PIX): 10% de desconto.
# - À vista (cartão): 5% de desconto.
# - À prazo 2X (cartão): preço normal.
# - À prazo 3X e acima (cartão): 20% de juros.

# 1. Quais são os dados de entrada necessários?
#   * um valor de um produto em reais.

# 2. Que devo fazer com estes dados?
#   * calcular os diferentes preços para o produto no dinheiro e Pix, crédito a vista, crédito 2X e crédito 3X.

# 3. Quais são as restrições deste problema?
#   * uma entrada em reais.

# 4. Qual é o resultado esperado?
#   * exibir o valor do produto na condição de pagamento escolhida pelo cliente.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar o valor de um produto em uma variavel valor.
#   * perguntar ao usuário qual a condição de pagamento escolhida pelo cliente sendo:
#       1 - Dinheiro ou PIX; 2 - Débito ou Crédito à vista; 3 - Crédito 2 vezes; 4 - Crédito 3 vezes.
#   * calcular o valor do produto para as diferentes formas de pagamento sendo:
#       1 - valor - (valor * 0.1); 2 - valor - (valor * 0.05); 3 - valor; 4 - valor * 1.2
#   * exibir na tela o preço final na forma de pagamento escolhida.

from time import sleep

print('\n')
valor = float(str(input('Digite o valor de um produto: ')).strip().replace(',', '.'))
print("""
Digite a seguir de 1 a 4 para as formas de pagamento:
1 - Dinheiro ou PIX;
2 - Débito ou Crédito à vista;
3 - Crédito 2x;
4 - Crédito 3x ou mais.
""")
opcao = int(str(input('Digite o método desejado: ')))
print("""
Carregando...
""")
sleep(3)
if opcao == 1:
    valor1 = valor - (valor * 0.1)
    print('O valor do produto é R${:.2f}!'.format(valor1))
elif opcao == 2:
    valor2 = valor - (valor * 0.05)
    print('O valor do produto é R${:.2f}!'.format(valor2))
elif opcao == 3:
    valor3 = valor
    print('O valor do produto é R${:.2f}!'.format(valor3))
elif opcao == 4:
    valor4 = valor * 1.2
    print('O valor do produto é R${:.2f}!'.format(valor4))
else:
    print("""Você digitou método de pagamento que não existe!
    Execute o programa novamente com os valores corretos!
    """)
