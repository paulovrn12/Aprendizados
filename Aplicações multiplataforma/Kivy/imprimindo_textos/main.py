from kivy.app import App
from kivy.uix.label import Label

def build():
    lb = Label()
    lb.text = 'Primeira aplicação!'
    lb.italic = True
    lb.font_size = 30
    return lb

app = App()
app.build = build
app.run()

