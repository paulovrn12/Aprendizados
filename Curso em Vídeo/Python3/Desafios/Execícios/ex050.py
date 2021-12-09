# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado foi impar desconsidere-o.

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

soma = 0
for c in range(0, 6):
    numb = int(input('Digite um número inteiro par: '))
    if numb % 2 == 0:
        soma = soma + numb # soma += numb
print('A soma dos números pares é {}'.format(soma))
