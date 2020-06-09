import tkinter

class MinhaGUI:
    def __init__(self):
        # Criando a janela principal
        self.main_window = tkinter.Tk()
  
        # Criando os labels
        self.label1 = tkinter.Label(self.main_window, text='Curso Python Progressivo!' )
        self.label2 = tkinter.Label(self.main_window, text='www.pythonprogressivo.net' )

        # Exibindo os labels
        self.label1.pack(side='top')
        self.label2.pack(side='bottom')

        # Fazer o Tkinter exibir o looping da janela
        tkinter.mainloop()

minha_gui = MinhaGUI()