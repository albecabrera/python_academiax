# PROGRAMACION ORIENTADA A OBJETOS
# Qué es la POO
# Paradigma de programación que utiliza objetos para representar datos y comportamientos.
# Un objeto es una instancia de una clase, que define sus propiedades y métodos.
# Características de la POO
# - Encapsulamiento: Agrupa datos y métodos relacionados en una sola entidad.
# - Abstracción: Oculta los detalles de implementación y muestra solo lo necesario.
# - Herencia: Permite crear nuevas clases basadas en clases existentes, heredando sus propiedades y métodos.
# - Polimorfismo: Permite que diferentes clases implementen el mismo método de diferentes maneras.
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        raise NotImplementedError("Subclases deben implementar este método")
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"
