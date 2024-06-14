import pytest
from src.buscar_xspf import buscar_archivos_xspf

def test_cantidad_archivos_por_defecto():
    lista = buscar_archivos_xspf()

    assert len(lista) == 4