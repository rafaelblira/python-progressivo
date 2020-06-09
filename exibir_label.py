import tkinter

class MinhaGUI:
    def __init__(self):
        # Criando a janela principal
        self.main_window = tkinter.Tk()
  
        # Criando um Label com o texto 'Curso Python Progressivo'
        self.texto = tkinter.Label(self.main_window, text='Curso Python Progressivo! ' )

        # Chamando o metodo pack() da função Label()
        self.texto.pack()

        # Fazer o Tkinter exibir o looping da janela
        tkinter.mainloop()

minha_gui = MinhaGUI()