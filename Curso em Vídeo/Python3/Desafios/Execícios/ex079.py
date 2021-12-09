# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = []
continuar = ''
while True:
    numeros.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().split()[0]
    if continuar not in 'SN': # se o usuário não digitar S de Sim ou N de Não.
        continuar = str(input('Digite corretamente! Deseja continuar? [S/N]: ')).upper().split()[0]
    else:
        if numeros[0] in numeros:
            print('Número já digitado, esse não será cadastrado!')
            del numeros[0] # delete o número que acabou de ser digitado.
numeros.sort() # organizar os números em ordem do menor para o maior.
print(f'Exceto os valores repetidos, você digitou os números {numeros}!')