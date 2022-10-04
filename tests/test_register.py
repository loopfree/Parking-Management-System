import pytest
import mariadb
from register_window import *


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


def test_valid_form():
    assert valid_form('email', 'username', '') == False
    assert valid_form('email', 'username', 'password') == True


def test_valid_email():
    emails = [('rpl2022@if2230.com', True),
              ('Ja.Ck@mahasiswa.itb.ac.id', True),
              ('Marks&Spencer@shop.id', False),
              ('this.at.yahoo.com', False),
              ('myhome@here', False)]
    for email, mark in emails:
        assert True if valid_email(email) else False == mark


def test_valid_username():
    for username, mark in [('abc_123', True), ('team', False),
                           ('50 people', False), ('ab b', False)]:
        assert (valid_username_space(username) and
                valid_username_length(username)) == mark


def test_valid_password():
    assert valid_password('i love you 3000') == True
    assert valid_password('2short') == False


def test_register_1(conn):
    cur = conn.cursor(buffered=True)
    query = f"INSERT INTO `admin` (email, username, password)" \
            f"VALUES ('test1@email.com', 'test1', 'test1');"
    cur.execute(query)
    conn.commit()
    try:
        register('test0@email.com', 'test1', 'test0pass', 'customer')
        assert False
    except:
        assert True

    query = f"DELETE FROM `admin`" \
            f"WHERE username = 'test1';"
    cur.execute(query)
    conn.commit()


def test_register_2(conn):
    try:
        register('test2@email.com', 'test2', 'test2pass', 'customer')
        assert True
    except:
        assert False

    cur = conn.cursor(buffered=True)
    query = f"DELETE FROM `customer`" \
            f"WHERE username = 'test2';"
    cur.execute(query)
    conn.commit()


def test_register_3(conn):
    cur = conn.cursor(buffered=True)
    try:
        register('test3@email.com', 'test3', 'test3pass', 'admin')
        query = f"SELECT email FROM `account`" \
                f"WHERE username = 'test3';"
        cur.execute(query)
        if cur.rowcount != 1:
            query = f"DELETE FROM `admin`" \
                    f"WHERE username = 'test3';"
            cur.execute(query)
            conn.commit()
            assert False
        else:
            for (email,) in cur:
                break
            assert email == 'test3@email.com'
    except:
        assert False

    query = f"DELETE FROM `admin`" \
            f"WHERE username = 'test3';"
    cur.execute(query)
    conn.commit()
