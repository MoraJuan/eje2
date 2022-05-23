from ManejadorPersonal import ManejadorPersonal
from ManejadorNovedades import ManejadorNovedades


class Menu:
    opcion=None
    
    def __init__(self):
        self.__opcion=0
    def mostrarmenu(self):
        Obj=ManejadorPersonal()
        Obj2 = ManejadorNovedades()
        while self.__opcion!=-1:
            print('[1]')
            print('[2] ')
            print('[3] ')
            self.__opcion=input('\nIngrese numero: ')
            if self.__opcion=='1':
                   Obj.CargaArreglo()
                   Obj2.cargaLista()
                   num = int(input('Numero'))
                   Obj.total(num, Obj2)
            elif self.__opcion=='2':
                Obj.CargaArreglo()
                Obj2.cargaLista()
                Obj.mostrar(Obj2)
                

                
            
                