# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
# Considere a maioridade com 21 anos.

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

# importações necessárias:
from datetime import date

anoagora = date.today().year
menores = 0

# leitura da entrada do usuário:
for c in range (1, 8):
    ano = int(str(input('Digite seu ano de nascimento: ')).strip())
    if anoagora - ano < 21:
        menores = menores + 1
maiores = c - menores
print('''
Da lista, {} pessoas são maiores de idade e {} são menores de idade.
'''.format(maiores, menores))