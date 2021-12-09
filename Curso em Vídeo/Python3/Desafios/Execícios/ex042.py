# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# Se formar um triangulo, informe qual tipo ele é:
# - Equilátero: todos os lados iguais.
# - Isósceles: dois lados iguais.
# - Escaleno: todos os lados diferentes.

# Soma de dois lados quaisquer devem dar maior que o valor do terceiro lado.

# 1. Quais são os dados de entrada necessários?
#   * três comprimentos de retas.

# 2. Que devo fazer com estes dados?
#   * verificar se seus comprimentos se encaixam na condição de existência de triângulos.

# 3. Quais são as restrições deste problema?
#   * nenhuma.

# 4. Qual é o resultado esperado?
#   * mostrar na tela se as retas formam ou não um triângulo e caso formarem, informar de qual tipo esse triângulo seria.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar três comprimentos de retas em três variaveis a, b e c do tipo float().
#   * verificar se há possibilidade de criar um triângulo.
#   * se sim, verificar qual tipo de triângulo é.
#   * se todos os lados forem iguais se trata de um triângulo equilátero.
#   * se dois lados forem iguais e um diferente, se trata de um trângulo isósceles.
#   * se os 3 lados forem diferentes, se trata de um triângulo escaleno.

a = float(str(input('Digite o comprimento da reta A: ')).strip().replace(',', '.'))
b = float(str(input('Digite o comprimento da reta B: ')).strip().replace(',', '.'))
c = float(str(input('Digite o comprimento da reta C: ')).strip().replace(',', '.'))

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print('{}Os lados A = {}, B = {} e C = {} formam um triângulo equilátero!{}'.format('\033[1;32m', a, b, c, '\033[m'))
    elif a == b != c or b == c != a or a == c != b:
        print('{}Os lados A = {}, B = {} e C = {} formam um triângulo isósceles!{}'.format('\033[1;34m', a, b, c, '\033[m'))
    elif a != b != c:
        print('{}Os lados A = {}, B = {} e C = {} formam um triangulo escaleno!{}'.format('\033[1;35m', a, b, c, '\033[m'))
else:
    print('{}Os lados A = {}, B = {} e C = {} não formam um triângulo!{}'.format('\033[1;31m', a, b, c, '\033[m'))
