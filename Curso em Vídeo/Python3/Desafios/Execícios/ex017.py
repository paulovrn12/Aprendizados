# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

# 1. Quais são os dados de entrada necessários?
#   * comprimento do cateto oposto e cateto adjacente.

# 2. Que devo fazer com estes dados?
#   * calcular o comprimeito da hipotenusa (hp² = co² + ca²).

# 3. Quais são as restrições deste problema?
#   * nenhuma.

# 4. Qual é o resultado esperado?
#   * exibir na tela o comprimento da hipotenusa.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar o valor de um cateto oposto.
#   * ler e armazenar o valor de um cateto adjacente.
#   * calcular o valor da hipotenusa e armazenar esse valor em uma variável.
#   * exibir na tela o valor da hipotenusa.

from math import hypot

texto1 = ' HIPOTENUSA '
texto2 = ' FIM DO APP '

print('\n{:=^44}\n'.format(texto1))

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hp = hypot(co, ca)
print('\n> Tendo:\n{} como cateto oposto;\n{} cateto adjacente;\n\n> Temos:\n{:.2f} como a hipotenusa.'.format(co, ca, hp))

print('\n{:=^44}\n'.format(texto2))
