class Gato :
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido
    
    def saludoDeGato(self):
        print("Hola, yo soy", self.nombre,"y puedo", self.sonido)

class Perro(Gato):
    def saludodePerro(self):
        print("Hola, yo soy", self.nombre,"y puedo", self.sonido)

michu = Gato("michu", "maullar")
michu.saludoDeGato()

toby = Perro("toby", "ladrar")
toby.saludodePerro()
