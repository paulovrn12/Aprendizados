# Desenvolva um programa que pergunte a distância de uma viagem em KM,. Calcule o preço da passagem
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viágens mais longas.

# 1. Quais são os dados de entrada necessários?
#   * um valor inteiro e positivo representando a quilometragem de uma viagem.

# 2. Que devo fazer com estes dados?
#   * calcular o preço do ônibus nessa viagem com duas faixas de valores diferentes.

# 3. Quais são as restrições deste problema?
#   * uma entrada sendo do tipo int().

# 4. Qual é o resultado esperado?
#   * exibir na tela o valor da viagem para viagens de até 200km e acima de 200km.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar um número inteiro em uma variavel 'distance'.  
#   * se 'distance' for igual ou menor que 200, calcular 'short_trip' = distance * 0.5 e exibir o valor em R$ da 'short_trip'.
#   * se 'distance' for maior que 200, calcular 'long_trip' = distance * 0.45 e exibir o valor em R$ da 'long_trip'.

distance = str(input('Digite a distância da sua viagem em km: ')).strip()
distance = int(distance)
if distance <= 200:
    short_trip = distance * 0.5
    print('O preço da sua viagem de {:.0f}km será de R${:.2f}.'.format(distance, short_trip))
elif distance > 200:
    long_trip = distance * 0.45
    print('O preço da sua viagem de {:.0f}km será de R${:.2f}.'.format(distance, long_trip))
