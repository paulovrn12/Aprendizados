# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# a) Quantas pessoas foram cadastradas.
# b) Uma listagem com as pessoas mais pesadas.
# c) Uma listagem com as pessoas mais leves.

info = [] # lista principal.
temp = [] # lista temporária.
maior = menor = 0 # maiores e menores valores, inicialmente zerados.
continuar = '' # variavel que indica se o usuário deseja adicionar novas pessoas.
while True: # repetição de adição de novos ítens e de parte da lógica verdadeira enquanto.
    temp.append(str(input('\nDigite o nome de uma pessoa: ')).strip())
    temp.append(float(str(input('Digite o peso de uma pessoa: ')).strip().replace(',', '.')))
    if len(info) == 0: # se a lista não conter itens.
        maior = menor = temp[1] # o maior e menor itens é igual ao primeiro adicionado.
    else: # se não
        if temp[1] > maior: # se o segundo item adicionado for o maior
            maior = temp[1] # maior é igual ao segundo
        if temp[1] < menor:
            menor = temp[1]
    info.append(temp[:])
    temp.clear()
    continuar = str(input('\nDeseja adicionar mais pessoas? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        print('\nDigite apenas S para SIM e N para NÃO!')
        continuar = str(input('Deseja adicionar mais pessoas? [S/N]: ')).strip().upper()[0]
    if continuar == 'N': # se o usuário não quiser adicionar novos itens
        break # pare a repetição.
print(f'A lista de pessoas é {info}.')
print(f'a) Foram cadastradas {len(info)} pessoas!')
print(f'b) O maior peso foi de {maior} kg de', end='')
for p in info:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print(f'c) O menor peso foi de {menor} kg de', end='')
for p in info:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()
