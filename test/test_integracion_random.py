from src.validar_lista_localizaciones import validar_lista_localizaciones
from src.parsear_xspf import obtener_localizaciones
from src.randomizar_lista import randomizar_lista

def test_integracion_longitud():
    lista_localizaciones_prueba = validar_lista_localizaciones( obtener_localizaciones('lista_prueba.xspf'))
    lista_randomizada_prueba = randomizar_lista(lista_localizaciones_prueba)
    assert len(lista_localizaciones_prueba) == len(lista_randomizada_prueba)

    lista_localizaciones_creedence = validar_lista_localizaciones(obtener_localizaciones('creedence.xspf'))
    lista_randomizada_creedence = randomizar_lista(lista_localizaciones_creedence)
    assert len(lista_localizaciones_creedence) == len(lista_randomizada_creedence)

def test_integracion_num_elemetos():
    lista_localizaciones_prueba = validar_lista_localizaciones(obtener_localizaciones('lista_prueba.xspf'))
    lista_randomizada_prueba = randomizar_lista(lista_localizaciones_prueba)
    assert len(lista_randomizada_prueba) == 5

    lista_localizaciones_creedence = validar_lista_localizaciones(obtener_localizaciones('creedence.xspf'))
    lista_randomizada_creedence = randomizar_lista(lista_localizaciones_creedence)
    assert len(lista_localizaciones_creedence) == 25

def test_integracion_diferentes():
    lista_localizaciones_prueba = validar_lista_localizaciones(obtener_localizaciones('lista_prueba.xspf'))
    lista_randomizada_prueba = randomizar_lista(lista_localizaciones_prueba)
    assert lista_localizaciones_prueba != lista_randomizada_prueba

    lista_localizaciones_creedence = validar_lista_localizaciones(obtener_localizaciones('creedence.xspf'))
    lista_randomizada_creedence = randomizar_lista(lista_localizaciones_creedence)
    assert lista_localizaciones_creedence != lista_randomizada_creedence
