from tkinter import *
from tkinter import messagebox

class MinhaGUI:
    def __init__(self):
        # Criamos a janela principal
        self.janela_principal = Tk()
        
        # Criando o botão
        self.botao = Button(self.janela_principal, text='Clique aqui', command=self.hello_world)
        
        # Empacotando o botão na janela principal
        self.botao.pack()
        
        # Rodando
        mainloop()

    def hello_world(self):
        messagebox.showinfo('Adoro a Apostila Python Progressivo!')


gui = MinhaGUI()