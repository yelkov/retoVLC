import os
import sys

def buscar_archivos_xspf():
    try:
        #indicamos la ruta del directorio donde deben colocarse los archivos .xspf
        directorio = os.path.join(os.path.dirname(__file__), '..', 'lista_canciones')

        #obtenemos con el metodo listdir todo el contenido del directorio
        contenido = os.listdir(directorio)

        #creamos una lista para almacenar todos los archivos .xspf que se encuentran
        lista_archivos = []

        for archivo in contenido:
            if archivo.endswith(".xspf"):
                lista_archivos.append(archivo)
        
        return lista_archivos

    
    except FileNotFoundError:
        print("El directorio 'lista_canciones' no se encuentra.")
        sys.exit(1)


