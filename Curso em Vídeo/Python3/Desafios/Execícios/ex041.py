# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM.
# - Até 14 ano: INFANTIL.
# - Até 19 anos: JUNIOR.
# - Até 20 anos: SÊNIOR.
# - Acima: MASTER.
   
# 1. Quais são os dados de entrada necessários?
#   * um ano de nascimento de um atleta.

# 2. Que devo fazer com estes dados?
#   * verificar a categoria desse atleta pela sua idade.

# 3. Quais são as restrições deste problema?
#   * importação da biblioteca datetime e usar o módulo date e year.

# 4. Qual é o resultado esperado?
#   * mostrar a categoria em que esse atleta se qualifica perante a sua idade atual.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * importar a biblioteca datetime e usar o módulo date.
#   * ler e armazenar um ano de nascimento de um atleta em uma variavel chamada ano de nascimento.
#   * calcular a idade desse atleta sendo a idade igual a subtração do ano atual com o ano de nascimento do atleta.
#   * se a idade for menor ou igual 9 esse atleta é mirim.
#   * se a idade estiver entre 10 e 14 anos esse atleta é infantil.
#   * se a idade estiver entre 15 e 19 anos esse atleta é junior.
#   * se a idade for igual a 20 anos esse atleta é senior.
#   * se a idade for maior que 20 esse atleta é master.

from datetime import date

ano_de_nascimento = int(str(input('Digite o ano de seu nascimento: ')).strip())
ano_atual = date.today().year
idade = ano_atual - ano_de_nascimento

if idade <= 9:
    print('Você tem {} anos.\nVocê é um atleta MIRIM!'.format(idade))
elif idade >= 10 and idade <= 14:
    print('Você tem {} anos.\nVocê é um atleta INFANTIL!'.format(idade))
elif idade >= 15 and idade <= 19:
    print('Você tem {} anos.\nVocê é um atleta JUNIOR!'.format(idade))
elif idade == 20:
    print('Você tem {} anos.\nVocê é um atleta SÊNIOR!'.format(idade))
elif idade > 20:
    print('Você tem {} anos.\nVocê é um atleta MASTER!'.format(idade))
