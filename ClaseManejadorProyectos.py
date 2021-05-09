from ClaseProyecto import Proyecto
from ClaseManejadorIntegrantesProyecto import ManejadorIntegrantesProyecto
import csv
import rutaAbsoluta

class ManejadorProyectos:
    __proyectos = []
    def __init__(self):
        self.__proyectos = []

    def CargarDesdeArchivo(self, nombreArchivo):
        rutaArchivo = rutaAbsoluta.getRutaAbsoluta(nombreArchivo, __file__)
        archivo = open(rutaArchivo)
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                unProyecto = Proyecto(fila[0], fila[1], fila[2])
                self.__proyectos.append(unProyecto)
        archivo.close()

    def ActualizarPuntos(self, unManejadorIntegrantes):
        if type(unManejadorIntegrantes) == ManejadorIntegrantesProyecto:
            print(" Calculando puntos de los proyectos ".center(120, "-"))
            for unProyecto in self.__proyectos:
                print("Calculando puntos del proyecto {0}".format(unProyecto.ConsultarId()))
                puntos = unManejadorIntegrantes.CalcularPuntaje(unProyecto.ConsultarId())
                unProyecto.ActualizarPuntos(puntos)

    def OrdenarProyectos(self):
        self.__proyectos.sort(reverse=True)
    
    def MostrarProyectos(self):
        self.OrdenarProyectos()
        print(" Datos de los proyectos ".center(120, "-"))
        for unProyecto in self.__proyectos:
            print("Proyecto: {0}".format(unProyecto.ConsultarId()))
            print("Titulo: {0}".format(unProyecto.ConsultarTitulo()))
            print("Palabras clave: {0}".format(unProyecto.ConsultarPalabrasClave()))
            print("Puntos: {0}".format(unProyecto.ConsultarPuntos()))