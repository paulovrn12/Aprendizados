from kivy.app import App
from kivy.uix.button import Button

def clique():
    print('botão clicado')

def build():
    bt = Button()
    bt.text = 'Clique aqui!'
    bt.on_press = clique
    return bt

janela = App()
janela.build = build
janela.run()
