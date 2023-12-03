import xml.etree.cElementTree as ET
import os 

def scrapear_xspf(archivo_xspf):
    ruta_xspf = os.path.join(os.path.dirname(__file__), '..', 'lista_canciones', archivo_xspf)
    arbol = ET.parse(ruta_xspf)
    raiz = arbol.getroot()

    ns = {'xspf': 'http://xspf.org/ns/0/'}
    lista_localizaciones = []
    for lista in raiz.findall('xspf:trackList', ns):
        for cancion in lista.findall('xspf:track', ns):
            localizacion = cancion.find('xspf:location', ns).text
            lista_localizaciones.append(localizacion)
    
    return lista_localizaciones
