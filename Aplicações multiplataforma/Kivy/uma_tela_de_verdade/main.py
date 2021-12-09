from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

def build():
    layout = FloatLayout()
    tx = TextInput()
    bt = Button()
    
    tx.text = 'Digite algo!'
    
    bt.text = 'Clique Aqui!'
    
    return layout

janela = App()
janela.build = build
janela.run()















