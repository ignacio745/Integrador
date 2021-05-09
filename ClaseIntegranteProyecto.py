class IntegranteProyecto:
    __idProyecto = ""
    __apellidoNombre = ""
    __dni = None
    __categoriaInvestigacion = ""
    __rol = ""
    def __init__(self, id, apellidoNombre, dni, categoriaInvestigacion, rol):
        if type(id) == str:
            self.__idProyecto = id
        else:
            
            self.__idProyecto = ""
        if type(apellidoNombre) == str:
            self.__apellidoNombre = apellidoNombre
        else:
            self.__apellidoNombre = ""

        if type(dni) == int:
            self.__dni = dni
        else:
            self.__dni = None
        
        if type(categoriaInvestigacion) == str:
            self.__categoriaInvestigacion = categoriaInvestigacion
        else:
            self.__categoriaInvestigacion = ""
        
        if type(rol) == str:
            self.__rol = rol
        else:
            self.__rol = ""
    
    def ConsultarId(self):
        return(self.__idProyecto)

    def ConsultarCategoria(self):
        return(self.__categoriaInvestigacion)
    
    def ConsultarRol(self):
        return(self.__rol)
    
