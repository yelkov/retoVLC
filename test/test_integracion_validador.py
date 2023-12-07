from src.parsear_xspf import obtener_localizaciones
from src.validar_lista_localizaciones import validar_lista_localizaciones
import pytest

def test_integracion_validador_ok():
    assert len(validar_lista_localizaciones(obtener_localizaciones('creedence.xspf'))) == 25
    assert len(validar_lista_localizaciones(obtener_localizaciones('lista_prueba.xspf'))) == 5

    assert validar_lista_localizaciones(obtener_localizaciones('lista_prueba.xspf')) == ["lista_canciones/canciones/21 Ramble Tamble.mp3","lista_canciones/canciones/24 Cotton Fields.mp3","lista_canciones/canciones/22 Born On The Bayou.mp3","lista_canciones/canciones/25 Commotion.mp3","lista_canciones/canciones/23 It Came Out Of The Sky.mp3"]
    assert validar_lista_localizaciones(obtener_localizaciones('creedence.xspf')) == ["lista_canciones/canciones/01 Susie Q.mp3","lista_canciones/canciones/02 I Put A Spell On You.mp3","lista_canciones/canciones/03 Proud Mary.mp3","lista_canciones/canciones/04 Bad Moon Rising - Remastered 1985.mp3","lista_canciones/canciones/05 Lodi - Remastered 1985.mp3","lista_canciones/canciones/06 Green River - Remastered 1985.mp3","lista_canciones/canciones/07 Commotion - Remastered 1985.mp3","lista_canciones/canciones/08 Down On The Corner.mp3","lista_canciones/canciones/09 Fortunate Son.mp3","lista_canciones/canciones/10 Travelin' Band.mp3","lista_canciones/canciones/11 Who'll Stop The Rain.mp3","lista_canciones/canciones/12 Up Around The Bend.mp3","lista_canciones/canciones/13 Run Through The Jungle.mp3","lista_canciones/canciones/15 Long As I Can See The Light.mp3","lista_canciones/canciones/14 Lookin' Out My Back Door.mp3","lista_canciones/canciones/16 I Heard It Through The Grapevine.mp3","lista_canciones/canciones/17 Have You Ever Seen The Rain.mp3","lista_canciones/canciones/18 Hey Tonight.mp3","lista_canciones/canciones/19 Sweet Hitch-Hiker.mp3","lista_canciones/canciones/20 Someday Never Comes.mp3","lista_canciones/canciones/21 Ramble Tamble.mp3","lista_canciones/canciones/22 Born On The Bayou.mp3","lista_canciones/canciones/23 It Came Out Of The Sky.mp3","lista_canciones/canciones/24 Cotton Fields.mp3","lista_canciones/canciones/25 Commotion.mp3"]

def test_integracion_validador_mal():
    with pytest.raises(SystemExit) as exit:
        validar_lista_localizaciones(obtener_localizaciones("archivo_vacio.xspf"))
    assert exit.type == SystemExit
    assert exit.value.code == 1 
