import xml.etree.cElementTree as ET
import os 

def scrapear_xspf(archivo_xspf):
    # Precondición: Verificar si la entrada es un archivo XSPF
    assert archivo_xspf.endswith('.xspf'), f"El archivo {archivo_xspf} no tiene la extensión .xspf."

    #ruta al archivo xspf
    ruta_xspf = os.path.join(os.path.dirname(__file__), '..', 'lista_canciones', archivo_xspf)
    
    #parsear xspf usando ET
    arbol = ET.parse(ruta_xspf)
    raiz = arbol.getroot()

    #definir espacio de nombres 
    ns = {'xspf': 'http://xspf.org/ns/0/'}

    #inicializar lista que sera devuelta e iterar sobre los elementos a scrapear
    lista_localizaciones = []
    for lista in raiz.findall('xspf:trackList', ns):
        for cancion in lista.findall('xspf:track', ns):
            localizacion = cancion.find('xspf:location', ns).text
            lista_localizaciones.append(localizacion)
    
    # Postcondición: Verificar que la lista de localizaciones de canciones es una lista de cadenas
    assert all(isinstance(localizacion, str) for localizacion in lista_localizaciones), "La lista de localizaciones no contiene cadenas."

    return lista_localizaciones
