import xml.etree.ElementTree as ET
import sys
import os

def obtener_localizaciones(archivo_xspf):
    # Ruta al archivo xspf que usaremos para parsear. Necesitamos introducirlo antes como parametro
    # pero siempre lo va a buscar en la carpeta 'lista_canciones'
    ruta_xspf = os.path.join(os.path.dirname(__file__), '..', 'lista_canciones', archivo_xspf)
        
    try:
        # Parsear xspf usando ET y obtenemos raiz, que utilizaremos despues para crear nuestra estructura de datos, que sera una lista
        arbol = ET.parse(ruta_xspf)
        raiz = arbol.getroot()

        # Definimos espacio de nombres para iterar entre las etiquetas del xspf
        ns = {'xspf': 'http://xspf.org/ns/0/'}

        # Inicializamos la lista que sera devuelta e iteramos sobre los elementos a scrapear
        lista_localizaciones = []
        for lista in raiz.findall('xspf:trackList', ns):
            for cancion in lista.findall('xspf:track', ns):
                localizacion = cancion.find('xspf:location', ns).text
                lista_localizaciones.append(localizacion)

        return lista_localizaciones
    
    except ET.ParseError:
        print("El archivo está vacío o no sigue correctamente el formato .xspf.")
        sys.exit(1)

    except FileNotFoundError:
        print("No se encuentra el archivo .xspf en la carpeta lista_prueba.")
        sys.exit(1)