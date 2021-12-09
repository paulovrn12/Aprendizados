# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere o dólar a 5.25 reais, dia 12/07/21, 09:45  GNT +3.

# 1. Quais são os dados de entrada necessários?
#   * um valor de dinheiro em reais do usuário.

# 2. Que devo fazer com estes dados?
#   * devo fazer a conversão de real para dólar, dividindo o valor em reais pelo valor em dólares.

# 3. Quais são as restrições deste problema?
#   * o usuário deve apresetar apenas valores em R$.

# 4. Qual é o resultado esperado?
#   * mostrar a conversão do valor em reais em dólares.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * apresentação.
#   * ler um valor em reais na formatação float.
#   * armazenar esse valor em uma variavel real.
#   * dividir o valor em real com o valor do dólar atual*.
#   * mostrar na tela o valor convertido.
#   * finalização.

apres = ' CONVERSOR REAL > DÓLAR '
final = ' FINAL DA CONVERSÃO '

print('\n{:#^34}\n'.format(apres))

print('\nAceitamos apenas pontuações\nna separação de casas decimais.\n')

real = float(input('Digite um valor em reais: R$'))
dola = real / 5.25
print('\nR${:.2f} equivalem á:\n> US${:.2f}'.format(real, dola))

print('\n{:#^34}\n'.format(final))
