# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# 1. Quais são os dados de entrada necessários?
#   * três números inteiros.

# 2. Que devo fazer com estes dados?
#   * verificar qual é o maior e qual é o menor entre eles.

# 3. Quais são as restrições deste problema?
#   * uma entrada inteira.

# 4. Qual é o resultado esperado?
#   * mostrar os valores maiores e menores.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * 

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior é {}'.format(maior))
print('O menor é {}'.format(menor))
