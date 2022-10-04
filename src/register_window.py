""" Halaman Register """

import re
import mariadb
from PyQt5 import QtCore, QtGui, QtWidgets
from exception import RegisterError


class RegisterWindow():
    def __init__(self, main_window):
        """ Inisiasi Kelas RegisterWindow """
        main_window.setObjectName("RegisterWindow")
        main_window.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        main_window.setCentralWidget(self.centralwidget)

        font = QtGui.QFont()
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.text_edit_email = QtWidgets.QTextEdit(self.centralwidget)
        self.text_edit_username = QtWidgets.QTextEdit(self.centralwidget)
        self.text_edit_password = QtWidgets.QTextEdit(self.centralwidget)
        self.push_button_reg_admin = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_reg_cust = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_login = QtWidgets.QPushButton(self.centralwidget)

        font.setPointSize(24)
        self.label_title.setObjectName("label_title")
        self.label_title.setGeometry(QtCore.QRect(0, 40, 800, 64))
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setFont(font)

        font.setPointSize(12)
        self.label_1.setObjectName("label_1")
        self.label_1.setGeometry(QtCore.QRect(270, 140, 260, 22))
        self.label_1.setFont(font)

        font.setPointSize(10)
        self.text_edit_email.setObjectName("text_edit_email")
        self.text_edit_email.setGeometry(QtCore.QRect(270, 170, 260, 38))
        self.text_edit_email.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_edit_email.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.text_edit_email.setFont(font)

        font.setPointSize(12)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QtCore.QRect(270, 230, 260, 22))
        self.label_2.setFont(font)

        font.setPointSize(10)
        self.text_edit_username.setObjectName("text_edit_username")
        self.text_edit_username.setGeometry(QtCore.QRect(270, 260, 260, 38))
        self.text_edit_username.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_edit_username.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.text_edit_username.setFont(font)
        font.setPointSize(10)

        font.setPointSize(12)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QtCore.QRect(270, 320, 260, 22))
        self.label_3.setFont(font)

        font.setPointSize(10)
        self.text_edit_password.setObjectName("text_edit_password")
        self.text_edit_password.setGeometry(QtCore.QRect(270, 350, 260, 38))
        self.text_edit_password.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_edit_password.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.text_edit_password.setFont(font)

        font.setPointSize(8)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QtCore.QRect(270, 390, 300, 25))
        self.label_5.setFont(font)
        pal = self.label_5.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"))
        self.label_5.setPalette(pal)

        font.setPointSize(9)
        self.push_button_reg_admin.setObjectName("push_button_reg_admin")
        self.push_button_reg_admin.setGeometry(QtCore.QRect(240, 430, 180, 30))
        self.push_button_reg_admin.setFont(font)
        self.push_button_reg_admin.clicked.connect(lambda: self.register_clicked('admin'))

        font.setPointSize(9)
        self.push_button_reg_cust.setObjectName("push_button_reg_cust")
        self.push_button_reg_cust.setGeometry(QtCore.QRect(240, 465, 180, 30))
        self.push_button_reg_cust.setFont(font)
        self.push_button_reg_cust.clicked.connect(lambda: self.register_clicked('customer'))

        font.setPointSize(9)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QtCore.QRect(460, 435, 120, 22))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setFont(font)

        font.setPointSize(9)
        self.push_button_login.setObjectName("push_button_login")
        self.push_button_login.setGeometry(QtCore.QRect(460, 455, 120, 30))
        self.push_button_login.setFont(font)
        self.push_button_login.clicked.connect(main_window.to_login_window)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_title.setText(_translate("RegisterWindow", "Register"))
        self.label_1.setText(_translate("RegisterWindow", "Email"))
        self.label_2.setText(_translate("RegisterWindow", "Username"))
        self.label_3.setText(_translate("RegisterWindow", "Password"))
        self.push_button_reg_admin.setText(_translate("RegisterWindow", "Submit as Admin"))
        self.push_button_reg_cust.setText(_translate("RegisterWindow", "Submit as Customer"))
        self.label_4.setText(_translate("RegisterWindow", "Punya Akun?"))
        self.push_button_login.setText(_translate("RegisterWindow", "Login"))

    def clear_form(self):
        """ Membersihkan form input pengguna """
        _translate = QtCore.QCoreApplication.translate
        self.text_edit_email.setText(_translate("RegisterWindow", ""))
        self.text_edit_username.setText(_translate("RegisterWindow", ""))
        self.text_edit_password.setText(_translate("RegisterWindow", ""))

    def register_clicked(self, role):
        """ Fungsi yang dipanggil setelah diklik """
        _translate = QtCore.QCoreApplication.translate
        email = self.text_edit_email.toPlainText()
        username = self.text_edit_username.toPlainText()
        password = self.text_edit_password.toPlainText()
        try:
            register(email, username, password, role)
        except RegisterError as e:
            pal = self.label_5.palette()
            pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"))
            self.label_5.setPalette(pal)
            self.label_5.setText(_translate("RegisterWindow", e.message))
            return

        # Color to blue
        pal = self.label_5.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("blue"))
        self.label_5.setPalette(pal)

        _translate = QtCore.QCoreApplication.translate
        self.label_5.setText(_translate("RegisterWindow", "Berhasil registrasi"))

        # Clear form
        self.clear_form()


def register(email, username, password, role):
    """ Fungsi untuk melakukan register """
    if not valid_form(email, username, password):
        raise RegisterError("Isi form dengan lengkap")

    if not valid_email(email):
        raise RegisterError("Masukkan email yang valid")

    if not valid_username_space(username):
        raise RegisterError("Username tidak boleh mengandung spasi")

    if not valid_username_length(username):
        raise RegisterError("Username minimal 5 karakter")

    if not valid_password(password):
        raise RegisterError("Password minimal 8 karakter")

    try:
        conn = mariadb.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="parkco"
        )
        cur = conn.cursor(buffered=True)

        # Check email uniqueness
        query = f"SELECT * FROM `account`" \
                f"WHERE email = '{email}';"
        cur.execute(query)
        if cur.rowcount > 0:
            raise RegisterError("Email sudah terpakai")

        # Check username uniqueness
        query = f"SELECT * FROM `account`" \
                f"WHERE username = '{username}';"
        cur.execute(query)
        if cur.rowcount > 0:
            raise RegisterError("Username sudah terpakai")

        # Insert to database
        if role == 'admin':
            query = "INSERT INTO `informasiparkiran` ()" \
                    "VALUES ();"
            cur.execute(query)

            query = f"INSERT INTO `admin` (email, username, password, idParkiran) " \
                    f"VALUES ('{email}', '{username}', '{password}', LAST_INSERT_ID());"
            cur.execute(query)

        else:   # role == 'customer'
            query = f"INSERT INTO `customer` (email, username, password) " \
                    f"VALUES ('{email}', '{username}', '{password}');"

            cur.execute(query)

        conn.commit()
        conn.close()

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")


def valid_form(email, username, password):
    """ Mengecek apakah form valid """
    return not (email == '' or username == '' or password == '')


def valid_email(email):
    """ Mengecek apakah email valid """
    return re.search(r'^[\w\.\-\+]+@[\w\.\-\+]+\.\w+(?:\.\w+)*$', email)


def valid_username_space(username):
    """ Mengecek apakah username valid """
    return ' ' not in username


def valid_username_length(username):
    """ Mengecek apakah panjang username valid """
    return len(username) >= 5


def valid_password(password):
    """ Mengecek apakah panjang password valid """
    return len(password) >= 8
