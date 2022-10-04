import pytest
import mariadb
from ckm_window import *

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

def test_validasi_pelat_nomor():
    assert validasi_pelat_nomor("#@BC") == False
    assert validasi_pelat_nomor("BK1234XY") == True

def test_is_filled_form():
    assert is_filled_form("", "Truk") == False
    assert is_filled_form("BK1234KY", "") == False
    assert is_filled_form("BK1220MK", "Motor") == True