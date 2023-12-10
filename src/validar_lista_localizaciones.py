import sys

def validar_lista_localizaciones(lista_localizaciones):
    # Precondicion: Verificamos que el parámetro introducido es una lista.
    assert isinstance(lista_localizaciones,list), "El dato introducido no es una lista."
    

    # Iteramos sobre todos los elementos para comprobar que ninguno está vacío.
    for localizacion in lista_localizaciones:
        if localizacion == None or localizacion.strip() == "" : 
            print("El archivo .xspf contiene localizaciones vacías.")
            sys.exit(1)
        else:
            continue
    
    # Postcondición: Verificamos que la lista de localizaciones de canciones es una lista de cadenas
    assert all(isinstance(localizacion, str) for localizacion in lista_localizaciones), "La lista de localizaciones no contiene strings."

    return lista_localizaciones          