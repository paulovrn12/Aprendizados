# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex.: 5! = 5*4*3*2*1 = 120

# 1. Quais são os dados de entrada necessários?
#   *

# 2. Que devo fazer com estes dados?
#   *

# 3. Quais são as restrições deste problema?
#   *

# 4. Qual é o resultado esperado?
#   *

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   *

# from math import factorial
# n = int(input('Digite um número: ))
# f = factorial(n)
# print('O fatorial de {} é {}.'.format(n, f))


n = int(str(input('Digite um número inteiro qualquer: ')).strip())
c = n
f = 1
while c > 0:
    f = f * c
    c = c - 1
print('O fatorial de {} ou {}! é igual a {}.'.format(n, n, f))
