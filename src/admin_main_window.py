""" Halaman Utama Admin """

from PyQt5 import QtCore, QtGui, QtWidgets

class AdminMainWindow():
    def __init__(self, main_window, user):
        """ Inisiasi Kelas AdminMainWindow """
        self.user = user

        main_window.setObjectName("AdminMainWindow")
        main_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 20, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 120, 351, 31))

        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 160, 351, 31))

        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 210, 451, 31))

        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(470, 120, 51, 31))

        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(470, 160, 100, 31))

        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.push_button = QtWidgets.QPushButton(self.centralwidget)
        self.push_button.setGeometry(QtCore.QRect(320, 370, 161, 71))
        self.push_button.setObjectName("push_button")
        self.push_button.clicked.connect(lambda : main_window.to_ckm_window(self.user))
        self.push_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_2.setGeometry(QtCore.QRect(320, 460, 161, 71))
        self.push_button_2.setObjectName("push_button_2")
        self.push_button_2.clicked.connect(lambda : main_window.to_hb_window(self.user))
        self.push_button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_3.setGeometry(QtCore.QRect(320, 270, 161, 71))
        self.push_button_3.setObjectName("push_button_3")
        self.push_button_3.clicked.connect(lambda : main_window.to_kip_window(self.user))
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
        self.label.setText(_translate("AdminMainWindow", "Park.Co"))
        if self.user.parkiran.nama_parkiran == None:
            self.label_2.setText(_translate("AdminMainWindow", "Parkiran anda belum diset."))
            self.label_3.setText(_translate("AdminMainWindow", "Silakan set dulu di kelola parkiran."))
        else:
            self.label_2.setText(_translate("AdminMainWindow", self.user.parkiran.nama_parkiran))
            self.label_3.setText(_translate("AdminMainWindow", self.user.username ))
            self.label_4.setText(_translate("AdminMainWindow", self.user.parkiran.alamat))
            self.label_5.setText(_translate("AdminMainWindow", "SLOT"))
            self.label_6.setText(_translate("AdminMainWindow", f"{self.user.parkiran.slot_terisi}/{self.user.parkiran.kapasitas}"))
        self.push_button.setText(_translate("AdminMainWindow", "Catat Kendaraan Masuk"))
        self.push_button_2.setText(_translate("AdminMainWindow", "Catat Kendaraan Keluar"))
        self.push_button_3.setText(_translate("AdminMainWindow", "Kelola Tempat Parkir"))
