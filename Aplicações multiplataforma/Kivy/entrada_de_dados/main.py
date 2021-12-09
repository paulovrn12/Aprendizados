from kivy.app import App
from kivy.uix.textinput import TextInput

def build():
    txinp = TextInput()
    txinp.text = 'Meu primeiro bloco de notas!'
    return txinp

janela = App()
janela.build = build
janela.run()