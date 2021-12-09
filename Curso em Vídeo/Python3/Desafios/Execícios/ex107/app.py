import moeda

preco = float(str(input('Digite o preço do produto: R$ ')).strip().replace(',', '.'))
porcentagem = float(str(input('Digite a porcentagem(%) que deseja trabalhar: ')).strip().replace(',', '.'))

acrescimo = moeda.aumentar(preco, porcentagem)
desconto = moeda.diminuir(preco, porcentagem)
metade = moeda.metade(preco)
dobro = moeda.dobro(preco)

print(f'''
A metade de R$ {preco:.2f} é R$ {metade:.2f}!
O dobro de R$ {preco:.2f} é R$ {dobro:.2f}!
Aumentando {porcentagem}% de R$ {preco:.2f} o novo valor fica em R$ {acrescimo:.2f}!
Diminuindo {porcentagem}% de R$ {preco:.2f} o novo valor fica em R$ {desconto:.2f}!
''')
