""" Halaman Kelola Informasi Parkiran """

from PyQt5 import QtCore, QtGui, QtWidgets
import mariadb
from exception import KelolaInformasiParkiranError


class KIPWindow():
    def __init__(self, main_window, user):
        """ Setup GUI Qtpy5 """
        self.user = user

        main_window.setObjectName("KIPWindow")
        main_window.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 781, 71))
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(600, 30, 191, 41))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|
                                  QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 781, 81))
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.push_button = QtWidgets.QPushButton(self.centralwidget)
        self.push_button.setGeometry(QtCore.QRect(30, 30, 93, 28))
        self.push_button.setObjectName("push_button")
        self.push_button.clicked.connect(lambda: main_window.to_admin_window(self.user))

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 180, 181, 31))
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 230, 181, 16))
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 270, 181, 21))
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 320, 201, 16))
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(250, 350, 131, 16))
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(250, 390, 131, 16))
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(250, 430, 131, 16))
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        self.text_edit_nama_parkiran = QtWidgets.QTextEdit(self.centralwidget)
        self.text_edit_nama_parkiran.setGeometry(QtCore.QRect(390, 180, 211, 31))
        font.setPointSize(10)
        self.text_edit_nama_parkiran.setFont(font)
        self.text_edit_nama_parkiran.setObjectName("text_edit_nama_parkiran")
        self.text_edit_nama_parkiran.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.text_edit_nama_parkiran.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.text_edit_alamat = QtWidgets.QTextEdit(self.centralwidget)
        self.text_edit_alamat.setGeometry(QtCore.QRect(390, 220, 211, 31))
        font.setPointSize(10)
        self.text_edit_alamat.setFont(font)
        self.text_edit_alamat.setObjectName("text_edit_alamat")
        self.text_edit_alamat.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.text_edit_alamat.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.text_edit_kapasitas = QtWidgets.QTextEdit(self.centralwidget)
        self.text_edit_kapasitas.setGeometry(QtCore.QRect(390, 270, 211, 31))
        font.setPointSize(10)
        self.text_edit_kapasitas.setFont(font)
        self.text_edit_kapasitas.setObjectName("text_edit_kapasitas")
        self.text_edit_kapasitas.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.text_edit_kapasitas.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.text_edit_tarif_mobil = QtWidgets.QTextEdit(self.centralwidget)
        self.text_edit_tarif_mobil.setGeometry(QtCore.QRect(390, 340, 211, 31))
        font.setPointSize(10)
        self.text_edit_tarif_mobil.setFont(font)
        self.text_edit_tarif_mobil.setObjectName("text_edit_tarif_mobil")
        self.text_edit_tarif_mobil.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.text_edit_tarif_mobil.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.text_edit_tarif_motor = QtWidgets.QTextEdit(self.centralwidget)
        self.text_edit_tarif_motor.setGeometry(QtCore.QRect(390, 380, 211, 31))
        font.setPointSize(10)
        self.text_edit_tarif_motor.setFont(font)
        self.text_edit_tarif_motor.setObjectName("text_edit_tarif_motor")
        self.text_edit_tarif_motor.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.text_edit_tarif_motor.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.text_edit_tarif_truk = QtWidgets.QTextEdit(self.centralwidget)
        self.text_edit_tarif_truk.setGeometry(QtCore.QRect(390, 420, 211, 31))
        font.setPointSize(10)
        self.text_edit_tarif_truk.setFont(font)
        self.text_edit_tarif_truk.setObjectName("text_edit_tarif_truk")
        self.text_edit_tarif_truk.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.text_edit_tarif_truk.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.push_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_2.setGeometry(QtCore.QRect(350, 510, 93, 28))
        self.push_button_2.setObjectName("push_button_2")
        self.push_button_2.clicked.connect(self.update_data_clicked)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 470, 781, 31))
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: red;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 470, 781, 31))
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: blue;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslate_ui()
        self.fill_form()
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self):
        """ Memperbarui teks pada UI """
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("KIPWindow", "Park.Co"))
        self.label_2.setText(_translate("KIPWindow", self.user.username))
        self.label_5.setText(_translate("KIPWindow", "Kelola Informasi Tempat Parkir"))
        self.push_button.setText(_translate("KIPWindow", "Back"))
        self.label_6.setText(_translate("KIPWindow", "Nama Parkiran"))
        self.label_7.setText(_translate("KIPWindow", "Alamat"))
        self.label_8.setText(_translate("KIPWindow", "Kapasitas"))
        self.label_9.setText(_translate("KIPWindow", "Tarif"))
        self.label_10.setText(_translate("KIPWindow", "Mobil"))
        self.label_11.setText(_translate("KIPWindow", "Motor"))
        self.label_12.setText(_translate("KIPWindow", "Truk"))
        self.push_button_2.setText(_translate("KIPWindow", "Update"))

    def fill_form(self):
        """ Mengisi form """
        _translate = QtCore.QCoreApplication.translate
        self.text_edit_nama_parkiran.setText(_translate("KIPWindow",
                                                        self.user.parkiran.nama_parkiran))
        self.text_edit_alamat.setText(_translate("KIPWindow",
                                                 self.user.parkiran.alamat))
        self.text_edit_kapasitas.setText(_translate("KIPWindow",
                                                    str(self.user.parkiran.kapasitas)))
        self.text_edit_tarif_mobil.setText(_translate("KIPWindow",
                                                      str(self.user.parkiran.tarif_mobil)))
        self.text_edit_tarif_motor.setText(_translate("KIPWindow",
                                                      str(self.user.parkiran.tarif_motor)))
        self.text_edit_tarif_truk.setText(_translate("KIPWindow", 
                                                     str(self.user.parkiran.tarif_truk)))

    def update_data_clicked(self):
        """ Mengupdate data sesuai dengan inputan pengguna """
        _translate = QtCore.QCoreApplication.translate
        id_parkiran = self.user.parkiran.id_parkiran
        nama_parkiran = self.text_edit_nama_parkiran.toPlainText()
        alamat = self.text_edit_alamat.toPlainText()
        kapasitas = self.text_edit_kapasitas.toPlainText()
        tarif_mobil = self.text_edit_tarif_mobil.toPlainText()
        tarif_motor = self.text_edit_tarif_motor.toPlainText()
        tarif_truk = self.text_edit_tarif_truk.toPlainText()

        try:
            update_data(id_parkiran, nama_parkiran, alamat, kapasitas, 
                        tarif_mobil, tarif_motor, tarif_truk)

            self.label_3.setText(_translate("KIPWindow", ""))
            self.label_4.setText(_translate("KIPWindow", "Informasi Parkiran Berhasil Diperbaharui"))
            self.user.parkiran.update()

        except KelolaInformasiParkiranError as e:
            self.label_3.setText(_translate("KIPWindow", e.message))
            self.label_4.setText(_translate("KIPWindow", ""))


