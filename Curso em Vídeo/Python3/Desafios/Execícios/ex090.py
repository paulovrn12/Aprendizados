# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
# Média >= 7: aprovado

aluno = {}
aluno['nome'] = str(input('Digite o nome desse(a) aluno(a): '))
aluno['media'] = float(str(input('Digite o valor da média desse(a) aluno(a): ')).strip().replace(',', '.'))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
print(aluno['situacao'])