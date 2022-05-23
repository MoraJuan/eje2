class Novedades:
    __legajo = None
    __importe = None
    __concepto = None
    __codigo = None

    def __init__(self, legajo, importe ,concepto, codigo):
        self.__legajo = legajo
        self.__importe = importe
        self.__concepto = concepto
        self.__codigo = codigo
    
    def getLegajo(self):
        return self.__legajo
    
    def getImporte(self):
        return self.__importe
    
    def getConcepto(self):
        return self.__concepto
    
    def getCodigo(self):
        return str(self.__codigo)