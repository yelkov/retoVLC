import random

def randomizar_lista(lista):
    # Precondicion: Verificar si la entrada es una lista
    assert isinstance(lista,list), f'La entrada de datos {lista} no es una lista'

    # Hacer una copia de la lista de entrada para no variar los datos originales
    lista_random = lista[:]

    return lista_random
