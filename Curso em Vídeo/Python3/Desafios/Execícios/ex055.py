# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

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

maior = 0
menor = 0
# leitura de dados do usuário:
for pessoa in range(1, 6):
    peso = float(str(input('Digite o peso da {}ª pessoa em kg: '.format(pessoa))).strip().replace(',', '.'))
    if pessoa == 1: # se for o primeiro laço de repetição.
        maior = peso # o 'maior' peso é o 'peso'.
        menor = peso # o 'menor' peso é o 'peso'.
    else:
        if peso > maior: # se o 'peso' for maior que o 'maior' número lido.
            maior = peso # o 'peso' vira o 'maior'.
        if peso < menor: # se o 'peso' for menor que o 'menor' número lido.
            menor = peso # o 'peso' vira o menor.
print('O maior peso lido foi de {} kg'.format(maior))
print('O menor peso lido foi de {} kg'.format(menor))
