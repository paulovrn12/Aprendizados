# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
# Tem que dar 20667

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
'''
soma = 0
contador = 0
for c in range(1, 501, 2): # O '2' mostra os números ímpares.
    if c % 3 == 0:
        contador = contador + 1 # contador de números. 0 = 0 + 1
        soma = soma + c # conceito de acumuladores. 0 = 0 + c
print('A soma de todos os {} valores solicitados é {}'.format(contador, soma))
'''


# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

# variavel que vai somando acada repetição, representada pelos termos somados.
cont = 0
# variavel que vai somando os valores.
soma = 0
# números impares no intervalo de 1 e 500.
for c in range(1, 501, 2):
    if c % 3 == 0:
        # soma da quantidade dos números utilizados pela soma abaixo.
        cont = cont + 1
        # soma dos termos, ímpares e múltiplos de 3.
        soma = soma + c
print('A soma dos {} termos é igual a {}'.format(cont, soma))