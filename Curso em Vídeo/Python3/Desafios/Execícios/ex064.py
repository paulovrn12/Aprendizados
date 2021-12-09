# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitado e qual foi a soma entre eles (desconsiderando o flag, o 999.)

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

contador = 0
soma = 0
numeros = ''
while numeros != 999:
    numeros = int(str(input('Digite um número para a soma: ')).strip())
    soma = soma + numeros
    contador = contador + 1
if numeros == 999:
    soma = soma - 999
contador = contador - 1
print('Foram somados {} números e tendo uma soma igual a {}!'.format(contador, soma))
