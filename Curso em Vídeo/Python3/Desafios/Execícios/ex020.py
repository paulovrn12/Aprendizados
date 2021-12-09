# O mesmo professor do desafio anterior quer sortear a ordem de apresenação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. 

# 1. Quais são os dados de entrada necessários?
#   * nomes de 4 alunos.

# 2. Que devo fazer com estes dados?
#   * embaralhar a ordem dos alunos.

# 3. Quais são as restrições deste problema?
#   * deve-se importar componentes da biblioteca random.

# 4. Qual é o resultado esperado?
#   * exibir uma ordem de alunos.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar nomes de 4 alunos em variáveis.
#   * embaralhar a lista de alunos. 
#   * exibir na tela a lista de alunos.

from random import shuffle

texto1 = ' ORDEM DE APRESENTAÇÃO '
texto2 = ' FINAL DO APLICATIVO '

print('\n{:↔^44}\n'.format(texto1))

al1 = str(input('Digite um nome: '))
al2 = str(input('Digite um nome: '))
al3 = str(input('Digite um nome: '))
al4 = str(input('Digite um nome: '))
alunos = [al1, al2, al3, al4]
shuffle(alunos)
print('\nA ordem dos alunos é:\n> {}'.format(alunos))

print('\n{:↔^44}\n'.format(texto2))
