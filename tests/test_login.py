import pytest
import mariadb
from login_window import *


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


def test_validForm():
    assert valid_form('username', '') == False
    assert valid_form('username', 'password') == True


def test_validUsername():
    assert valid_username('abc_123') == True
    assert valid_username('50people ') == False


def test_login_1(conn):
    cur = conn.cursor(buffered=True)
    query = f"INSERT INTO `admin` (email, username, password)" \
            f"VALUES ('test1@email.com', 'test1', 'test1');"
    cur.execute(query)
    conn.commit()
    try:
        id, role = login('test1', 'test1')
        assert True
    except:
        assert False

    query = f"DELETE FROM `admin`" \
            f"WHERE id = LAST_INSERT_ID();"
    cur.execute(query)
    conn.commit()


def test_login_2():
    try:
        login('test2', 'test2')
        assert False
    except:
        assert True


def test_login_3(conn):
    cur = conn.cursor(buffered=True)
    query = f"INSERT INTO `customer` (email, username, password)" \
            f"VALUES ('test3@email.com', 'test3', 'test3');"
    cur.execute(query)
    conn.commit()
    try:
        login('test3', 'test0')
        assert False
    except:
        assert True

    query = f"DELETE FROM `customer`" \
            f"WHERE id = LAST_INSERT_ID();"
    cur.execute(query)
    conn.commit()
