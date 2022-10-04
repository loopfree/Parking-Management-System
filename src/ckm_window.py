""" Halaman Catat Kendaraan Masuk """

import re
import mariadb
from PyQt5 import QtCore, QtGui, QtWidgets
from exception import CatatKendaraanMasukError


class CKMWindow():
    def __init__(self, main_window, user):
        """ Inisiasi halaman catat kendaraan masuk """
        self.user = user
        main_window.setObjectName("CKMWindow")
        main_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 50, 471, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.push_button = QtWidgets.QPushButton(self.centralwidget)
        self.push_button.setGeometry(QtCore.QRect(70, 70, 93, 28))
        self.push_button.setObjectName("push_button")
        self.push_button.clicked.connect(lambda : main_window.to_admin_window(self.user))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 110, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.text_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.text_edit.setGeometry(QtCore.QRect(260, 210, 261, 41))
        self.text_edit.setObjectName("text_edit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 180, 531, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.text_edit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.text_edit_2.setGeometry(QtCore.QRect(260, 300, 261, 41))
        self.text_edit_2.setObjectName("text_edit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 270, 531, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 360, 791, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.push_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_2.setGeometry(QtCore.QRect(350, 480, 93, 28))
        self.push_button_2.setObjectName("push_button_2")
        self.push_button_2.clicked.connect(lambda : self.input_data_clicked(main_window))
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("color: red;")
        self.label_6.setGeometry(QtCore.QRect(0, 440, 800, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.date_edit = QtWidgets.QDateEdit(self.centralwidget)
        self.date_edit.setGeometry(QtCore.QRect(270, 400, 110, 31))
        self.date_edit.setDate(QtCore.QDate(2022, 4, 1))
        self.date_edit.setObjectName("date_edit")
        self.time_edit = QtWidgets.QTimeEdit(self.centralwidget)
        self.time_edit.setGeometry(QtCore.QRect(410, 400, 118, 31))
        self.time_edit.setObjectName("time_edit")
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self):
        """ Melakukan perubahan nama pada atribut yang terdapat pada UI """
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("CKMWindow", "Park Co"))
        self.push_button.setText(_translate("CKMWindow", "Back"))
        self.label_2.setText(_translate("CKMWindow", "Catat Kendaraan Masuk"))
        self.label_3.setText(_translate("CKMWindow", "Pelat Nomor"))
        self.label_4.setText(_translate("CKMWindow", "Jenis Kendaraan"))
        self.label_5.setText(_translate("CKMWindow", "Waktu Masuk"))
        self.push_button_2.setText(_translate("CKMWindow", "Submit"))

    def input_data_clicked(self, main_window):
        input_pelat = self.text_edit.toPlainText()
        input_jenis = self.text_edit_2.toPlainText()
        parkiran = self.user.parkiran
        input_waktu_masuk = self.date_edit.date().toPyDate()
        input_waktu_masuk = input_waktu_masuk.strftime("%Y-%m-%d")
        input_waktu_masuk = input_waktu_masuk + " " + self.time_edit.time().toString()

        try :
            input_data(input_pelat, input_jenis, input_waktu_masuk, parkiran)
            self.date_edit.setDate(QtCore.QDate(2022, 4, 1))
            main_window.to_admin_window(self.user)
        except CatatKendaraanMasukError as e:
            self.label_6.setText(e.message)


def input_data(pelat, jenis, waktu_masuk, parkiran):
    """ Menginput data kendaraan yang masuk """
    # setup connection to database
    try:
        conn = mariadb.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="parkco"
        )
        cur = conn.cursor(buffered=True)
        # insert data into kendaraan table (idKendaraan, pelat, jenis)
        # cek apakah kendaraan sudah terparkir
        cur.execute("SELECT sedangParkir FROM kendaraan WHERE platNomor = %s", (pelat,))
        row = cur.fetchone()

        if not is_filled_form(pelat, jenis):
            raise CatatKendaraanMasukError("Form Tidak Boleh Kosong")
        if parkiran.slot_terisi == parkiran.kapasitas :
            raise CatatKendaraanMasukError("Parkiran Penuh")
        if cur.rowcount != 0:
            if row[0] == 1:
                raise CatatKendaraanMasukError("Kendaraan sudah terparkir")
        if not(jenis == "Motor" or jenis == "Mobil" or jenis == "Truk"):
            raise CatatKendaraanMasukError("Jenis kendaraan tidak valid (Motor, Mobil, Truk)")
        if not validasi_pelat_nomor(pelat):
            raise CatatKendaraanMasukError("Pelat Nomor Invalid Format")

        # cek jika kendaraan sudah terdaftar
        cur.execute("SELECT idKendaraan, jenis FROM kendaraan WHERE platNomor = %s", (pelat,))
        if cur.rowcount == 0: # Kalau kendaraannya tidak ada
            cur.execute("INSERT INTO kendaraan (platNomor, jenis) VALUES (%s, %s)",
                    (pelat, jenis))
        elif cur.fetchone()[1] != jenis:
            raise CatatKendaraanMasukError("Jenis kendaraan berbeda dari data")

        # insert data into parkir table (idKendaraan, waktuMasuk)
        cur.execute("INSERT INTO kendaraanterparkir (idParkiran, idKendaraan, waktuMasuk, sudahKeluar) VALUES \
                    (%s,(SELECT idKendaraan FROM kendaraan WHERE platNomor = %s), %s, 0)",
                    (parkiran.id_parkiran, pelat, waktu_masuk))
        # tandai kendaraan sedang parkir
        cur.execute("UPDATE kendaraan SET sedangParkir = 1 WHERE platNomor = %s", (pelat,))

        cur.close()
        conn.commit()
        conn.close()

        parkiran.add_one_slot()

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")


def validasi_pelat_nomor(plat_nomor):
    """ Mengecek apakah pelat nomor valid """
    if re.search(r'^[A-Z]{1,2}\s*\d{1,4}\s*[A-Z]{0,3}$', plat_nomor):
        return True
    return False


def is_filled_form(pelat, jenis):
    """ Mengecek apakah form telah diisi semua"""
    return (pelat != "" and jenis != "")
