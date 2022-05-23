import numpy as np
from ClaseFlores import Flores 
import csv
class ManejadorFlores:
    __dimension = 0
    __incremento = 5
    __cantidad = 0

    def __init__(self, dimension=5):
        self.__flores = np.empty(dimension, dtype=Flores)
        self.__cantidad = 0
        self.__dimension = dimension
        
    def agregar(self, flor):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__cantidad
            self.__flores.rezise(self.__dimension)
        self.__flores[self.__cantidad]= flor
        self.__cantidad += 1    
        
    def CargaArre(self):
        archivo = open('flores.csv')
        reader = csv.reader(archivo, delimiter= ';')
        for fila in reader:
            UnaFlor = Flores(fila[0],fila[1],fila[2], fila[3])
            self.agregar(UnaFlor)
        

    def retorna(self, numero):
        return self.__flores[numero-1]
    
    