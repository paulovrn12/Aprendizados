def leiaInt(mensagem):
    while True:
        try:
            entrada = str(input(mensagem)).strip()
            valor = int(entrada)
        except (ValueError, TypeError):
            print(f'O valor digitado \"{entrada}\" não é um número inteiro!')
        except KeyboardInterrupt:
            print('Entrada de dados finalizada!')
            return 0
        else:
            break
    return valor

def leiaFloat(mensagem):
    while True:
        try:
            entrada = str(input(mensagem)).strip().replace(',', '.')
            valor = float(entrada)
        except (ValueError, TypeError):
            print(f'O valor digitado \"{entrada}\" não é um valor real!')
        except KeyboardInterrupt:
            print('Entrada de dados finalizada!')
            return 0
        else:
            break
    return valor