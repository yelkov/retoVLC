from src.randomizar_lista import randomizar_lista
import random
import pytest

lista_testear = ['uno','dos','tres','cuatro','cinco']
otra_lista_testear = [1,2,3,4,5,6,7,8,9,10]

def test_lista_vacia():
    assert randomizar_lista([]) == []

def test_no_lista():
    with pytest.raises(AssertionError,match='La entrada de datos no es una lista'):
        randomizar_lista('Esto no es una lista')

def test_lista_diferente():
    assert  lista_testear != randomizar_lista(lista_testear)
    assert  otra_lista_testear != randomizar_lista(otra_lista_testear)

def test_mumero_elementos():
    assert  len(lista_testear) == len(randomizar_lista(lista_testear))
    assert  len(otra_lista_testear) == len(randomizar_lista(otra_lista_testear)) 

def test_mismos_elementos():
    assert all(element in randomizar_lista(lista_testear) for element in lista_testear)
    assert all(element in randomizar_lista(otra_lista_testear) for element in otra_lista_testear)