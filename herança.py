class Veiculo:
    def __init__(self, tipo, modelo, km):
        self.tipo = tipo
        self.modelo = modelo
        self.km = km
  
class Carro (Veiculo):
    def __init__(self, tipo, modelo, km, portas):
        Veiculo.__init__(self, tipo, modelo, km)
        self.portas = portas

class Moto (Veiculo):
    def __init__(self, tipo, modelo, km, cilindradas):
        Veiculo.__init__(self, tipo, modelo, km)
        self.cilindradas = cilindradas
 
    def exibe(self):
        print(self.tipo, "modelo", self.modelo, "com", self.km, "km rodados e", self.cilindradas, "cilindradas.")
  

honda = Moto("Moto", "Honda CG150", "10000", 1500)
honda.exibe()