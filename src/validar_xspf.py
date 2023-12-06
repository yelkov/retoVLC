import xml.etree.ElementTree as ET
import os

def validar_xspf(archivo_xspf):

    try:
        # Establecemos la ruta al archivo xspf que vamos a intentar parsear
        ruta_xspf = os.path.join(os.path.dirname(__file__), '..', 'lista_canciones', archivo_xspf)

        # Parseamos xspf usando ET y obtenemos raiz
        arbol = ET.parse(ruta_xspf)
        raiz = arbol.getroot()

        # Definimos espacio de nombres para iterar entre las etiquetas del xspf
        ns = {'xspf': 'http://xspf.org/ns/0/'}

        # Comprobamos que las etiquetas location no están vacías y de estarlo lanzamos una excepción
        for lista in raiz.findall('xspf:trackList', ns):
            for cancion in lista.findall('xspf:track', ns):
                localizacion = cancion.find('xspf:location', ns).text
                if localizacion == None or localizacion.strip() == "" :
                    raise ValueError
                else:
                    continue
                
    except ET.ParseError:
        raise ET.ParseError

    



