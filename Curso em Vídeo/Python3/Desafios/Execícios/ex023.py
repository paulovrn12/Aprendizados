# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Exemplo: 
# Digite um número: 1834
# unidade:4
# dezena: 3
# centena: 8
# milhar: 1

# 1. Quais são os dados de entrada necessários?
#   * um número de 0 a 9999.

# 2. Que devo fazer com estes dados?
#   * mostrar seus dígitos separados.

# 3. Quais são as restrições deste problema?
#   * número inteiro positivo com no máximo 4 dígitos.

# 4. Qual é o resultado esperado?
#   * mostrar seus dígitos correspondentes a unidade, dezena, centena e milhar.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar um número inteiro com no máximo 4 dígitos em uma variavel number.
#   * armazenar a divisão inteira de number por 1000 em n_milhar.
#   * armazenar o resto da divisão inteira por 1000 em n_rest_m.
#   * armazenar a divisão inteira de n_rest_m (resto da divisão inteira por 1000) por 100 em n_centena.
#   * armazenar o resto da divisão inteira por 100 em n_rest_c.
#   * armazenar a divisão inteira de n_rest_c (resto da divisão inteira por 100) por 10 em n_dezena.
#   * armazenar o resto da divisão inteira por 10 em n_ rest_d.
#   * armazenar a divisão inteira de n_rest_d (resto da divisão inteira por 10) por 1 em n_unidade.
#   * exibir na tela os valores: n_unidade, n_dezena, n_centena, n_milhar.

print('\n')

number = int(input('Digite um número de 0 até 9999: '))
n_milhar = number // 1000   # n_milhar = number // 1000 % 10
n_rest_m = number % 1000
n_centena = n_rest_m // 100 # n_centena = number // 100 % 10
n_rest_c = n_rest_m % 100 
n_dezena = n_rest_c // 10   # n_dezena = number // 10 % 10
n_rest_d = n_rest_c % 10
n_unidade = n_rest_d // 1   # n_unidade = number // 1 % 10

print("""

Unidade: {}
Dezena:  {}
Centena: {}
Milhar:  {}

""".format(n_unidade, n_dezena, n_centena, n_milhar))
