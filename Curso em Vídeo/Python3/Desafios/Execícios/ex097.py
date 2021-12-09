# Faça um programa que tenha uma função chamada escreva(), que receba qualquer texto como parâmetro e mostre uma mensagem com tamanho de traços superiores e inferiores adaptável:
# exemplo:
# Entrada:
# escreva('Olá, Mundo!')
# Saida:
# -----------
# Olá, Mundo!
# -----------

def escreva(texto):
    tam = len(texto) + 4
    print(f'═' * tam)
    print(f'{texto:^{tam}}')
    print(f'═' * tam)

print()

texto = str(input('Digite um texto: ')).strip().upper()

escreva(texto)

