from tkinter import *

class MinhaGUI:
    def __init__(self):
        # Cria janela principal
        self.janela_principal = Tk()

        # Define o título
        self.janela_principal.title("Calcula IMC")
        
        # Cria três frames
        self.frame_cima = Frame(self.janela_principal)
        self.frame_meio = Frame(self.janela_principal)
        self.frame_baixo = Frame(self.janela_principal)
        self.frame_baixo2 = Frame(self.janela_principal)
        
        # No frame de cima, um label e uma entry
        self.label_peso = Label(self.frame_cima, text='Digite seu peso: ')
        self.label_altura = Label(self.frame_meio, text='Digite sua altura: ')
        self.entrada_peso = Entry(self.frame_cima, width = 30)
        self.entrada_altura = Entry(self.frame_meio, width = 30)
        
        # Empacotando os labels e entradas no primeiro e segundo frame
        self.label_peso.pack(side='left')
        self.label_altura.pack(side='left')
        self.entrada_peso.pack(side='left')
        self.entrada_altura.pack(side='left')
        
        # Labels do frame de baixo
        self.label_resultado = Label(self.frame_baixo, text='Seu IMC é:  ')
        self.label_dinamica = StringVar()
        self.label3 = Label(self.frame_baixo, textvariable=self.label_dinamica)
        self.label_situacao = Label(self.frame_baixo, text='Situação:  ')
        self.label_dinamica2 = StringVar()
        self.label4 = Label(self.frame_baixo, textvariable=self.label_dinamica2)
        
        # Empacotando as labels do baixo
        self.label_resultado.pack(side='left')
        self.label3.pack(side='left')
        self.label_situacao.pack(side='left')
        self.label4.pack(side='left')
        
        # Criando os botões
        self.botao = Button(self.frame_baixo2, text='Exibe', command=self.calcula)
        self.botao_sair = Button(self.frame_baixo2, text='Sair', command=self.janela_principal.quit)
        
        # Empacotando botões e label
        self.botao.pack(side='left')
        self.botao_sair.pack(side='left')
        
        # Empacotando os frames na janela principal
        self.frame_cima.pack()
        self.frame_meio.pack()
        self.frame_baixo.pack()
        self.frame_baixo2.pack()
        
        # Rodando
        mainloop()
  
    #Calculando
    def calcula(self):
        peso = self.entrada_peso.get()
        altura = self.entrada_altura.get()

        resp = round((float(peso))/(float(altura)*float(altura)),2)    
        self.label_dinamica.set(resp)

        if resp < 17:
            situacao = "Muito abaixo do peso"
        elif  17 <= resp <= 18.49:
            situacao = "Abaixo do peso"
        elif 18.50 <= resp <=24.99:
            situacao = "Peso normal"
        elif 25 <= resp <=29.99:
            situacao = "Acima do peso"
        elif 30 <= resp <=34.99:
            situacao = "Obesidade I"
        elif 35 <= resp <= 39.99:
            situacao = "Obesidade II (severa)"
        else:
            situacao = "Obesidade III (morbida)"
        self.label_dinamica2.set(situacao)


  
gui = MinhaGUI()