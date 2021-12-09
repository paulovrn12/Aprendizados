import funcoes as f

diretorio = 'E:\Arquivos de Programas\Scripts\Curso em Vídeo\Desafios\Execícios\ex115\dados_cadastrais\pessoas.txt'
while True:
    menu = f.menu()
    opcao = f.leituraOpcao('Digite a opção desejada: ')
    if opcao == 1:
        nome = f.leituraNome('Digite o nome da pessoa: ')
        idade = f.leituraIdade('Digite a idade da pessoa: ')
        f.cadastroPessoas(diretorio, nome, idade)
    if opcao == 2:
        f.listagemPessoas(diretorio)

    acao = str(input('Deseja realizar mais alguma ação? [S/N]: ')).strip().upper()[0]
    while acao not in 'SN':
        print('Digite apenas S para Sim ou N para Não!')
        acao = str(input('Deseja realizar mais alguma ação? [S/N]: ')).strip().upper()[0]
    if acao == 'S':
        print()
        continue
    if acao == 'N':
        print('\nObrigado por utilizar o meu programa!\nVolte sempre!\n')
        break
