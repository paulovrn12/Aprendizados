import moeda

preco = float(str(input('Digite o preço do produto: R$')).strip().replace(',', '.'))
porcentagem = float(str(input('Digite a porcentagem(%) que deseja trabalhar: ')).strip().replace(',', '.'))
moeda.resumo(preco, porcentagem, porcentagem)
