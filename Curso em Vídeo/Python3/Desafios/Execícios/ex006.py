# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# 1. Quais são os dados de entrada necessários?
#   * um número inteiro.

# 2. Que devo fazer com estes dados?
#   * calcular o dobro, triplo e raiz quadrada do número escrito pelo usuário.

# 3. Quais são as restrições deste problema? 
#   * o usuário deve digitar um número inteiro.

# 4. Qual é o resultado esperado?
#   * exibir na tela os resultados dos cálculos apresentados.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * efeito visual simples com o nome do programa.
#   * ler um valor digitado pelo usuário.
#   * armazenar esse valor em uma variável.
#   * calcular o seu dobro do número.
#   * calcular o seu triplo do número.
#   * calcular a sua raiz quadrada do número.
#   * mostrar ao usuário os resultados dos cálculos.
#   * efeito visual simples de fim do programa.

visual1 = 'DOBRO, TRIPLO E RAIZ QUADRADA'
visual2 = 'FIM DO APLICATIVO'

print('\n{:-^44}'.format(visual1))

print('Nesse programa é aceito números inteiros e fracionários!\n')

numb = float(input('Digite um número qualquer: '))
dubl = numb * 2
trip = numb * 3
sqrt = float(numb ** (1/2))

print('\n> {} é o dobro de {}. \n> {} é o triplo de {}. \n> {:.2f} é a raiz quadrada de {}.\n'.format(dubl, numb, trip, numb, sqrt, numb))

print('{:-^44}\n'.format(visual2))
