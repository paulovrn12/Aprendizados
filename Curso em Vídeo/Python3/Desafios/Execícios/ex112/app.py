from utilidadesCeV import moeda
from utilidadesCeV import dado

preco = dado.leiaDinheiro('Digite o preço do produto: R$')
porcentagem = float(str(input('Digite a porcentagem(%) que deseja trabalhar: ')).replace(',', '.'))
moeda.resumo(preco, porcentagem, porcentagem)