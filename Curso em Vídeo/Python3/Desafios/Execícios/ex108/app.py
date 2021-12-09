import moeda

preco = float(str(input('Digite o preço do produto: R$')).strip().replace(',', '.'))
porcentagem = float(str(input('Digite a porcentagem(%) que deseja trabalhar: ')).strip().replace(',', '.'))

print(f'''
A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}!
O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))
}!
Aumentando {porcentagem}% de {moeda.moeda(preco)} o novo valor fica em {moeda.moeda(moeda.aumentar(preco, porcentagem))}!
Diminuindo {porcentagem}% de {moeda.moeda(preco)} o novo valor fica em {moeda.moeda(moeda.diminuir(preco, porcentagem))}!
''')
