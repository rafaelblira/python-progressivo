from tkinter import *
from tkinter import messagebox

class MinhaGUI:
    def __init__(self):
        # Criamos a janela principal
        self.janela_principal = Tk()
        
        # Criando os botões
        self.botao = Button(self.janela_principal, text='Clique aqui', command=self.hello_world)
        self.botao_sair = Button(self.janela_principal, text='Sair', command=self.janela_principal.quit)
        
        # Empacotando os botões janela principal
        self.botao.pack()
        self.botao_sair.pack()
        
        # Rodando
        mainloop()

  
    def hello_world(self):
        messagebox.showinfo('Adoro a Apostila Python Progressivo!')


gui = MinhaGUI()