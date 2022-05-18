from zooAnimales.animal import Animal
class Reptil(Animal):
    totalReptiles=0
    listado =[]
    serpientes=0
    iguanas=0

    def __init__(self,nombre,edad,habitat,genero,colorEscamas,largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil.totalReptiles+=1
        self.listado.append(self)
        
    @classmethod
    def cantidadReptiles(cls): return cls.totalReptiles 
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        cls.iguanas+=1
        return Reptil(nombre, edad, "humdeal", genero, "verde", 3)
        
    @classmethod
    def crearSerpiente(cls,nombre, edad, genero):
        cls.serpientes+=1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)

    def movimiento(self):
        return "reptar"

    def setColorEscamas(self,a): self._colorEscamas=a
    def getColorEscamas(self): return self._colorEscamas
    def setLargoCola(self, a): self._largoCola = a
    def getLargoCola(self): return self._largoCola