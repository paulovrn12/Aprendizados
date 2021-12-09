# Crie um script Python que leia dois números e tente mostrar a soma entre eles.

# 1. Quais são os dados de entrada necessários?
#   * dois números.

# 2. Que devo fazer com estes dados?
#   * deve somá-los e exibir na tela a soma entre eles.

# 3. Quais são as restrições deste problema?
#   * deve ser digitado apenas dois números inteiros.

# 4. Qual é o resultado esperado?
#   * exibir na tela a soma entre os dois números.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * pedir o primeiro número.
#   * pedir o segundo número.
#   * somar os números.
#   * exibir a soma dos dois números.

print('A seguir digite dois números inteiros "sem virgula" para serem somados.')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
soma = num1 + num2

print('A soma entre {} e {} é igual a {}.'.format(num1, num2, soma))
