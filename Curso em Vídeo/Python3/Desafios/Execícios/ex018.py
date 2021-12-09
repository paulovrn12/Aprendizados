# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# 1. Quais são os dados de entrada necessários?
#   * um ângulo qualquer.

# 2. Que devo fazer com estes dados?
#   * calcular o seno, cosseno e tangente desse ângulo.

# 3. Quais são as restrições deste problema?
#   * nenhuma.

# 4. Qual é o resultado esperado?
#   * exibir na tela o valor do seno, cosseno e tangente desse ângulo.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar em uma variável o valor de um ângulo qualquer.
#   * calcular o valor do seno, cosseno e tangente desse ângulo.
#   * exibir na tela esses valores.

from math import cos, sin, tan, radians

texto1 = ' SENO, COSSENO E TANGENTE '
texto2 = ' FIM DO APLICAÇÃO PYTHON3 '

print('\n{:☼^44}\n'.format(texto1))

ang = float(input('Digite o valor de um ângulo qualquer: '))
se = sin(radians(ang))
co = cos(radians(ang))
tg = tan(radians(ang))
print('\nValores referentes ao ângulo de {}º:\n> Seno: {:.2f}.\n> Cosseno: {:.2f}.\n> Tangente: {:.2f}'.format(ang, se, co, tg))

print('\n{:☼^44}\n'.format(texto2))
