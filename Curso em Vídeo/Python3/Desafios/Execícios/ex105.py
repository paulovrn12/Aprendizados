# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings da função.

# funções necessárias:
def notas(*nota_aluno):
    '''
    -> Recebe varias notas de alunos e faz um relatório da turma
    :param *nota_aluno: recebe uma lista com diversas notas dos alunos.
    by @paulovrn12
    '''
    nota_aluno = list(nota_aluno)
    quantidade = len(nota_aluno[0])
    maior_nota = max(nota_aluno[0])
    menor_nota = min(nota_aluno[0])
    media_nota = sum(nota_aluno[0])/len(nota_aluno[0])
    situacao = ['ABAIXO DA MÉDIA','MEDÍOCRE','ACIMA DA MÉDIA']
    n_situacao = ''
    if media_nota < 5.0:
        n_situacao = situacao[0]
    if 5.0 >= media_nota <= 7.0:
        n_situacao = situacao[1]
    if media_nota > 7.0:
        n_situacao = situacao[2]
    relatório = {'quant':quantidade,
                 'maior':maior_nota,
                 'menor':menor_nota,
                 'media':media_nota,
                 'situc':n_situacao}
    return relatório

# programa principal:
todas_notas = []
while True:
    nota = float(str(input('Digite a nota de um aluno da turma: ')).strip().replace(',', '.'))
    todas_notas.append(nota)
    resp = str(input('Deseja adicionar mais notas? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        print('Digite apenas S para Sim e N para Não!')
        resp = str(input('Deseja adicionar mais notas? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Abaixo encontramos em dicionário o relatório das notas da turma:\n{notas(todas_notas)}')

