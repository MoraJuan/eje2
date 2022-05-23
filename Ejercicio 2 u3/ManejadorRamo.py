from ClaseRamo import Ramo
from ManejadorFlores import ManejadorFlores
import csv

class ManejadorRamo:
    __lista = []
    def __init__(self):
        self.__lista = []
    
    
    def agregarUnRamo(self, UnManejador):
        num=int(input('Ingrese cantidad de flores a agregar:'))
        ramo = Ramo(num) 
        tipo= int(input('Ingrese tipon de flor *1 *2 *3 *4'))
        i=0
        for i in range(num):
           ramo.agregarflor(UnManejador.retorna(tipo))
        self.__lista.append(ramo)
    
    def mostrar(self):
        i=0
        for i in range(len(self.__lista)):
            print('{}'.format(str(self.__lista[i].getFlor())))
        