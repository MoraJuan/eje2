from ClaseNovedades import Novedades

import numpy as np
import csv
class ManejadorNovedades:
    __lista = []
    
    
    def __init__(self):
        self.__lista = []
    
    def cargaLista(self):
        archivo = open('novedades.csv')
        reader = csv.reader(archivo, delimiter = ';')
        for fila in reader:
            UnNovedades = Novedades(fila[0], fila[1], fila[2], fila[3])
            self.__lista.append(UnNovedades)
       
        
    def getLista(self):
        return self.__lista

    def sueldoLiquidar(self, num, sueldo):
        total=0
        i=0
        while int(self.__lista[i].getLegajo()) != int(num):
            i+=1
        if int(self.__lista[i].getLegajo()) == int(num):
            if str(self.__lista[i].getCodigo()) != 'D':
                total = int(self.__lista[i].getImporte()) + int(sueldo)
            else: 
                total = int(sueldo) - int(self.__lista[i].getImporte())
            return total
    
    def mostrar(self, Legajo, sueldo):
        total=0
        print('Codigo     Concepto        Importe')

        for i in range(len(self.__lista)):
            if(self.__lista[i].getLegajo() == Legajo):
                print('{}----{}----{}'.format(self.__lista[i].getCodigo(), self.__lista[i].getConcepto(), self.__lista[i].getImporte()))
            if str(self.__lista[i].getCodigo()) != 'D':
                    total = int(self.__lista[i].getImporte()) + int(sueldo)
            else: 
                    total = int(sueldo) - int(self.__lista[i].getImporte())
        print('total:{}'.format(total))
                
                
