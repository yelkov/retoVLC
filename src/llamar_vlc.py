import subprocess
import os

def llamar_vlc(ruta_vlc,lista_reproduccion):

    # Precondicion: Verificamos que las rutas no están vacías
    assert ruta_vlc != "", 'La ruta a VLC está vacía.'
    assert lista_reproduccion != [], 'La ruta a la lista de reproducción está vacía.'

    comando = [ruta_vlc] + [lista_reproduccion]
    subprocess.run(comando)
