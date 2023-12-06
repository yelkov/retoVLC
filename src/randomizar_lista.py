import random

def randomizar_lista(lista):
    # Precondicion: Verificamos si la entrada es una lista
    assert isinstance(lista,list), 'La entrada de datos no es una lista'

    # Hacemos una copia de la lista de entrada para no variar los datos originales
    lista_random = lista[:]

    # Utilizamos el metodo shuffle de la libreia random para cambiar de orden los elementos de la lista generada
    random.shuffle(lista_random)

    # Poscondicion: para verificar que todos los elementos de nuestro input se encuentran en la segunda lista, 
    # vamos a crear dos diccionarios que tengan como claves los elementos de cada una de las listas. 
    # A ambos diccionarios les vamos a añadir como valor de clave 0, así a pesar de que el orden de los elementos sea diferente, 
    # si comparten exactamente los mismo elementos con el mismo valor los diccionarios tendran que ser iguales.
    diccionario_lista = {elemento: 0 for elemento in lista}
    diccionario_lista_random = {elemento: 0 for elemento in lista_random}

    assert diccionario_lista == diccionario_lista_random, "Los elementos de la lista de canciones no coinciden con los elementos de la lista randomizada"

    return lista_random
