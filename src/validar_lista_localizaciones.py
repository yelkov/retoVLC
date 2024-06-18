import sys
from tkinter import messagebox

def validar_lista_localizaciones(lista_localizaciones):
    # Precondicion: Verificamos que el parámetro introducido es una lista.
    assert isinstance(lista_localizaciones,list), "El dato introducido no es una lista."
    

    # Iteramos sobre todos los elementos para comprobar cuantos estan vacíos.
    contador = 0
    for localizacion in lista_localizaciones:
        if localizacion == None or localizacion.strip() == "" : 
            contador += 1
    if contador > 0:
        messagebox.showinfo("Atención",f"El archivo .xspf contiene {contador} localizaciones vacías de un total de {len(lista_localizaciones)}.")
    
    # Postcondición: Verificamos que la lista de localizaciones de canciones es una lista de cadenas
    assert all(isinstance(localizacion, str) for localizacion in lista_localizaciones), "La lista de localizaciones no contiene strings."

    return lista_localizaciones          