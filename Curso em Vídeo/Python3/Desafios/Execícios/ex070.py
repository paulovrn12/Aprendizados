# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# a) Qual é o total gasto na compra.
# b) Quantos produtos custam mais de R$ 1000,00.
# c) Qual é o nome do produto mais barato.

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Digite o nome de um produto: ')).strip()
    preco = float(str(input('Digite o preço desse produto: R$ ')).strip().replace(',', '.'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato == produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja adicionar mais produtos? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total gasto na compra foi de {total:.2f}, tendo {totmil} produtos custando mais de R$ 1000,00.')
print(barato, f'sendo o produto mais barato da lista que custa R${menor:2f}!')