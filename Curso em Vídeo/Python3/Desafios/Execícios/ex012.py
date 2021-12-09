# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.

# 1. Quais são os dados de entrada necessários?
#   * valor de um produto em R$.

# 2. Que devo fazer com estes dados?
#   * calcular o valor do desconto desse produto (valor * 0.05).

# 3. Quais são as restrições deste problema?
#   * o valor deve ser em reais e ter dois dígitos decimais.

# 4. Qual é o resultado esperado?
#   * mostrar o valor com o desconto na tela.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * apresentação.
#   * ler um valor em reais.
#   * armazenar esse valor em uma variável.
#   * calcular o valor do produto com o desconto.
#   * exibir na tela o novo valor com desconto.
#   * finalização.

apres = ' DESCONTO DE PRODUTOS '
final = ' FIM DO PROGRAMA '

print('\n{:-^48}\n'.format(apres))

print('Aceitamos os valores apenas em R$##.## (reais).\n')

produto = float(input('Digite o valor original de um produto: R$'))
descont = produto - (produto * 0.05)
print('\nO valor do produto com desconto é de R${:.2f}.'.format(descont))

print('\n{:-^48}\n'.format(final))
