import tkinter as tk
from .buscar_xspf import buscar_archivos_xspf
from .parsear_xspf import obtener_localizaciones
from .validar_lista_localizaciones import validar_lista_localizaciones
from .randomizar_lista import randomizar_lista
from .llamar_vlc import llamar_vlc

def iniciar_interfaz():

    # ======== RAIZ =========

    raiz = tk.Tk()
    raiz.title("VLC mixer")
    raiz.config(bg="#616161")
    raiz.iconbitmap(r"imagenes\\logo.ico")
    raiz.grid_columnconfigure(0,weight=1)

    # ======== FRAME PRINCIPAL =========

    frame_principal = tk.Frame(raiz,width=540,height=316, bg="#161a4a",padx=20,pady=20)
    frame_principal.grid(row=0,column=0,padx=2,pady=2,sticky="nsew")
    frame_principal.grid_propagate(False)

    frame_principal.grid_columnconfigure(0, weight=1)


        # ------- texto superior --------

    texto_principal = tk.Label(frame_principal,text="¡Bienvenido a VLC mixer de canciones!",justify="center",bg="#161a4a",fg="#fcae64",font=("Arial",16,"bold"),highlightthickness=1,highlightbackground="#fcae64",padx=15,pady=5)
    texto_principal.grid(row=1,column=0,sticky="ns")

    

        # ------- texto instrucciones --------

    texto_instrucciones = tk.Label(frame_principal, text="Seleccione una lista de canciones y a continuación haga click en randomizar.",bg="#161a4a",fg="#fcae64",pady=15)
    texto_instrucciones.grid(row=3,column=0,sticky="n")

        # ------- menú de seleccion --------

    archivo_seleccionado = tk.StringVar()
    archivo_seleccionado.set("Seleccione una lista")
    lista_archivos = buscar_archivos_xspf()
    selector = tk.OptionMenu(frame_principal,archivo_seleccionado,*lista_archivos)
    selector.config(bg="#161a4a",fg="#fcae64",highlightbackground="#fcae64",activebackground="#fcae64",activeforeground="#161a4a")
    selector["menu"].config(bg="#161a4a",fg="#fcae64",activebackground="#fcae64",activeforeground="#161a4a")
    selector.grid(row=4,column=0,sticky="s",pady=(0,20))

        # ------- botón de randomizar --------
    boton_randomizar = tk.Button(frame_principal,text="¡Randomizar!",command=lambda:randomizar(archivo_seleccionado.get()),padx=10,pady=10,font=("Arial",18,"bold"),bg="#fcae64",fg="#313131",activebackground="#313131",activeforeground="#fcae64")
    boton_randomizar.grid(row=5,column=0,sticky="s",pady=(40,0))
    raiz.mainloop()





def randomizar(archivo_xspf):
    lista_localizaciones = obtener_localizaciones(archivo_xspf)
    validar_lista_localizaciones(lista_localizaciones)
    lista_randomizada = randomizar_lista(lista_localizaciones)
    llamar_vlc(lista_randomizada)

