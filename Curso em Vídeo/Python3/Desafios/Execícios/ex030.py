# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

# 1. Quais são os dados de entrada necessários?
#   * um número inteiro qualquer.

# 2. Que devo fazer com estes dados?
#   * verificar esse número é par ou não.

# 3. Quais são as restrições deste problema?
#   * entrada inteira.

# 4. Qual é o resultado esperado?
#   * exibir na tela se um número é par ou impar

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar um número inteiro digitado pelo usuário numa variável 'número'.
#   * se a 'número' % 2 == 0, exibir que a 'número' é par.
#   * se a 'número' % 2 != 0, exibir que a 'número' é ímpar.

número = str(input('Digite um número: ')).strip()
número = int(número)
if número % 2 == 0:
    print('O número {} é par!'.format(número))
elif número % 2 != 0:
    print('O número {} é impar!'.format(número))
