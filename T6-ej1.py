
#En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
#Color,Ruedas,Puertas

#Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
#Velocidad,Cilindrada

#Por último, tendrás que crear un objeto de laclase Coche y mostrarlo por consola.

class Vehiculo: #no se le crea objeto a esta clase
    def description(self):
        print("I'm a Vehicle!")
        
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        
class Coche (Vehiculo):
    #super().__init()
    #aqui podria hacer un atributo de clase: ruedas = 4, porque todos los coches tienen 4 ruedas, pero en este caso lo heredo de vehiculo
    
    def __init__(self,  cilindrada,color, ruedas, puertas, velocidad=3):
        Vehiculo.__init__(self, color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    

c = Coche("a","v","c", "f")
c.description ()
c.puertas = 2
print(c.puertas)


#print(Car.velocidad)
#print(Car.cilindrada)


#ejercutar el init de la clase padre:vehiculo.__init__(self,color) o...
#super().__init__(color)
#LAS clases en python son diccionarios!! no existen clases como tal


