# Faça um programa que tenha uma função chamada area(), que receba as dimenções de um terreno retangular(largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
    print(f'A área é de {largura * comprimento:.2f} metros.')

print()
larg = float(str(input('Digite um valor de largura em metros: ')).strip().replace(',', '.'))
comp = float(str(input('Digite um valor de comprimento em metros: ')).strip().replace(',', '.'))
area(larg, comp)