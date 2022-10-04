""" Halaman Login """

from PyQt5 import QtCore, QtGui, QtWidgets
import mariadb
from exception import LoginError
import entity


class LoginWindow():
    def __init__(self, main_window):
        """ Inisiasi Halaman Login """
        main_window.setObjectName("LoginWindow")
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
        self.text_edit_username = QtWidgets.QTextEdit(self.centralwidget)
        self.line_edit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.push_button_login = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_register = QtWidgets.QPushButton(self.centralwidget)

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
        self.text_edit_username.setObjectName("text_edit_username")
        self.text_edit_username.setGeometry(QtCore.QRect(270, 170, 260, 38))
        self.text_edit_username.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_edit_username.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.text_edit_username.setFont(font)

        font.setPointSize(12)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QtCore.QRect(270, 230, 260, 22))
        self.label_2.setFont(font)

        font.setPointSize(10)
        self.line_edit_password.setObjectName("line_edit_password")
        self.line_edit_password.setGeometry(QtCore.QRect(270, 260, 260, 38))
        self.line_edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_edit_password.setFont(font)

        font.setPointSize(8)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QtCore.QRect(270, 300, 300, 25))
        self.label_4.setFont(font)
        pal = self.label_4.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"))
        self.label_4.setPalette(pal)

        font.setPointSize(11)
        self.push_button_login.setObjectName("push_button_login")
        self.push_button_login.setGeometry(QtCore.QRect(340, 340, 120, 38))
        self.push_button_login.setFont(font)
        self.push_button_login.clicked.connect(lambda: self.login_clicked(main_window))

        font.setPointSize(9)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QtCore.QRect(0, 440, 800, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setFont(font)

        font.setPointSize(9)
        self.push_button_register.setObjectName("push_button_register")
        self.push_button_register.setGeometry(QtCore.QRect(340, 480, 120, 30))
        self.push_button_register.setFont(font)
        self.push_button_register.clicked.connect(main_window.to_register_window)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_title.setText(_translate("LoginWindow", "Login"))
        self.label_1.setText(_translate("LoginWindow", "Username"))
        self.label_2.setText(_translate("LoginWindow", "Password"))
        self.push_button_login.setText(_translate("LoginWindow", "Login"))
        self.label_3.setText(_translate("LoginWindow", "Belum punya akun?"))
        self.push_button_register.setText(_translate("LoginWindow", "Register"))

    def login_clicked(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        username = self.text_edit_username.toPlainText()
        password = self.line_edit_password.text()
        try:
            id, role = login(username, password)
            if role == 'admin':
                main_window.to_admin_window(entity.Admin(id))
            elif role == 'customer':
                main_window.to_search_window(entity.Customer(id))
        except LoginError as e:
            self.label_4.setText(_translate("LoginWindow", e.message))
            return


def login(username, password):
    if not valid_form(username, password):
        raise LoginError("Isi form dengan lengkap")

    if not valid_username(username):
        raise LoginError("Username tidak boleh mengandung spasi")

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
        for role in ['admin', 'customer']:
            query = f"SELECT id, password FROM `{role}`" \
                    f"WHERE username = '{username}';"
            cur.execute(query)
            if cur.rowcount != 0:       # found username
                for (id, password_sql) in cur:
                    break

                if password_sql != password:
                    conn.close()
                    raise LoginError("Password salah")

                conn.close()
                return id, role

        conn.close()
        raise LoginError("Username tidak ditemukan")

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")


def valid_form(username, password):
    return not (username == '' or password == '')


def valid_username(username):
    return ' ' not in username
