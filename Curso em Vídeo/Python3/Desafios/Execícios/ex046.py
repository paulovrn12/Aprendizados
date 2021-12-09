# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

# 1. Quais são os dados de entrada necessários?
#   * enter

# 2. Que devo fazer com estes dados?
#   * iniciar uma contagem regressiva.

# 3. Quais são as restrições deste problema?
#   * importação da biblioteca time para usar o módulo sleep.

# 4. Qual é o resultado esperado?
#   * mostrar uma contagem regressiva para o estouro de fogos de artifício.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * importar o módulo sleep da biblioteca time.
#   * ler uma entrada para iniciar a contagem regressiva.
#   * para o laço c no intervalo de 10 a 0 -1, mostre c com um segundo de pausa 'sleep(1)'.
#   * escreva fogos estourando.

from time import sleep

inicio = input('Tecle ENTER para iniciar a contagem regressiva.')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('Fogos estourando!')
