# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final. mostre uma listagem de preços, organizando os dados em forma tabular (Em formato de tabela de texto e alinhado).

produtos = ('Doritos', 9.90,
            'Fini', 4.99,
            'Coca-cola', 8.50,
            'Kit-kat', 3.70,
            'Água de coco', 13.90)
print('LISTAGEM DE PREÇOS')
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')

#print(f'''
#{produtos[0]:.<30}R${produtos[1]:.2f}
#{produtos[2]:.<30}R${produtos[3]:.2f}
#{produtos[4]:.<30}R${produtos[5]:.2f}
#{produtos[6]:.<30}R${produtos[7]:.2f}
#{produtos[8]:.<30}R${produtos[9]:.2f}
#''')