def update_data(id_parkiran, nama_parkiran, alamat, kapasitas, tarif_mobil, tarif_motor, tarif_truk):
    """ Fungsi untuk melakukan pembaruan data informasi parkian """
    if not full_form(nama_parkiran, alamat, kapasitas, tarif_mobil, tarif_motor, tarif_truk):
        raise KelolaInformasiParkiranError("Isi form dengan lengkap")

    if not integer_kapasitas(kapasitas):
        raise KelolaInformasiParkiranError("Tipe kapasitas salah")

    if not integer_tarif(tarif_mobil, tarif_motor, tarif_truk):
        raise KelolaInformasiParkiranError("Tipe tarif salah")

    try:
        conn = mariadb.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="parkco"
        )
        cur = conn.cursor(buffered=True)

        query = f"UPDATE informasiparkiran SET namaParkiran='{nama_parkiran}',"\
                f"alamat='{alamat}', kapasitas='{kapasitas}', tarifMotor='{tarif_motor}', "\
                f"tarifMobil='{tarif_mobil}',tarifTruk='{tarif_truk}' " \
                f"WHERE idParkiran = '{id_parkiran}';"
        cur.execute(query)

        conn.commit()
        conn.close()

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")


def full_form(nama_parkiran, alamat, kapasitas, tarif_mobil, tarif_motor, tarif_truk):
    """
    Mengecek apakah suatu form telah terisi penuh atau belum
    """
    is_filled = True
    if nama_parkiran == "":
        is_filled = False
    elif alamat == "":
        is_filled = False
    elif kapasitas == "":
        is_filled = False
    elif tarif_mobil == "":
        is_filled = False
    elif tarif_motor == "":
        is_filled = False
    elif tarif_truk == "":
        is_filled = False
    return is_filled


def integer_kapasitas(kapasitas):
    """ Mengecek apakah kapasitas bertipe integer """
    return str(kapasitas).isdigit()


def integer_tarif(tarif_mobil, tarif_motor, tarif_truk):
    """ Mengecek apakah tarif sudah bertipe integer """
    return str(tarif_mobil).isdigit() and str(tarif_motor).isdigit() and str(tarif_truk).isdigit()
