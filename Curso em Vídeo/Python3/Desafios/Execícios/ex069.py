# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# a) quantas pessoas tem mais de 18 anos.
# b) quantos homens foram cadastrados.
# c) quantas mulheres tem menos de 20 anos.

# 

print('''
  ╔═════ Cadastro de pessoas ══════╗
  ║                                ║
  ║ »»»»»»»»»»»» MENU «««««««««««« ║
  ║                                ║
  ║  As idades aceitas não         ║
  ║  podem ser menores que 0 anos  ║
  ║  e apenas valores inteiros.    ║
  ║                                ║
  ║  Sexos aceitos:                ║
  ║    [M] para Masculino.         ║
  ║    [F] para Feminino.          ║
  ║                                ║
  ╚════════════════════════════════╝
''')

pessoas_18mais = 0
contador_homem = 0
pessoas_20menos = 0

while True:
    idade = int(str(input('Baseado no MENU acima, digite a idade de uma pessoa: ')).strip())
    sexo = str(input('Baseado no MENU acima, digite o sexo dessa pessoa: ')).strip().upper()[0]
    nova_pessoa = str(input('Deseja cadastrar mais uma pessoa? [S/N]: ')).strip().upper()[0]
    if idade >= 0 and sexo in 'MF' and nova_pessoa in 'SN':
        if sexo == 'M':
            contador_homem += 1
        if idade >= 18:
            pessoas_18mais += 1
        if idade <= 20:
            pessoas_20menos += 1
        if nova_pessoa == 'N':
            break
    else:
        print('''Repita o processo e digite de
        acordo com o MENU no topo do terminal!''')
print(f'Foram cadastrados {contador_homem} homens, {pessoas_18mais} pessoas com 18 anos ou mais e {pessoas_20menos} pessoas com 20 anos ou menos.')