from tkinter import *
from tkinter import messagebox

class MinhaGUI:
    def __init__(self):
        # Cria janela principal
        self.janela_principal = Tk()
        
        # Cria dois frames
        self.frame_cima = Frame(self.janela_principal)
        self.frame_baixo = Frame(self.janela_principal)
        
        # Objeto IntVar dos botões
        self.radio_valor = IntVar()
        self.radio_valor.set(1)  # Para a primeira opção ficar marcada
        
        # Criando os radio buttons e o label
        self.label = Label(self.frame_cima, text='Qual o melhor curso?')
        self.python = Radiobutton(self.frame_cima, text='Python Progressivo', \
            variable = self.radio_valor, value=1)
        self.java = Radiobutton(self.frame_cima, text='Java Progressivo', \
            variable = self.radio_valor, value=2)
        self.c = Radiobutton(self.frame_cima, text='C Progressivo', \
            variable = self.radio_valor, value=3)
        
        # Empacotando o label e os radio buttons
        self.label.pack(anchor = 'w')
        self.python.pack(anchor = 'w')
        self.java.pack(anchor = 'w')
        self.c.pack(anchor = 'w')
        
        # Criando os botões
        self.botao = Button(self.frame_baixo, text='Exibe', command=self.exibe)
        self.botao_sair = Button(self.frame_baixo, text='Sair', command=self.janela_principal.quit)
        
        # Empacotando botões
        self.botao.pack(side='left')
        self.botao_sair.pack(side='left')
        
        # Empacotando os frames na janela principal
        self.frame_cima.pack()
        self.frame_baixo.pack()
        
        # Rodando
        mainloop()
  
    def exibe(self):
        nome = str(self.radio_valor.get())
        messagebox.showinfo('Resposta','Você escolheu a opçao ' + nome)
   
  
gui = MinhaGUI()