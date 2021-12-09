# IMPORTAÇÕES   
from tkinter import *
import robocopy as rc



def TelaInicio():
    # VARIÁVEIS ÚTEIS
    icon_dir = r'Scripts\Advanced Backup v.0.1 alpha\Application\data\icon\adv.ico'

    # GUI
    tela = Tk()
    tela.title('Início - Advanced Backup v.0.1 alpha')
    CentroMonitor(tela, 400, 180)
    tela.iconbitmap(icon_dir)
    tela.resizable(False, False)
    # WIDGETS
    orient_tx = Label(tela, text='Selecione abaixo a opção de Backup desejada!', width=53)
    copy_paste_bt = Button(tela, text='Copiar e Colar\n(Simples)')
    robocopy_bt = Button(tela, text='Backup Robocopy\n(Avançado)', command=TelaRobocopy)
    cloud_bt = Button(tela, text='Backup Externo\n(Cloud / Nuvem)')
    github_bt = Button(tela, text='Backup de Código\n(Git / GitHub)')
    # LAYOUTS
    orient_tx.grid(sticky='we', columnspan=2, padx=10, pady=10)
    copy_paste_bt.grid(sticky='we', row=1, column=0, padx=10, pady=10)
    robocopy_bt.grid(sticky='we', row=1, column=1, padx=10, pady=10)
    cloud_bt.grid(sticky='we', row=2, column=0, padx=10, pady=10)
    github_bt.grid(sticky='we', row=2, column=1, padx=10, pady=10)
    # END GUI
    tela.mainloop()

def TelaRobocopy(ultimo_backup='Sem histórico!'):
    # FUNÇÕES ÚTEIS
    def CorDiretorio(label):
        if ultimo_backup == 'Sem histórico!':
            label['fg'] = '#ff0000'
            return label['fg']
        else:
            label['fg'] = '#00ff00'
            return label['fg']
    #def BotaoRepetirBackup():
    #    if ultimo_backup == 'Sem histórico!':
    #        
    #        return 
    #    else:
    #
    #        return
    # VARIÁVEIS ÚTEIS
    icone_dir = r'Scripts\Advanced Backup v.0.1 alpha\Application\data\icon\adv.ico'
    # GUI
    tela = Tk()
    tela.title('Robocopy - Advanced Backup v.0.1 alpha')
    CentroMonitor(tela, 400, 180)
    tela.iconbitmap(icone_dir)
    tela.resizable(False, False)
    # WIDGETS
    texto_opcao = Label(tela, text='Você selecionou a opção Backup Robocopy')
    texto_ajuda = Label(tela, text='Nessa opção é possível realizar um backup dos seus arquivos com o\ndetalhamento completo de tudo o que foi feito no processo.', justify=LEFT)
    texto_historico = Label(tela, text=f'Ultimo backup:', justify=LEFT)
    texto_diretorio = Label(tela, text=f'{ultimo_backup}', justify=LEFT, anchor=W,  fg='#000000')
    CorDiretorio(texto_diretorio)
    botao_rep_backup = Button(tela, text='Repetir os diretórios do\nultimo backup realizado', justify=CENTER, width=22)
    botao_selec_dir = Button(tela, text='Selecionar diretórios de orígem\ne destino do seu backup', justify=CENTER)
    # LAYOUTS
    texto_opcao.grid(row=0, column=0, columnspan=4, sticky='we', padx=10, pady=10)
    texto_ajuda.grid(row=1, column=0, rowspan=2, columnspan=4, sticky=W, padx=10)
    texto_historico.grid(row=3, column=0, columnspan=3, sticky=W, padx=10)
    texto_diretorio.grid(row=3, column=1, sticky=E, padx=10)
    botao_rep_backup.grid(row=4, column=0, rowspan=2, columnspan=4, sticky=W,padx=10, pady=10)
    botao_selec_dir.grid(row=4, column=2, rowspan=2, columnspan=4, sticky=E,padx=10, pady=10)

    # END GUI
    tela.mainloop()

