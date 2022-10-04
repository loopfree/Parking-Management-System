""" Halaman Lihat Informasi Parkiran """

import mariadb
from PyQt5 import QtCore, QtGui, QtWidgets
from entity import InformasiParkiran


class ParkingSearchWindow():
    """
    Inisiasi kelas ParkiranSearchWindow
    """
    def __init__(self, main_window, user):
        self.user = user
        main_window.setObjectName("parking_search_window")
        main_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        main_window.setCentralWidget(self.centralwidget)

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.scroll = QtWidgets.QScrollArea(self.frame)
        self.widget = QtWidgets.QWidget(self.frame)
        self.vbox = QtWidgets.QVBoxLayout(self.frame)
        font = QtGui.QFont()

        font.setPointSize(12)
        self.label_1.setGeometry(QtCore.QRect(40, 10, 171, 51))
        self.label_1.setFont(font)
        self.label_1.setObjectName("label")

        self.label_2.setGeometry(QtCore.QRect(650, 30, 131, 31))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.text_edit.setGeometry(QtCore.QRect(30, 60, 301, 28))
        self.text_edit.setObjectName("text_edit")

        self.frame.setGeometry(QtCore.QRect(30, 140, 731, 411))
        self.frame.setStyleSheet("border: 2px solid black;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.scroll.setGeometry(QtCore.QRect(0, 0, 731, 411))
        self.vbox.setGeometry(QtCore.QRect(0, 0, 731, 411))
        self.scroll.setWidgetResizable(True)
        self.scroll.setObjectName("scroll")

        font.setPointSize(16)
        self.push_button_search = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_search.setGeometry(QtCore.QRect(350, 60, 93, 28))
        self.push_button_search.setObjectName("push_button_search")
        self.push_button_search.clicked.connect(self.show_parkiran)

        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.show_parkiran()
        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self):
        """" Retranslate UI """
        _translate = QtCore.QCoreApplication.translate
        self.label_1.setText(_translate("parking_search_window", "Cari Tempat Parkir"))
        self.label_2.setText(_translate("parking_search_window", self.user.username))
        self.push_button_search.setText(_translate("parking_search_window", "Cari"))

    def show_parkiran(self):
        """" Menampilkan parkiran yang tersedia """
        # delete all child
        for i in reversed(range(self.vbox.count())):
            self.vbox.itemAt(i).widget().deleteLater()

        list_parkiran = search_parkiran(self.text_edit.toPlainText())

        # show List of Parkiran
        font = QtGui.QFont()
        font.setPointSize(14)
        for parkiran in list_parkiran:
            label = QtWidgets.QLabel()
            text = f"Nama Parkiran: {parkiran.nama_parkiran}\n"\
                   f"Alamat: {parkiran.alamat}\n"\
                   f"Slot terisi: {parkiran.slot_terisi}/{parkiran.kapasitas}\n"\
                   f"Tarif Motor: Rp{parkiran.tarif_motor}\n"\
                   f"Tarif Mobil: Rp{parkiran.tarif_mobil}\n"\
                   f"Tarif Truk: Rp{parkiran.tarif_truk}\n"

            label.setText(text)
            label.setFont(font)
            self.vbox.addWidget(label)


def search_parkiran(search_query):
    """ Fungsi untuk melakukan pencarian pada parkiran sesuai inputan pengguna """
    try:
        conn = mariadb.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="parkco"
        )
        cur = conn.cursor(buffered=True)

        # Run SQL Query
        query = f"SELECT * FROM `informasiparkiran` " \
                f"WHERE LOWER(namaParkiran) LIKE LOWER('%{search_query}%');"

        cur.execute(query)

        # Fetch all data
        list_parkiran = []
        for row in cur:
            if (row[1] != None):    # InformasiParkiran is incomplete
                list_parkiran.append(InformasiParkiran(row[0]))

        conn.close()

        return list_parkiran

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
