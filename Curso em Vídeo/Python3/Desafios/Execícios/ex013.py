# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

# 1. Quais são os dados de entrada necessários?
#   * valor de um salário em reais.

# 2. Que devo fazer com estes dados?
#   * calcular o valor do salário com aumento de 15% (salario • 1.15).

# 3. Quais são as restrições deste problema?
#   * o valor do salário deve ser apenas em R$##.##.

# 4. Qual é o resultado esperado?
#   * exibir na tela o novo salário desse funcionário.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * apresentação.
#   * ler e armazenar esse valor de salário em uma variável.
#   * calcular o valor do aumento do salário.
#   * exibir na tela o valor atual do salário com aumento.
#   * finalização.

apres = ' AUMENTO SALARIAL '
final = ' FIM DO APLICATIVO '

print('\n{:*^50}\n'.format(apres))

salar = float(input('Digite o seu salário atual: R$'))
aumen = salar * 1.15
print('\nSeu salario com aumento de 15% é de R${:.2f}.'.format(aumen))

print('\n{:*^50}\n'.format(final))
