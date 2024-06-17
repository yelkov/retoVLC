import tkinter as tk
from buscar_xspf import buscar_archivos_xspf
from parsear_xspf import obtener_localizaciones
from validar_lista_localizaciones import validar_lista_localizaciones
from randomizar_lista import randomizar_lista
from llamar_vlc import llamar_vlc

def iniciar_interfaz():

    # ======== RAIZ =========

    raiz = tk.Tk()
    raiz.title("VLC mixer")
    raiz.config(bg="lightgrey")
    raiz.iconbitmap(r"imagenes\\logo.ico")
    raiz.grid_columnconfigure(0,weight=1)

    # ======== FRAME PRINCIPAL =========

    frame_principal = tk.Frame(raiz,width=640,height=396)
    frame_principal.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")
    frame_principal.grid_propagate(False)

    frame_principal.grid_columnconfigure(0, weight=1)

        # ------- texto superior --------

    texto_principal = tk.Label(frame_principal,text="¡Bienvenido a VLC mixer de canciones!",justify="center")
    texto_principal.grid(row=0,column=0,sticky="n")

        # ------- texto instrucciones --------

    texto_instrucciones = tk.Label(frame_principal, text="Para utilizar el programa, puede seleccionar una lista de canciones y a continuación hacer click en randomizar.")
    texto_instrucciones.grid(row=2,column=0,sticky="n")

        # ------- menú de seleccion --------

    archivo_seleccionado = tk.StringVar()
    archivo_seleccionado.set("Seleccione una lista")
    lista_archivos = buscar_archivos_xspf()
    selector = tk.OptionMenu(frame_principal,archivo_seleccionado,*lista_archivos)
    selector.grid(row=3,column=0,sticky="s")

        # ------- botón de randomizar --------
    boton_randomizar = tk.Button(frame_principal,text="¡Randomiza!",command=lambda:randomizar(archivo_seleccionado.get()))
    boton_randomizar.grid(row=4,column=0,sticky="s")

    raiz.mainloop()





def randomizar(archivo_xspf):
    lista_localizaciones = obtener_localizaciones(archivo_xspf)
    validar_lista_localizaciones(lista_localizaciones)
    lista_randomizada = randomizar_lista(lista_localizaciones)
    llamar_vlc(lista_randomizada)

iniciar_interfaz()