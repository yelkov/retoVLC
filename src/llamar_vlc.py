import subprocess
import platform

def llamar_vlc(lista_reproduccion):

    # Precondicion: Verificamos que la entrada de datos es una lista
    assert isinstance(lista_reproduccion,list), f'El archivo introducido como parámetro no es una lista.'

    # Utilizamos la librería platform para identificar el sistema operativo del equipo con el que está trabajando el usuario, y en función de esto el programa buscará una ruta en la que esté instalado VLC.
    
    sistema_operativo = platform.system()

    if sistema_operativo == "Windows":
        try:
            ruta_vlc = r"C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
            comando = [ruta_vlc] + lista_reproduccion
            subprocess.run(comando)

        except FileNotFoundError:
            try:
                ruta_vlc = r"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
                comando = [ruta_vlc] + lista_reproduccion
                subprocess.run(comando)

            except FileNotFoundError:
                "VLC no se encuentra en la ruta esperada."

    elif sistema_operativo == 'Linux':
        try:
            ruta_vlc = r"/usr/bin/vlc"
            comando = [ruta_vlc] + lista_reproduccion
            subprocess.run(comando)

        except FileNotFoundError:
            try:
                ruta_vlc = r"/snap/bin/vlc"
                comando = [ruta_vlc] + lista_reproduccion
                subprocess.run(comando)

            except FileNotFoundError:
                "VLC no se encuentra en la ruta esperada."

    elif sistema_operativo == "Darwin":
        try:
            ruta_vlc = r"/Applications/VLC.app/Contents/MacOS/VLC"
            comando = [ruta_vlc] + lista_reproduccion
            subprocess.run(comando)

        except FileNotFoundError:
            "VLC no se encuentra en la ruta esperada."

    else:
        try:
            ruta_vlc = r"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
            comando = [ruta_vlc] + lista_reproduccion
            subprocess.run(comando)

        except FileNotFoundError:
            "No es posible identificar el sistema operativo."