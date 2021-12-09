# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário passa mostrar as notas de cada aluno individualmente, com o 999 parando a mostragem das notas.
# 
# Exemplo de resposta:
# 
# Nº  Nome      Média
# -------------------
# 0   Pedro     5.8
# 1   Maria     8.0
# 2   João      3.8
# 3   Gustavo   4.8 
# -------------------

linha = []
tabela = []
topo = ['Nº', 'Nome', 'Média']
repeticao = 0
media = 0
separador = '-'
while True:
    repeticao = repeticao = 1
    if repeticao == 1:
        numeros = 0
    else:
        numeros = numeros + 1
    linha.append(numeros)
    linha.append(str(input('Digite o nome de um(a) aluno(a): ')))
    nota_1 = float(str(input('Digite a 1ª nota desse(a) aluno(a): ').strip().replace(',', '.')))
    nota_2 = float(str(input('Digite a 2ª nota desse(a) aluno(a): ').strip().replace(',', '.')))
    media = (nota_1 + nota_2) / 2
    linha.append(media)
    tabela.append(linha[:])
    linha.clear()
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Digite apenas S para SIM e N para NÃO!\nDeseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'{topo[0]:<3} {topo[1]:<12} {topo[2]:>5}\n{separador * 22}')
for l, a in enumerate(tabela):
    print(f'{l:<3}{a[1]:<12}{a[2]:>5.1f}')
