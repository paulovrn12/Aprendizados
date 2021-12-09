# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
# de uma pessoa, retornando um valor literal (frase) indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO
# nas eleições.
# Entre 18 e 64 anos Voto Obrigatório
# Abaixo de 18 não vota;
# Acima acima 65 o voto é opcional.

from datetime import date

def voto(ano_nascimento):
    """
    -> Recebe um ano de nascimento e baseado nisso mostra se a pessoa deve votar ou não.
    :param ano_nascimento: recebe um ano de nascimento.
    """
    anoAtual = date.today().year
    idade = anoAtual - ano_nascimento
    if idade < 18:
        return 'VOTO NEGADO'
    if idade > 65:
        return 'VOTO OPCIONAL'
    if idade >=18 and idade <=65:
        return 'VOTO OBRIGATÓRIO'

nascimento = int(str(input('Digite um ano de nascimento: ')).strip())

print(f'Sua situação de voto atual é {voto(nascimento)}, pois tem {date.today().year - nascimento} anos!')