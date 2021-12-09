# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

# 1. Quais são os dados de entrada necessários?
#   * duas notas de um aluno.

# 2. Que devo fazer com estes dados?
#   * calcular a média entre eles.

# 3. Quais são as restrições deste problema?
#   * o aluno deve digitar dois valores com pontuação.

# 4. Qual é o resultado esperado?
#   * a apresentação da média desse aluno na tela.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * apresentação do programa.
#   * leitura da primeira nota.
#   * leitura da segunda nota.
#   * armazenamento dessas notas em duas variaveis.
#   * cálculo da média (nota 1 + nota 2 / 2) e armazenamento desse resultado em uma variável de média.
#   * mostrar na tela o resultado do aluno, da média das notas desse aluno.
#   * finalização do programa.

visual1 = ' MÉDIA DE NOTAS ESCOLARES '
visual2 = ' FINALIZAÇÃO DO APLICATIVO '

print('\n{:=^44}\n'.format(visual2))

nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2
print('A sua média nas duas provas foi de: \n> {:.1f} pontos!'.format(media))

print('\n{:=^44}\n'.format(visual2))
