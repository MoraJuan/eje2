from ManejadorFlores import ManejadorFlores
from ManejadorRamo import ManejadorRamo

if __name__ == '__main__':
    Obj = ManejadorFlores()
    Obj2 = ManejadorRamo()
    
    Obj.CargaArre()
    Obj2.agregarUnRamo(Obj)
    Obj2.mostrar()
    