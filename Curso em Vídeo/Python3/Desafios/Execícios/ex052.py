# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# 1. Quais são os dados de entrada necessários?
#   * um número inteiro.

# 2. Que devo fazer com estes dados?
#   * verificar se o número de entrada é primo ou não.

# 3. Quais são as restrições deste problema?
#   * utilização de laço de repetição for na solução do problema.

# 4. Qual é o resultado esperado?
#   * exibir na tela se o valor digitado é primo ou não.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * 

total = 0
number = int(input('Digite um número inteiro: '))
for c in range(1, number + 1):
    if number % c == 0:
        total = total + 1
if total == 2:
    print('O número {} é primo!'.format(number))
else:
    print('O número {} não é primo!'.format(number))
