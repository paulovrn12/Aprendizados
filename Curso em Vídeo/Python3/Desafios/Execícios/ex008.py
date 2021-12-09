# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# 1. Quais são os dados de entrada necessários?
#   * um valor em metros.

# 2. Que devo fazer com estes dados?
#   * deve se converter esse valor em um valor em centímetros e milímetros.

# 3. Quais são as restrições deste problema?
#   * nenhuma restrição.

# 4. Qual é o resultado esperado?
#   * que o usuário visualize na tela esse valor em métros convertido para centímetros e milímetros.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * apresentação.
#   * leitura de um valor em metros digitado pelo usuário.
#   * armazenamento desse valor em uma variável de metros.
#   * conversão de metros para centímetros. 1m = 100 cm
#   * conversão de metros para milímetros. 1m = 1000 mm.
#   * mostrar esses resultados na tela do usuário. 
#   * finalização.

apresent = ' MILICENTMETRO '
finaliza = ' CONVERSÃO END '

print('\n{:#^35}\n'.format(apresent))

metro = float(input('Digite um valor em metros: '))
centi = metro * 100
milim = metro * 1000
print('\n* {:.2f} metros equivale a: \n> {:.2f} centímetros. \n> {:.2f} milímetros.'.format(metro, centi, milim))

print('\n{:#^35}\n'.format(finaliza))
