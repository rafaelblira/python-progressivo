import tkinter

class MinhaGUI:
    def __init__(self):
        # Criando a janela principal
        self.main_window = tkinter.Tk()
    
        # Criando a label Ceará e exibindo
        self.label = tkinter.Label(self.main_window, text="Ceará", bg="black", fg="white")
        self.label.pack(fill = tkinter.Y, side='left')
        
        # Criando a label Flamengo e exibindo
        self.label = tkinter.Label(self.main_window, text="Flamengo", bg="red", fg="black")
        self.label.pack(fill = tkinter.Y, side='left')
        
        # Criando a label Palmeiras e exibindo
        self.label = tkinter.Label(self.main_window, text="Palmeiras", bg="green", fg="black")
        self.label.pack(fill = tkinter.Y, side='left')

        # Fazer o Tkinter exibir o looping da janela
        tkinter.mainloop()

minha_gui = MinhaGUI()