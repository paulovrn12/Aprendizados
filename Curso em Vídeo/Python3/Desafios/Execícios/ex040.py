# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO.
# Média entre 5.0 e 6.9: RECUPERAÇÃO.
# Média 7.0 ou superior: APROVADO.

# 1. Quais são os dados de entrada necessários?
#   * dois falores em porto flutuante.

# 2. Que devo fazer com estes dados?
#   * calcular a média dentre esses dois valores.

# 3. Quais são as restrições deste problema?
#   * entradas do tipo float e print do valor da média com uma casa decimal.

# 4. Qual é o resultado esperado?
#   * mostrar na tela a média desse aluno e mostrar se ele foi aprovado, reprovado ou se está de recuperação.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar duas notas de um aluno em duas variaveis nota1 e nota2.
#   * calcular a média dessas notas as somando e dividindo por 2.0.
#   * se a média for maior ou igual a 7, mostrar na tela a média e que o aluno foi aprovado.
#   * se a média estar entre 5 e 6.9, mostrar na tela a média e que o aluno está de recuperação.
#   * se a média for menor que 5, mostrar a média na tela e que o aluno foi reprovado.

nota1 = float(str(input('Digite o valor da sua primeira nota: ')).strip().replace(',', '.'))
nota2 = float(str(input('Digite o valor da sua segunda nota: ')).strip().replace(',', '.'))
media = (nota1 + nota2) / 2.0   # cálculo da média.
if media >= 7:
    print('{}Você foi APROVADO, com a média de {:.1f} pontos!{}'.format('\033[1;32m', media, '\033[m'))
elif media >= 5 and media < 7: # ou: elif 7 > média >=5:
    print('{}Você está de RECUPERAÇÃO, por estar com a média de {:.1f} pontos!{}'.format('\033[1;33m', media, '\033[m'))
elif media < 5:
    print('{}Você está REPROVADO, com a média de {:.1f} pontos!{}'.format('\033[1;31m', media, '\033[m'))
