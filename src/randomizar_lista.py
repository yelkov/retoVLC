import random

def randomizar_lista(lista):
    # Precondicion: Verificamos si la entrada es una lista
    assert isinstance(lista,list), 'La entrada de datos no es una lista'

    # Hacemos una copia de la lista de entrada para no variar los datos originales
    lista_random = lista[:]

    # Utilizamos el método shuffle de la librería random para cambiar de orden los elementos de la lista generada.
    random.shuffle(lista_random)

    # Poscondición: para verificar que todos los elementos de nuestro input se encuentran en la segunda lista,
    # las ordenamos siguiendo el mismo criterio con la función sorted 
    assert sorted(lista_random) == sorted(lista), "La dos listas no contienen los mismos elementos"

    return lista_random