from ClaseManejadorIntegrantesProyecto import ManejadorIntegrantesProyecto
from ClaseManejadorProyectos import ManejadorProyectos
import limpiador

if __name__ == '__main__':
    limpiador.clearScreen()

    unManejadorProyectos = ManejadorProyectos()
    unManejadorIntegrantes = ManejadorIntegrantesProyecto()
    
    unManejadorProyectos.CargarDesdeArchivo("proyectos.csv")
    unManejadorIntegrantes.CargarDesdeArchivo("integrantesProyecto.csv")

    unManejadorProyectos.ActualizarPuntos(unManejadorIntegrantes)
    unManejadorProyectos.MostrarProyectos()

    input(" Presione Enter para salir ".center(120, "-"))
    limpiador.clearScreen()