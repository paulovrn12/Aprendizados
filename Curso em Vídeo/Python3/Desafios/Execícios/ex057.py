# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, faça a digitação novamente até ter um valor correto.

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

print('''
Digite a seguir:
Use M para masculino
Use F para feminino''')

s = ''
while 'M' != s != 'F':
    s = str(input('Digite o sexo de uma pessoa: ')).strip().upper()[0]
    if 'M' != s != 'F':
        print('Digite uma opção válida!')
    else:
        print('Dado gravado com sucesso!')
