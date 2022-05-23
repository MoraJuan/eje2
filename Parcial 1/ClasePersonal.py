class Personal:
    __legajo= None
    __dni= None 
    __apellido=None 
    __nombre=None  
    __sueldo= None 

    def __init__(self, legajo, dni,apellido,nombre,sueldo):
        self.__legajo = legajo
        self.__dni = dni
        self.__apellido =apellido
        self.__nombre = nombre
        self.__sueldo = sueldo

    def getLegajo(self):
        return self.__legajo
    def getDni(self):
        return self.__dni
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getSueldo(self):
        return self.__sueldo

    def __gt__(self, other):
        Valor = False
        if self.__nombre > other.getNombre():
            Valor = True
        return Valor
            
