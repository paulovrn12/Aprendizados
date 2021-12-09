def aumentar(valor, porcentagem):
    """
    -> recebe um valor e uma porcentagem e retorna o valor acrecido referente a porcentagem.
    valor: recebe um valor monetario qualquer.
    porcentagem: recebe uma porcentagem qualquer.
    return
    by @paulovrn12
    """
    valor_final = valor + (valor * porcentagem/100)
    return valor_final

def diminuir(valor, porcentagem):
    """
    -> recebe um valor e uma porcentagem e retorna o valor subtraido referente a porcentagem.
    valor: recebe um valor monetario qualquer.
    porcentagem: recebe uma porcentagem qualquer.
    return
    by @paulovrn12
    """
    valor_final = valor - (valor * porcentagem/100)
    return valor_final

def dobro(valor):
    """
    -> recebe um valor e uma porcentagem e retorna o valor acrecido a porcentagem.
    valor: recebe um valor monetario qualquer.
    return
    by @paulovrn12
    """
    valor_final = valor * 2
    return valor_final

def metade(valor):
    """
    -> recebe um valor e uma porcentagem e retorna o valor acrecido a porcentagem.
    valor: recebe um valor monetario qualquer.
    return
    by @paulovrn12
    """
    valor_final = valor / 2
    return valor_final
