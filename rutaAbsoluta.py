import os
"""Este modulo da por supuesto que el archivo a abrir se encuentra en la misma ubicacion que el modulo, 
caso contrario se envia la direccion del modulo que lo llama con __file__"""

def getRutaAbsoluta(nombreArchivo, direccionArchivo = __file__):
    rutaAbsoluta = os.path.dirname(os.path.abspath(direccionArchivo))
    rutaCompleta = os.path.join(rutaAbsoluta, nombreArchivo)
    return(rutaCompleta)