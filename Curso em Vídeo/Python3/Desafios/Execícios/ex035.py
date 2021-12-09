# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# 1. Quais são os dados de entrada necessários?
#   * 3 valores de comprimento de retas.

# 2. Que devo fazer com estes dados?
#   * 

# 3. Quais são as restrições deste problema?
#   * 

# 4. Qual é o resultado esperado?
#   * 

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * 

a = float(input('Digite um comprimento de uma reta A: '))
b = float(input('Digite um comprimento de uma reta B: '))
c = float(input('Digite um comprimento de uma reta C: '))
if a < b + c and b < a + c and c < a + b:
    print('As retas formam um triangulo.')
else:
    print('As retas não formam um triângulo.')
