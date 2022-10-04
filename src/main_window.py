""" Halaman Utama Program """

import sys
import time
from PyQt5 import QtWidgets, QtGui, QtCore
from lihat_info_parkiran import ParkingSearchWindow
from login_window import LoginWindow
from register_window import RegisterWindow
from kip_window import KIPWindow
from admin_main_window import AdminMainWindow
from ckm_window import CKMWindow
from hitung_biaya_window import HitungBiayaWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        """ Inisiasi Halaman Utama """
        super().__init__()
        self.ui = LoginWindow(self)

    def to_register_window(self):
        """ Untuk menuju halaman register """
        self.ui = RegisterWindow(self)

    def to_login_window(self):
        """ Untuk menuju halaman login """
        self.ui = LoginWindow(self)

    def to_kip_window(self, user):
        """ Untuk menuju halaman kelola informasi parkiran """
        self.ui = KIPWindow(self, user)

    def to_search_window(self, user):
        """ Untuk menuju halaman pencarian parkiran """
        self.ui = ParkingSearchWindow(self, user)

    def to_admin_window(self, user):
        """ Untuk menuju halaman admin """
        self.ui = AdminMainWindow(self, user)
       
    def to_ckm_window(self, user):
        """ Untuk menuju halaman catat kendaraan masuk """
        self.ui = CKMWindow(self, user)
        
    def to_hb_window(self, user):
        """ Untuk menuju halaman hitung biaya """
        self.ui = HitungBiayaWindow(self, user)
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    splash_pix = QtGui.QPixmap('../img/logo.jpg')
    splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    # add fade to splashscreen
    opaqueness = float(0.0)
    step = float(0.1)
    splash.setWindowOpacity(opaqueness)
    splash.show()
    while opaqueness < 1:
        splash.setWindowOpacity(opaqueness)
        time.sleep(step) # Gradually appears
        opaqueness+=step
    time.sleep(1) # hold image on screen for a while
    splash.close() # close the splash screen


    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
