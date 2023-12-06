import sys
import xml.etree.ElementTree as ET
from src.validar_xspf import validar_xspf
from src.parsear_xspf import obtener_localizaciones
from src.randomizar_lista import randomizar_lista
from src.llamar_vlc import llamar_vlc

def reproductor_random(archivo_xspf):
    try:
        validar_xspf(archivo_xspf)
        lista_localizaciones = obtener_localizaciones(archivo_xspf)
        lista_randomizada = randomizar_lista(lista_localizaciones)
        llamar_vlc(lista_randomizada)

    except FileNotFoundError:
        print("No se encuentra el archivo .xspf en la carpeta lista_prueba.")
    except ValueError:
        print("El archivo .xspf contiene localizaciones vacías.")
    except ET.ParseError:
        print("El archivo está vacío o no sigue correctamente el formato .xspf.")


if __name__ == '__main__' :
    try:
        archivo_xspf = sys.argv[1]
        reproductor_random(archivo_xspf)
    except IndexError:
        print("Recuerde indicar la lista a reproducir siguiendo el formato: app.py lista_de_canciones.xspf")
    