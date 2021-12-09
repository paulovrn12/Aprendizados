def aumentar(valor=0, porcentagem=0, formato=False):
    """
    -> recebe um valor e uma porcentagem e retorna o valor acrecido referente a porcentagem.
    valor: recebe um valor monetario qualquer.
    porcentagem: recebe uma porcentagem qualquer.
    return
    by @paulovrn12
    """
    valor_final = valor + (valor * porcentagem/100)
    return valor_final if formato is False else moeda(valor_final)

def diminuir(valor=0, porcentagem=0, formato=False):
    """
    -> recebe um valor e uma porcentagem e retorna o valor subtraido referente a porcentagem.
    valor: recebe um valor monetario qualquer.
    porcentagem: recebe uma porcentagem qualquer.
    return
    by @paulovrn12
    """
    valor_final = valor - (valor * porcentagem/100)
    return valor_final if formato is False else moeda(valor_final)


def dobro(valor=0, formato=False):
    """
    -> recebe um valor e uma porcentagem e retorna o valor acrecido a porcentagem.
    valor: recebe um valor monetario qualquer.
    return
    by @paulovrn12
    """
    valor_final = valor * 2
    return valor_final if formato is False else moeda(valor_final)


def metade(valor=0, formato=False):
    """
    -> recebe um valor e uma porcentagem e retorna o valor acrecido a porcentagem.
    valor: recebe um valor monetario qualquer.
    return
    by @paulovrn12
    """
    valor_final = valor / 2
    return valor_final if formato is False else moeda(valor_final)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')

def resumo(valor=0, taxaa=10, taxar=5):
    print('-' * 36)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 36)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(valor, taxaa, True)}')
    print(f'{taxaa}% de aumento: \t{diminuir(valor, taxar, True)}')
    print('-' * 36)
