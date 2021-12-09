# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci.
# Ex.: 0 → 1 → 1 → 2 → 3 → 5 → 8...
#      t1  t2  t3  t4  t5  t6  t7...

# t1 = 0
# t2 = 1
# t3 = t1 + t2
# t4 = t2 + t3
# t5 = t3 + t4
# t6 = t4 + t5
# t7 = t5 + t6

n_termos = int(str(input('Quantos ternos da sequência de Fibonacci você deseja mostrar? ')))
t1 = 0
t2 = 1
contador = 3
print('{} > {}'.format(t1, t2), end='')
while contador <= n_termos:
    t3 = t1 + t2
    print(' > {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    contador = contador + 1
print(' > FIM!')