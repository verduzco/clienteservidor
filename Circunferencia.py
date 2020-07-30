"""
Nombre: Circunferencia.py
Objetivo: muestra como trabajar en objetos con python
Autor:
Fecha:30 de julio de 2020
"""

import math
from Punto import Punto

class Circunferencia(Punto):
    
    #Constructor
    def __init__(self, valorX, valorY, vRadio):
        # Atributos de Punto 
        Punto.__init__(self, valorX, valorY)      
        # Atributo de la circunferencia radio
        self.radio = vRadio

    def getRadio(self):
        return radio

    def setRadio(self, vRadio):
        self.radio = vRadio

    def getArea(self):
        return math.pi*math.pow(self.radio, 2)    

    def toString(self):
        return Punto.toString(self)+" y el valor del radio es: "+str(self.radio)+" y el área es: "+ str(self.getArea())




