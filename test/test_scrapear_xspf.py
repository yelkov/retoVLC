from src.scrapear_xspf import scrapear_xspf
import pytest

def test_devuelve_lista():
    assert isinstance(scrapear_xspf('lista_prueba.xspf'), list)
    assert isinstance(scrapear_xspf('creedence.xspf'), list)

def test_lista_no_vacia():
    assert scrapear_xspf('lista_prueba.xspf') != []
    assert scrapear_xspf('creedence.xspf') != []

def test_numero_elementos():
    assert len(scrapear_xspf('lista_prueba.xspf')) == 5
    assert len(scrapear_xspf('creedence.xspf')) == 25

def test_lista_localizaciones():
    assert scrapear_xspf('lista_prueba.xspf') == ['lista_canciones/canciones/21%20Ramble%20Tamble.mp3','lista_canciones/canciones/24%20Cotton%20Fields.mp3','lista_canciones/canciones/22%20Born%20On%20The%20Bayou.mp3','lista_canciones/canciones/25%20Commotion.mp3','lista_canciones/canciones/23%20It%20Came%20Out%20Of%20The%20Sky.mp3']
    
    assert scrapear_xspf('creedence.xspf') == ['lista_canciones/canciones/01%20Susie%20Q.mp3','lista_canciones/canciones/02%20I%20Put%20A%20Spell%20On%20You.mp3','lista_canciones/canciones/03%20Proud%20Mary.mp3','lista_canciones/canciones/04%20Bad%20Moon%20Rising%20-%20Remastered%201985.mp3','lista_canciones/canciones/05%20Lodi%20-%20Remastered%201985.mp3','lista_canciones/canciones/06%20Green%20River%20-%20Remastered%201985.mp3','lista_canciones/canciones/07%20Commotion%20-%20Remastered%201985.mp3','lista_canciones/canciones/08%20Down%20On%20The%20Corner.mp3','lista_canciones/canciones/09%20Fortunate%20Son.mp3','lista_canciones/canciones/10%20Travelin%27%20Band.mp3','lista_canciones/canciones/11%20Who%27ll%20Stop%20The%20Rain.mp3','lista_canciones/canciones/13%20Run%20Through%20The%20Jungle.mp3','lista_canciones/canciones/12%20Up%20Around%20The%20Bend.mp3','lista_canciones/canciones/14%20Lookin%27%20Out%20My%20Back%20Door.mp3','lista_canciones/canciones/16%20I%20Heard%20It%20Through%20The%20Grapevine.mp3','lista_canciones/canciones/15%20Long%20As%20I%20Can%20See%20The%20Light.mp3','lista_canciones/canciones/17%20Have%20You%20Ever%20Seen%20The%20Rain.mp3','lista_canciones/canciones/18%20Hey%20Tonight.mp3','lista_canciones/canciones/19%20Sweet%20Hitch-Hiker.mp3','lista_canciones/canciones/20%20Someday%20Never%20Comes.mp3','lista_canciones/canciones/21%20Ramble%20Tamble.mp3','lista_canciones/canciones/22%20Born%20On%20The%20Bayou.mp3','lista_canciones/canciones/23%20It%20Came%20Out%20Of%20The%20Sky.mp3','lista_canciones/canciones/25%20Commotion.mp3','lista_canciones/canciones/24%20Cotton%20Fields.mp3']