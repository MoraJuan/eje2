from ClasePersonal import Personal
from ClaseNovedades import Novedades
from ManejadorNovedades import ManejadorNovedades
import numpy as np
import csv
class ManejadorPersonal:
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, dimension=5):
        self.__personal = np.empty(dimension, dtype=Personal)
        self.__cantidad = 0
        self.__dimension = dimension

    def agregar(self, personal):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__personal.resize(self.__dimension)
        self.__personal[self.__cantidad] = personal
        self.__cantidad += 1
    
    def CargaArreglo(self):
        archivo = open('personal.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            personal = Personal(fila[0], fila[1], fila[2], fila[3], fila[4])
            self.agregar(personal)

    
    def total(self, num,Obj):
        i=0
        while(num != int(self.__personal[i].getLegajo())):
            i+=1
        print('{}'.format(Obj.sueldoLiquidar(num, int(self.__personal[i].getSueldo()))))
    
    def mostrar(self, Obj):
        otro = self.__personal
        for i in range(len(self.__personal)):
            print('-------------------------------------------------------')
            if (self.__personal[i].getNombre() > otro[i].getNombre()):
                print('Nombre {}, Apellido {}'.format(self.__personal[i].getNombre(), self.__personal[i].getApellido()))
                print('DNI {}'.format(self.__personal[i].getDni()))
                print('Sueldo: {}'.format(int(self.__personal[i].getSueldo())))
                print('{}'. format(Obj.mostrar(self.__personal[i].getLegajo(), self.__personal[i].getSueldo())))
            else:
                self.__personal[i]
            print('-------------------------------------------------------')
