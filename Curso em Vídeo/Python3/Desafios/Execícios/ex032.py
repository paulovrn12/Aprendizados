# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

# 1. Quais são os dados de entrada necessários?
#   * um ano qualquer da era comum.

# 2. Que devo fazer com estes dados?
#   * calcular o valor da entrada é divisível por 4 exceto multiplos de 100 que não são multiplos de 400.

# 3. Quais são as restrições deste problema?
#   * uma entrada no tipo int().

# 4. Qual é o resultado esperado?
#   * exibir na tela se o ano é bissexto ou não.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar um valor inteiro e positivo em uma variavel 'year'.
#   * se o resto da divisão inteira de 'year' por 4 for 0, exibir na tela que o ano 'year' é bissexto.
#   * se o resto da divisão inteira de 'year' por 4 for diferente de 0, exibir na tela que o ano 'year' não é bissexto.

from datetime import date

year = str(input('Digite um ano qualquer da era comum (E.C.). Digite 0 para o ano atual: ')).strip()
year = int(year)
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano {} é bissexto.'.format(year))
else:
    print('O ano {} não é bissexto.'.format(year))
