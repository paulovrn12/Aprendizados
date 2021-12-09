# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade, pegando o ano atual no sistema) em um dicionário
#se por acaso a CTPS(carteira de trabalho de previdência social) for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar (35 anos de contribuição). Se CTPS for igual a 0, mostre os dados na tela.

from datetime import date

clt = {}
clt['Nome'] = str(input('Digite o nome do trabalhador: ')).strip()
clt['Nascimento'] = int(str(input('Digite o seu ano de nascimento: ')).strip()) 
clt['Idade'] = date.today().year - clt['Nascimento']
clt['CTPS'] = int(str(input('Digite o número da sua Carteira de Trabalho: ')).strip())
if clt['CTPS'] == 0:
    del clt['CTPS']
    for key, value in clt.items():
        print(f'{key} é {value}.')
    print('Não possue carteira de trabalho!')
else:
    clt['Ano_Contrato'] = int(str(input('Digite o ano em que foi contratado: ')).strip())
    clt['Idade_Contrato'] = clt['Ano_Contrato'] - clt['Nascimento']
    clt['Salario'] = float(str(input('Digite o seu salário atual: R$ ')).strip().replace(',', '.'))
    clt['Ano_Aposentadoria'] = clt['Ano_Contrato'] + 35
    clt['Idade_Aposentadoria'] = clt['Idade_Contrato'] + 35
    print()
    for key, value in clt.items():
        if key == 'Nome':
            print(f'Seu nome é {value}', end='')
        if key == 'Nascimento':
            print(f', nascido em {value}', end=' ')
        if key == 'Idade':
            print(f'({value} anos)', end=' ')
        if key == 'CTPS':
            print(f'e possue a carteira de número {value}.')
        if key == 'Ano_Contrato':
            print(f'Você foi contratado em {value}', end=' ')
        if key == 'Idade_Contrato':
            print(f'({value} anos)', end=' ')
        if key == 'Salario':
            print(f'e ganha R$ {value:.2f}.')
        if key == 'Ano_Aposentadoria':
            print(f'Você vai se aposentar em {value}', end=' ')
        if key == 'Idade_Aposentadoria':
            print(f'({value} anos).')     
print()
print(clt)
