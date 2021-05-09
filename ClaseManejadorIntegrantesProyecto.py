from ClaseIntegranteProyecto import IntegranteProyecto
import csv
import rutaAbsoluta

class ManejadorIntegrantesProyecto:
    categorias = ["I", "II", "III", "IV"]
    roles = ["director", "codirector", "integrante"]
    __integrantesProyecto = []
    
    def __init__(self):
        self.__integrantesProyecto = []
    
    def CargarDesdeArchivo(self, nombreArchivo):
        rutaArchivo = rutaAbsoluta.getRutaAbsoluta(nombreArchivo, __file__)
        archivo = open(rutaArchivo)
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = False
            elif fila[2].isdigit() and 1<=int(fila[2]) and (fila[3] in self.categorias) and (fila[4] in self.roles):
                unIntegranteProyecto = IntegranteProyecto(fila[0], fila[1], int(fila[2]), fila[3], fila[4])
                self.__integrantesProyecto.append(unIntegranteProyecto)
        archivo.close()

    def ConsultarIntegrantes(self, id):
        cont = 0
        for unIntegrante in self.__integrantesProyecto:
            if unIntegrante.ConsultarId() == id:
                cont += 1
        return(3 <= cont)

    def ConsultarMiembro(self, id, rol, categorias = ["I", "II", "III", "IV"]):
        cumple = False
        if type(categorias) == list:
            for unIntegrante in self.__integrantesProyecto:
                if unIntegrante.ConsultarId() == id and unIntegrante.ConsultarRol() == rol and unIntegrante.ConsultarCategoria() in categorias:
                    cumple = True
                    break
        return(cumple)



    def CalcularPuntaje(self, id):
        puntos = 0
        
        if self.ConsultarIntegrantes(id):
            puntos += 10
        else:
            puntos -= 20
            print("El Proyecto debe tener como mínimo 3 integrantes")
        
        if self.ConsultarMiembro(id, "director", ["I", "II"]):
            puntos += 10
        else:
            puntos -= 5
            print("El Director del Proyecto debe tener categoria I o II")

        if self.ConsultarMiembro(id, "codirector", ["I", "II", "III"]):
            puntos += 10
        else:
            puntos -= 5
            print("El Codirector del Proyecto debe tener como mínimo categoría III")

        director = self.ConsultarMiembro(id, "director")

        if not director:
            print("El Proyecto debe tener un Director")
        
        codirector = self.ConsultarMiembro(id, "codirector")

        if not codirector:
            print("El Proyecto debe tener un Codirector")
        
        if (not director) or (not codirector):
            puntos -= 10
        
        return (puntos)