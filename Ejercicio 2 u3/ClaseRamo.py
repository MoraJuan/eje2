class Ramo:
    __tamaño = None
    __flores = []
    def __init__(self, tamaño):
        if tamaño < 4:
            self.__tamaño = tamaño
            self.__flores = []
    
    
    def getFlores(self):
        i = 0
        s = ''
        for i in range(self.__tamaño):
          s+= self.__flores[i].getNombre() + '\n'
        return s

    
    def agregarflor(self,flor):
        self.__flores.append(flor)

    def getFlor(self):
        return self.__flores
    def getTamaño(self):
        return self.__tamaño

    

