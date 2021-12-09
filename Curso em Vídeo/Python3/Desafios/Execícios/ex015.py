# Escreva um programa que pergunte a quantidade de quilômetros percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0.15 por quilômetro rodado.

# 1. Quais são os dados de entrada necessários?
#   * uma quantia de quilômetros percorridos.
#   * uma quantia de dias alugados.

# 2. Que devo fazer com estes dados?
#   * calcular o valor a pagar pelo aluguel (paga = (kmsr * 0.15) + (dias * 60))

# 3. Quais são as restrições deste problema?
#   * inserir valores em km e em dias.

# 4. Qual é o resultado esperado?
#   * o valor total a pagar em reais.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar a quantia de quilômetros percorridos em uma variável kmsr.
#   * ler e armazenar a quantia de dias alugados em uma variável dias.
#   * calcular o valor total a pagar.
#   * exibir na tela o valor total a pagar pelo aluguel.

apres = ' ALUGUEL DE CARROS '
final = ' FIM DA CALCULADORA '

print('\n{:=^50}\n'.format(apres))

kmsr = float(input('Digite quantos KM foram percorridos: '))
dias = int(input('Digite o número de dias alugados: '))
paga = (kmsr * 0.15) + (dias * 60)
print('\nO valor total a pagar pelo aluguel é de R${:.2f}'.format(paga))

print('\n{:=^50}\n'.format(final))
