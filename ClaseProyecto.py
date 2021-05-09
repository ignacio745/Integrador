class Proyecto:
    __idProyecto = ""
    __titulo = ""
    __palabrasClave = ""
    __puntos = 0
    def __init__(self, id, titulo, palabrasClave):
        if type(id) == str:
            self.__idProyecto = id
        else:
            self.__idProyecto = ""
        if type(titulo) == str:
            self.__titulo = titulo
        else:
            self.__titulo = ""
        if type(palabrasClave) == str:
            self.__palabrasClave = palabrasClave
        else:
            self.__palabrasClave = ""
        self.__puntos = 0
    
    def ActualizarPuntos(self, puntos):
        if type(puntos) == int:
            self.__puntos = puntos
    
    def ConsultarId(self):
        return(self.__idProyecto)
    
    def ConsultarPuntos(self):
        return(self.__puntos)

    def ConsultarTitulo(self):
        return(self.__titulo)
    
    def ConsultarPalabrasClave(self):
        return(self.__palabrasClave)
    
    def __gt__(self, otro):
        resultado = None
        if type(otro) == Proyecto:
            resultado = self.ConsultarPuntos() > otro.ConsultarPuntos()
        return(resultado)