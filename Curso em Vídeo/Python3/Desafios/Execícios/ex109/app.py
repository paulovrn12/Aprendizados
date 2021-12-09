import moeda

preco = float(str(input('Digite o preço do produto: R$')).strip().replace(',', '.'))
porcentagem = float(str(input('Digite a porcentagem(%) que deseja trabalhar: ')).strip().replace(',', '.'))

print(f'''
A metade de {moeda.moeda(preco, True)} é {moeda.metade(preco, True)}!
O dobro de {moeda.moeda(preco, True)} é {moeda.dobro(preco, True)}!
Aumentando {porcentagem}% de {moeda.moeda(preco, True)} o novo valor fica em {moeda.aumentar(preco, porcentagem, True)}!
Diminuindo {porcentagem}% de {moeda.moeda(preco, True)} o novo valor fica em {moeda.diminuir(preco, porcentagem, True)}!
''')
