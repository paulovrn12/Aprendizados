# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido. 

# 1. Quais são os dados de entrada necessários?
#   * quatro nomes de alunos.

# 2. Que devo fazer com estes dados?
#   * deverá sortear esses nomes.

# 3. Quais são as restrições deste problema?
#   * nenhuma.

# 4. Qual é o resultado esperado?
#   * um nome ser escolhido.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar esses nomes em 4 variáveis.
#   * randomizar esses nomes.
#   * exibir na tela o nome sorteado.

from random import choice

texto1 = ' SORTEIO DE ALUNOS '
texto2 = ' FINAL APP PYTHON3 '

print('\n{:◙^44}\n'.format(texto1))

alu1 = input('Nome de um aluno: ')
alu2 = input('Nome de um aluno: ')
alu3 = input('Nome de um aluno: ')
alu4 = input('Nome de um aluno: ')
alunos = [alu1, alu2, alu3, alu4]
sort = choice(alunos)
print('O aluno sorteado é o {}.'.format(sort))

print('\n{:◙^44}\n'.format(texto2))
