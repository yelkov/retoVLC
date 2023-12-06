from src.validar_xspf import validar_xspf
import xml.etree.ElementTree as ET
import pytest

def test_archivo_erroneo():
    with pytest.raises(ValueError):
        validar_xspf('archivo_erroneo.xspf')

def test_archivo_vacio():
    with pytest.raises(ET.ParseError):
        validar_xspf('archivo_vacio.xspf')

     