# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite: 6.245
# A parte inteira é 6.s

# 1. Quais são os dados de entrada necessários?
#   * um número real (fracionário)

# 2. Que devo fazer com estes dados?
#   * mostrar a porção inteira desse número.

# 3. Quais são as restrições deste problema?
#   * nenhuma.

# 4. Qual é o resultado esperado?
#   * exibir na tela o valor inteiro.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * importar a biblioteca math (trunc)
#   * ler e armazenar um valor 'float' em uma variável.
#   * usar o trunc() para remover a porção fracionária da variável.
#   * exibir na tela a porção inteira do número digitado pelo usuário.

from math import trunc

apres = ' PARTE INTEIRA '
final = ' FIM DO PROGRAMA '

print('\n{:*^44}\n'.format(apres))

number = float(input('Digite um número fracionário: '))
nu_int = trunc(number)
print('\nA parte inteira de {} é:\n> {}'.format(number, nu_int))

print('\n{:*^44}\n'.format(final))
