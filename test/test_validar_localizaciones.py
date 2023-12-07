from src.validar_lista_localizaciones import validar_lista_localizaciones
import pytest


def test_archivo_erroneo():
    with pytest.raises(SystemExit) as exit:
        validar_lista_localizaciones(["","",""])
    assert exit.type == SystemExit
    assert exit.value.code == 1 

    with pytest.raises(SystemExit) as exit:
        validar_lista_localizaciones([" "," ","  "])
    assert exit.type == SystemExit
    assert exit.value.code == 1 


def test_archivo_valido():
    assert validar_lista_localizaciones(['cancion1.mp3','cancion2.mp3','cancion3.mp3']) == ['cancion1.mp3','cancion2.mp3','cancion3.mp3']