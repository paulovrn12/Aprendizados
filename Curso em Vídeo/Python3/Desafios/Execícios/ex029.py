# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre um,a mensagem deizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km/h acima do limite. Mostre o valor da multa.

# 1. Quais são os dados de entrada necessários?
#   * um número inteiro e positivo representando a velocidade de um veículo.

# 2. Que devo fazer com estes dados?
#   * verificar se o número é menor, igual ou superior a 80.
#   * se for maior, calcular o valor de uma multa, sendo R$ 7,00 cada 1 km/h a mais que 80.

# 3. Quais são as restrições deste problema?
#   * uma entrada inteira e positiva.

# 4. Qual é o resultado esperado?
#   * mostrar se o motorista não foi ou foi multado e mostrar o valor da multa.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar um valor inteiro de km/h em uma variável 'now_speed'.
#   * criar uma variavel 'speed_limit recebendo o valor 80.
#   * se ele ter uma 'now_speed' sendo maior que 80, calcule o valor da multa: crie uma variável 'traffic_ticket' sendo ela igual a ('now_speed' - 'speed_limit') * 7, e em seguida exiba que o motorista foi multado e o valor da sua multa!
#   * se a 'now_speed' for igual a 80, exiba na tela: "Cuidado com a multa, você está no limite de velocidade!"
#   * se a 'now_speed' for menor que 80 e maior ou igual a 40, exiba na tela: "Isso aí você está dirigindo de forma prudente."
#   * se a 'now_speed' for menor que 40, exiba na tela: "Caso você esteja na faixa da esquerda ou em via única você está multado em R$ 87,13 por transitar abaixo da metade da velocidade máxima permitida de acordo com o Artigo 219 do Código de Trânsito Brasileiro!"

now_speed = str(input('Digite o valor da sua velocidade atual em km/h: ')).strip()
now_speed = int(now_speed)
speed_limit = 80
if now_speed > speed_limit:
    traffic_ticket = (now_speed - speed_limit) * 7
    print('Você foi multado em R$ {:.0f},00 por estar a {:.0f}km/h acima da velocidade permitida!'.format(traffic_ticket, traffic_ticket / 7))
elif now_speed == 80:
    print('Cuidado com a multa, você está no limite de velocidade!')
elif now_speed < 80 and now_speed >= 40:
    print('Isso aí você está dirigindo de forma prudente!')
elif now_speed < 40:
    print('Caso você esteja na faixa da esquerda ou em via única você está multado em R$ 87,13 por transitar\nabaixo da metade da velocidade máxima permitida de acordo com o Artigo 219 do Código de Trânsito Brasileiro!')
