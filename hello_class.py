class Carro:

    def __init__(self, marca, cilindrada, kilometraje):
        self.marca = marca
        self.cilindrada = cilindrada
        self.kilometraje = kilometraje
    def encender(self):
        print("brum brum")

    def _iniciar_motor(self):
        print("Iniciando motor mor....")

carro = Carro("subaru", 1500, 20000)
carro.encender()\

print(f"marca carro: {carro.marca}")

carro2 = Carro()
print(f"marca carro2:{carro2.marca}")

 