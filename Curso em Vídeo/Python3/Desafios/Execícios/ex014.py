# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

# 1. Quais são os dados de entrada necessários?
#   * Uma temperatura em ºC

# 2. Que devo fazer com estes dados?
#   * calcular a temperatura em Fahrenheit ((F = 1,8 * C) + 32).

# 3. Quais são as restrições deste problema?
#   * o valor digitado deve ser apenas em Celsius.

# 4. Qual é o resultado esperado?
#   * exibir na tela a conversão de uma temperatura em ºC para ºF.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar uma temperatura em ºC em uma variável TCelsius.
#   * calcular a temperatura em Fahrenheit.
#   * exibir na tela o resultado do calculo.

apres = ' CONVERSOR DE TEMPERATURAS '
final = ' FECHANDO O CONVERSOR '

print('\n{:*^44}\n'.format(apres))

TCelsius = float(input('Digite uma temperatura em Celsius: '))
TFahrenh = (1.8 * TCelsius) + 32
print('\n{:.2f}ºC equivalem a:\n> {:.2f}ºF.'.format(TCelsius, TFahrenh))

print('\n{:*^44}\n'.format(final))
