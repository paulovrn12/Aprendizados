# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso. Sem usar ifs, apenas tuplas.

numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'desesseis', 'desessete', 'dezoito',
           'dezenove', 'vinte')

while True:
    n_user = int(input('Digite um número de 0 a 20: '))
    if 0 <= n_user <= 20:
        break
    else:
        print('Tente novamente!', end=' ')
print(f'O número {n_user} por extenso é {numeros[n_user]}!')

