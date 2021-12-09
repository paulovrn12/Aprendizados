# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

# 1. Quais são os dados de entrada necessários?
#   * um número inteiro.

# 2. Que devo fazer com estes dados?
#   * mostrar a tabuada desse número, multiplicando do 1 ao 10.

# 3. Quais são as restrições deste problema?
#   * o programa deve receber apenas números inteiros.

# 4. Qual é o resultado esperado?
#   * a tabuada do número ser exibida ao usuário.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * apresentação.
#   * receber o número inteiro do usuário.
#   * armazenar esse número em uma variável.
#   * exibir na tela a tabuáda completa desse número no print.
#   * finalização.

apres = ' TABUADA '
final = ' FIM DO APP '

print('\n{:+^49}\n'.format(apres))

print('Veremos a tabuada de um número que você desejar.\nAceitamos somente números inteiros!\n')
number = int(input('Digite um número: '))
x1 = number * 1
x2 = number * 2
x3 = number * 3
x4 = number * 4
x5 = number * 5
x6 = number * 6
x7 = number * 7
x8 = number * 8
x9 = number * 9
x10 = number * 10
print('\nA tabuada do número {} é:\n{} •  1 = {}\n{} •  2 = {}\n{} •  3 = {}\n{} •  4 = {}\n{} •  5 = {}\n{} •  6 = {}\n{} •  7 = {}\n{} •  8 = {}\n{} •  9 = {}\n{} • 10 = {}'.format(number, number, x1, number, x2, number, x3, number, x4, number, x5, number, x6, number, x7, number, x8, number, x9, number, x10))

print('\n{:+^49}\n'.format(final))
