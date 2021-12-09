def aumentar(valor=0, porcentagem=0):
    """
    -> recebe um valor e uma porcentagem e retorna o valor acrecido referente a porcentagem.
    valor: recebe um valor monetario qualquer.
    porcentagem: recebe uma porcentagem qualquer.
    return
    by @paulovrn12
    """
    valor_final = valor + (valor * porcentagem/100)
    valor_final = str(f'R$ {valor_final:.2f}').replace(',', '.')
    return valor_final

def diminuir(valor=0, porcentagem=0):
    """
    -> recebe um valor e uma porcentagem e retorna o valor subtraido referente a porcentagem.
    valor: recebe um valor monetario qualquer.
    porcentagem: recebe uma porcentagem qualquer.
    return
    by @paulovrn12
    """
    valor_final = valor - (valor * porcentagem/100)
    valor_final = str(f'R$ {valor_final:.2f}').replace(',', '.')
    return valor_final

def dobro(valor=0):
    """
    -> recebe um valor e uma porcentagem e retorna o valor acrecido a porcentagem.
    valor: recebe um valor monetario qualquer.
    return
    by @paulovrn12
    """
    valor_final = valor * 2
    valor_final = str(f'R$ {valor_final:.2f}').replace(',', '.')
    return valor_final

def metade(valor=0):
    """
    -> recebe um valor e uma porcentagem e retorna o valor acrecido a porcentagem.
    valor: recebe um valor monetario qualquer.
    return
    by @paulovrn12
    """
    valor_final = valor / 2
    valor_final = str(f'R$ {valor_final:.2f}').replace(',', '.')
    return valor_final

def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
