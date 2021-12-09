# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada, utilizando laço for.

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

n = int(input('Digite um número: '))
for c in range(0, 11):
    t = n * c
    print('{} * {} = {}'.format(n, c, t))
