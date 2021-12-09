# Escreva um programa que leia dois números inteiros e compare-os, mostrando ana tela uma mensagem:
# O primeiro valor é maior.
# O segundo valor é maior.
# Não existe valor maior, os dois são iguais.

# 1. Quais são os dados de entrada necessários?
#   * dois valores inteiros.

# 2. Que devo fazer com estes dados?
#   * comparar esses valores.

# 3. Quais são as restrições deste problema?
#   * entrada inteira.

# 4. Qual é o resultado esperado?
#   * exibir na tela se o primeiro valor é maior, se o segundo é maior e se ambos são iguais.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar um valor inteiro em uma variavel valor1.
#   * ler e armazenar um valor inteiro em uma variavel valor2.
#   * se 'valor1' for maior que 'valor2', exibir que o primeiro valor é o maior número.
#   * se 'valor2' for maior que 'valor1', exibir que o segundo valor é o maior número.
#   * se 'valor1' for igual a 'valor2', exibir que ambos os valores são iguais.

valor1 = int(str(input('Digite um valor inteiro: ')).strip())
valor2 = int(str(input('Digite outro valor inteiro: ')).strip())
if valor1 > valor2:
    print('O número {} é o maior.'.format(valor1))
elif valor2 > valor1:
    print('O número {} é o maior.'.format(valor2))
elif valor1 == valor2:
    print('Ambos os valores são iguais.')
