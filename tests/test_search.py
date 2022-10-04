import pytest
import mariadb
from lihat_info_parkiran import search_parkiran

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

def test_search_1(conn):

    cur = conn.cursor(buffered=True)
    query = f"INSERT INTO `InformasiParkiran` (namaParkiran, alamat, kapasitas, slotTerisi, tarifMotor, tarifMobil, tarifTruk)" \
            f"VALUES ('ayamgorengpemudakalasan', 'halo', 20, 20, 1000, 2000, 3000);"
    cur.execute(query)
    conn.commit()
    
    list_parkiran = search_parkiran('gorengpemudakal')


    query = f"DELETE FROM `InformasiParkiran`" \
            f"WHERE idParkiran = LAST_INSERT_ID();"
    cur.execute(query)
    conn.commit()

    assert len(list_parkiran) == 1

    assert list_parkiran[0].nama_parkiran == 'ayamgorengpemudakalasan'

def test_search_2():
    
    list_parkiran = search_parkiran('gorengpeng')

    assert len(list_parkiran) == 0

def test_search_3(conn):

    cur = conn.cursor(buffered=True)
    query = f"INSERT INTO `InformasiParkiran` (namaParkiran, alamat, kapasitas, slotTerisi, tarifMotor, tarifMobil, tarifTruk)" \
            f"VALUES ('ayamgorengpemudakalasan', 'halo', 20, 20, 1000, 2000, 3000),('ayamgorengpemudakalasan1', 'halo', 20, 20, 1000, 2000, 3000);"
    cur.execute(query)
    conn.commit()
    
    list_parkiran = search_parkiran('gorengpemudakal')


    query = f"DELETE FROM `InformasiParkiran`" \
            f"WHERE namaParkiran = 'ayamgorengpemudakalasan' or namaParkiran = 'ayamgorengpemudakalasan1';"
    cur.execute(query)
    conn.commit()

    assert len(list_parkiran) == 2

    assert list_parkiran[0].nama_parkiran == 'ayamgorengpemudakalasan'

    assert list_parkiran[1].nama_parkiran == 'ayamgorengpemudakalasan1'