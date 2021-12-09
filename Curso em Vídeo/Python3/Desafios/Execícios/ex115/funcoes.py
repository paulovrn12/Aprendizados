def menu():
    from time import sleep
    sleep(1)
    menu = print('╔════════════════════════════════╗\n║ SISTEMA DE CADASTRO DE PESSOAS ║\n╠════════════════════════════════╣\n║ ----- OPÇÕES DO SISTEMA ------ ║\n║ 1 - CADASTRAR NOVA PESSOA      ║\n║ 2 - LISTAR PESSOAS CADASTRADAS ║\n╚════════════════════════════════╝')
    sleep(1)
    return menu

def leituraOpcao(mensagem='Opção: '):
    opcoes = [1, 2]
    while True:
        try:
            entrada = str(input(mensagem)).strip()
            opcao = int(entrada)
        except (ValueError, TypeError, KeyboardInterrupt):
            print(f'Opção \"{entrada}\" inválida!')
            continue
        else:
            if opcao not in opcoes:
                print(f'A opção \"{entrada}\" é inválida!')
                continue
            else:
                break
    return opcao

def leituraNome(mensagem='Nome: '):
    while True:
        try:
            nome = str(input(mensagem)).strip()
        except Exception:
            print('Digite um nome válido!')
            continue
        else:
            break
    return nome

def leituraIdade(mensagem='Idade: '):
    while True:
        try:
            entrada = str(input(mensagem)).strip()
            idade = int(entrada)
        except (ValueError, TypeError, KeyboardInterrupt):
            print(f'Idade \"{entrada}\" inválida!')
            continue
        else:
            break
    return idade

def cadastroPessoas(diretorio, nome='<desconhecido>', idade=0):
    try:
        with open(diretorio, 'r', encoding="utf-8") as arquivo:
            arquivo.read()
    except FileNotFoundError:
        with open(diretorio, 'w', encoding="utf-8") as arquivo:
            arquivo.write(f'Nome: {nome}, Idade: {idade}')
    else:
        with open(diretorio, 'a', encoding="utf-8") as arquivo:
            arquivo.write(f'\nNome: {nome}, Idade: {idade}')

def listagemPessoas(diretorio):
    try:
        with open(diretorio, 'r', encoding="utf-8") as arquivo:
            listagem = arquivo.read()
    except FileNotFoundError:
        print('Nenhuma pessoa foi cadastrada ainda, escolha a opção 1, relativa ao cadastro de pessoas!')
    else:
        return print(f'\n{listagem}\n')
