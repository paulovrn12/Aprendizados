# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

# 1. Quais são os dados de entrada necessários?
#   * 

# 2. Que devo fazer com estes dados?
#   * 

# 3. Quais são as restrições deste problema?
#   * 

# 4. Qual é o resultado esperado?
#   * 

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * 

mediaidade = 0
somaidade = 0
mulhermenorvinte = 0
maioridadehomem = 0
nomemaisvelho = ''

for pessoa in range(1, 5):
    nome = str(input('''Digite o nome da {}ª pessoa: '''.format(pessoa)).split())
    idade = int(str(input('''Digite a idade da {}ª pessoa: '''.format(pessoa))).strip())
    sexo = str(input('''Sexo:
    Digite M para masculino.
    Digite F para feminino.
    Digite o sexo da {}ª pessoa: '''.format(pessoa).upper()).strip())
    somaidade = somaidade + idade

    if pessoa == 1 and sexo == 'M':
        maioridade = idade
        nomemaisvelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo == 'F' and idade < 20:
        mulhermenorvinte = mulhermenorvinte + 1
mediaidade = somaidade / pessoa
print('''
A idade média do grupo é de {} anos.
O homem mais velho é o {} e ele tem {} anos.
{} mulheres têm menos de 20 anos.'''.format(mediaidade, nomemaisvelho, idade, mulhermenorvinte))