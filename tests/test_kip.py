import pytest
import mariadb
from kip_window import *

@pytest.fixture
def conn():
    try:
        conn = mariadb.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="parkco"
        )
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")

def test_full_form():
    assert full_form("nama_parkiran", "alamat", "kapasitas", "tarif_mobil", "tarif_motor", "") == False
    assert full_form("nama_parkiran", "alamat", "kapasitas", "tarif_mobil", "tarif_motor", "tarif_truk") == True

def test_integer_kapasitas():
    assert integer_kapasitas("") == False
    assert integer_kapasitas(30) == True

def test_integer_tarif():
    assert integer_tarif(1, "a", 55) == False
    assert integer_tarif(1, 2, 3) == True