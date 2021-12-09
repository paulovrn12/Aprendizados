# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta , pinta uma área de 2m²

# 1. Quais são os dados de entrada necessários?
#   * uma largura.
#   * uma altura.

# 2. Que devo fazer com estes dados?
#   * calcular a área dessa parede (altura • largura)
#   * calcular a quatida de de tinta necessária em litros (área / 2)

# 3. Quais são as restrições deste problema?
#   * a altura e largura devem ser digitadas em metros.

# 4. Qual é o resultado esperado?
#   * apresentar na tela a litragem de tinta necessária para a pintura de uma parede.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar os valores de altura e largura (em metros) em duas variáveis.
#   * calcular a área da parede adicionando o valor a uma variável de área.
#   * calcular a litragem de tinta necessaria para essa pintura.
#   * mostrar na tela o quantos litros são necessários para a pintura dessa parede.

apres = ' LITRAGEM DE TINTA '
final = ' FIM DO CALCULO '

print('\n{:+^40}\n'.format(apres))

print('Aceitamos os valores em metros!\n')
altu = float(input('Digite a altura da parede: '))
larg = float(input('Digite a largura da parede: '))
area = altu * larg
litr = area / 2
print('Para uma parede de {:.2f}m² é preciso:\n{:.2f}ℓ de tinta.'.format(area, litr))

print('\n{:+^40}\n'.format(final))
