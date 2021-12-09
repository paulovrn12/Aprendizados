# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# 1. Quais são os dados de entrada necessários?
#   * um valor inteiro que representa o ano de nascimento de uma pessoa.

# 2. Que devo fazer com estes dados?
#   * calcular se (baseado no ano atual) a situação dela em relação ao alistamento militar.

# 3. Quais são as restrições deste problema?
#   * uma entrada inteira, utilização da biblioteca datetime com o date.

# 4. Qual é o resultado esperado?
#   * exibir na tela se a pessoa ainda deve se alistar e o ano de alistamento, se a pessoa está na hora de se alistar,
# se o tempo de alistamento já passou.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * importar a biblioteca datetime e usar apenas o date para utilizar o ano atual.  

from datetime import date

ano_de_nascimento = int(str(input('Digite o ano de seu nascimento: ')).strip())

ano_atual = date.today().year
idade = ano_atual - ano_de_nascimento
idade_de_alistamento = 18
ano_de_alistamento = 0

if idade < idade_de_alistamento:    # se minha idade for menor que 18 anos.
    faltam = abs(idade - idade_de_alistamento)
    ano_de_alistamento = ano_atual + faltam
    if faltam == 1:
        print('{}Falta {} ano para se alistar!\nVocê deve se alistar em {}.{}'.format('\033[0;32m', faltam, ano_de_alistamento, '\033[m'))
    elif faltam > 1:
        print('{}Faltam {} anos para se alistar!\nVocê deve se alistar em {}.{}'.format('\033[0;32m', faltam, ano_de_alistamento, '\033[m'))
elif idade == idade_de_alistamento: # se minha idade for igual a 18 anos.
    print('{}Este é o ano de seu alistamento!\nApresente-se a junta militar.{}'.format('\033[0;33m', '\033[m'))
elif idade > idade_de_alistamento:  # se minha idade for maior que 18 anos.
    passou = abs(idade - idade_de_alistamento)
    ano_de_alistamento = ano_atual - passou
    if passou == 1:
        print('{}Passou {} ano do seu alistamento!\nVocê deveria ter se apresentado a junta militar em {}.{}'.format('\033[0;31m', passou, ano_de_alistamento, '\033[m'))
    elif passou > 1:
        print('{}Passaram {} anos do seu alistamento!\nVocê deveria ter se apresentado a junta militar em {}.{}'.format('\033[0;31m', passou, ano_de_alistamento, '\033[m'))
