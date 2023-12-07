import sys
import xml.etree.ElementTree as ET
from src.parsear_xspf import obtener_localizaciones
from src.validar_lista_localizaciones import validar_lista_localizaciones
from src.randomizar_lista import randomizar_lista
from src.llamar_vlc import llamar_vlc

def reproductor_random(archivo_xspf):
    lista_localizaciones = obtener_localizaciones(archivo_xspf)
    validar_lista_localizaciones(lista_localizaciones)
    lista_randomizada = randomizar_lista(lista_localizaciones)
    llamar_vlc(lista_randomizada)


if __name__ == '__main__' :
    try:
        archivo_xspf = sys.argv[1]
        reproductor_random(archivo_xspf)
    except IndexError:
        print("Recuerde indicar la lista a reproducir siguiendo el formato: app.py lista_de_canciones.xspf")
    