""" File untuk kelas Entity """

import mariadb


class Admin:
    def __init__(self, id):
        """
        Membuat sebuah objek Admin dari id berdasarkan database
        pada tabel Admin yang dimiliki
        """
        try:
            conn = mariadb.connect(
                user="root",
                password="",
                host="localhost",
                port=3306,
                database="parkco"
            )
            cur = conn.cursor(buffered=True)
            query = f"SELECT * FROM `admin`" \
                    f"WHERE id = '{id}';"
            cur.execute(query)

            if cur.rowcount == 0:
                return

            for (id, email, username, password, id_parkiran) in cur:
                self.id = id
                self.email = email
                self.username = username
                self.password = password
                self.parkiran = InformasiParkiran(id_parkiran)
                break

            conn.close()

        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")


class Customer:
    """
    Membuat sebuah objek Customer dari id berdasarkan database
    pada tabel customer yang dimiliki
    """
    def __init__(self, id):
        try:
            conn = mariadb.connect(
                user="root",
                password="",
                host="localhost",
                port=3306,
                database="parkco"
            )
            cur = conn.cursor(buffered=True)
            query = f"SELECT * FROM `customer`" \
                    f"WHERE id = '{id}';"
            cur.execute(query)

            if cur.rowcount == 0:
                return

            for (id, email, username, password) in cur:
                self.id = id
                self.email = email
                self.username = username
                self.password = password
                break

            conn.close()

        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")


class InformasiParkiran:
    """
    Membuat sebuah objek InformasiParkiran dari data yang diberikan.
    """
    def __init__(self, id_parkiran):
        try:
            conn = mariadb.connect(
                user="root",
                password="",
                host="localhost",
                port=3306,
                database="parkco"
            )
            cur = conn.cursor(buffered=True)
            query = f"SELECT * FROM `informasiparkiran`" \
                    f"WHERE idParkiran = '{id_parkiran}';"
            cur.execute(query)

            self.id_parkiran = id_parkiran
            self.nama_parkiran = None

            if cur.rowcount == 0:
                return

            for (_, nama_parkiran, alamat, kapasitas, slot_terisi,
                 tarif_motor, tarif_mobil, tarif_truk) in cur:
                self.nama_parkiran = nama_parkiran
                self.alamat = alamat
                self.kapasitas = kapasitas
                self.slot_terisi = slot_terisi
                self.tarif_motor = tarif_motor
                self.tarif_mobil = tarif_mobil
                self.tarif_truk = tarif_truk
                break

            conn.close()

        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")

    def update(self):
        try:
            conn = mariadb.connect(
                user="root",
                password="",
                host="localhost",
                port=3306,
                database="parkco"
            )
            cur = conn.cursor(buffered=True)
            query = f"SELECT * FROM `informasiparkiran`" \
                    f"WHERE idParkiran = '{self.id_parkiran}';"
            cur.execute(query)

            if cur.rowcount == 0:
                return

            for (_, nama_parkiran, alamat, kapasitas, slot_terisi,
                 tarif_motor, tarif_mobil, tarif_truk) in cur:
                self.nama_parkiran = nama_parkiran
                self.alamat = alamat
                self.kapasitas = kapasitas
                self.slot_terisi = slot_terisi
                self.tarif_motor = tarif_motor
                self.tarif_mobil = tarif_mobil
                self.tarif_truk = tarif_truk
                break

            conn.close()

        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")

    def add_one_slot(self):
        try:
            conn = mariadb.connect(
                user="root",
                password="",
                host="localhost",
                port=3306,
                database="parkco"
            )
            cur = conn.cursor(buffered=True)
            query = f"UPDATE `informasiparkiran` "\
                    f"SET slotTerisi = {self.slot_terisi + 1} "\
                    f"WHERE idParkiran = {self.id_parkiran};"

            cur.execute(query)
            conn.commit()
            conn.close()

            self.slot_terisi += 1

        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")

    def delete_one_slot(self):
        try:
            conn = mariadb.connect(
                user="root",
                password="",
                host="localhost",
                port=3306,
                database="parkco"
            )
            cur = conn.cursor(buffered=True)
            query = f"UPDATE `informasiparkiran` "\
                    f"SET slotTerisi = {self.slot_terisi - 1} "\
                    f"WHERE idParkiran = {self.id_parkiran};"

            cur.execute(query)
            conn.commit()
            conn.close()

            self.slot_terisi -= 1

        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
