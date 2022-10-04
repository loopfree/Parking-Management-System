from PyQt5 import QtCore, QtGui, QtWidgets
import mariadb
from datetime import datetime
from exception import HitungBiayaError


class HitungBiayaWindow(object):

    def __init__(self, main_window, user):
        self.user = user

        main_window.setObjectName("main_window")
        main_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 781, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.push_button = QtWidgets.QPushButton(self.centralwidget)
        self.push_button.setGeometry(QtCore.QRect(70, 70, 93, 28))
        self.push_button.setObjectName("push_button")
        self.push_button.clicked.connect(lambda : main_window.to_admin_window(self.user))
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setGeometry(QtCore.QRect(0, 150, 801, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.text_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.text_edit.setGeometry(QtCore.QRect(390, 210, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.text_edit.setFont(font)
        self.text_edit.setObjectName("text_edit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 210, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.push_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_2.setGeometry(QtCore.QRect(350, 490, 93, 28))
        self.push_button_2.setObjectName("push_button_2")
        self.push_button_2.clicked.connect(self.hitung_biaya_clicked)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 270, 801, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 380, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 370, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.date_edit = QtWidgets.QDateEdit(self.centralwidget)
        self.date_edit.setGeometry(QtCore.QRect(260, 320, 110, 31))
        self.date_edit.setDate(QtCore.QDate(2022, 4, 1))
        self.date_edit.setObjectName("date_edit")
        self.time_edit = QtWidgets.QTimeEdit(self.centralwidget)
        self.time_edit.setGeometry(QtCore.QRect(420, 320, 118, 31))
        self.time_edit.setObjectName("time_edit")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(4, 420, 791, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
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
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("HitungBiayaWindow", "Park.Co"))
        self.push_button.setText(_translate("HitungBiayaWindow", "Back"))
        self.label_2.setText(_translate("HitungBiayaWindow", "Biaya Parkir"))
        self.label_3.setText(_translate("HitungBiayaWindow", "Pelat Nomor"))
        self.push_button_2.setText(_translate("HitungBiayaWindow", "Hitung"))
        self.label_5.setText(_translate("HitungBiayaWindow", "Waktu Keluar"))
        self.label_6.setText(_translate("HitungBiayaWindow", "Biaya"))
        self.label_4.setText(_translate("HitungBiayaWindow", "Rp 0"))
        self.label_7.setText(_translate("HitungBiayaWindow", ""))

    def hitung_biaya_clicked(self):
        waktu_keluar = self.date_edit.date().toPyDate()
        waktu_keluar = waktu_keluar.strftime("%Y-%m-%d")
        waktu_keluar = waktu_keluar + " " + self.time_edit.time().toString()
        pelat = self.text_edit.toPlainText()
        try:
            biaya = hitung_biaya(pelat, waktu_keluar, self.user.parkiran)
            biaya = int(biaya)
            self.label_4.setText(f"Rp {biaya}")
        except HitungBiayaError as e:
            self.label_7.setText(e.message)


def hitung_biaya(pelat, waktu_keluar, parkiran):
    try:
        conn = mariadb.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="parkco"
        )
        cur = conn.cursor(buffered=True)
        # cari idKendaraan dengan pelat
        query = "SELECT idKendaraan FROM kendaraan WHERE platNomor = '" + pelat + "'"
        cur.execute(query)
        idKendaraan = cur.fetchone()[0]

        if idKendaraan is None:
            raise HitungBiayaError("Kendaraan tersebut tidak terparkir di parkiran admin")

        # cek apakah kendaraan terparkir di parkiran admin
        query = "SELECT idParkiran FROM kendaraanterparkir WHERE idKendaraan = '" + \
                str(idKendaraan) + "' AND sudahKeluar = 0"
        cur.execute(query)
        idParkiran = cur.fetchone()[0]

        if idParkiran != parkiran.id_parkiran:
            raise HitungBiayaError("Kendaraan tersebut tidak terparkir di parkiran admin")

        # cari jenis kendaraan dengan idKendaraan
        query = "SELECT jenis FROM kendaraan WHERE idKendaraan = '" + str(idKendaraan) + "'"
        cur.execute(query)
        jenisKendaraan = cur.fetchone()[0]

        # cari waktu masuk dari kendaraanTerparkir
        query = "SELECT waktuMasuk FROM kendaraanterparkir WHERE idKendaraan = '" + \
                str(idKendaraan) + "' AND sudahKeluar = 0"
        cur.execute(query)

        waktu_masuk = cur.fetchone()[0]
        
        # cari tarif biaya dari informasiparkiran menurut jenis kendaraan
        tarif = 0
        if jenisKendaraan == "Motor":
            cur.execute("SELECT tarifMotor FROM informasiparkiran WHERE idParkiran = '" + \
                         str(idParkiran) + "'")
            tarif = cur.fetchone()[0]
        elif jenisKendaraan == "Mobil":
            cur.execute("SELECT tarifMobil FROM informasiparkiran WHERE idParkiran = '" + \
                        str(idParkiran) + "'")
            tarif = cur.fetchone()[0]
        elif jenisKendaraan == "Truk":
            cur.execute("SELECT tarifTruk FROM informasiparkiran WHERE idParkiran = '" + \
                        str(idParkiran) + "'")
            tarif = cur.fetchone()[0]

        # convert waktu keluar dari string menjadi datetime y-m-d h:m:s
        waktu_keluar = datetime.strptime(waktu_keluar, "%Y-%m-%d %H:%M:%S")
        selisih = waktu_keluar - waktu_masuk
        hours, _ = divmod(selisih.total_seconds(), 3600)
        biaya = hours * tarif

        query = f"UPDATE kendaraanterparkir "\
                f"SET biaya = {biaya}, "\
                    f"sudahKeluar = 1, "\
                    f"waktuKeluar = '{waktu_keluar}' "\
                f"WHERE idKendaraan = {idKendaraan} AND sudahKeluar = 0;"
        cur.execute(query)

        # update sedangParkir = 0
        query = f"UPDATE kendaraan "\
                f"SET sedangParkir = 0 "\
                f"WHERE idKendaraan = {idKendaraan};"
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()

        parkiran.delete_one_slot()
        return biaya

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
