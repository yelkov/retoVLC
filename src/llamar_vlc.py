import subprocess
import platform
import os 

def llamar_vlc(lista_reproduccion):

    # Precondicion: Verificamos que la entrada de datos es una lista
    assert isinstance(lista_reproduccion,list), f'El archivo introducido como parámetro no es una lista.'

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