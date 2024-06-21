import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from Bhod import Vhod
from registrasia import Register
from profile import Profile
import sys


myConnection = sqlite3.connect("Baza1.db")
myCursor = myConnection.cursor()
app = QApplication(sys.argv)


acc_win = QMainWindow()
ch_win = QMainWindow()
sin_win = QMainWindow()
sup_win = QMainWindow()


acc_ui = Vhod()
sin_ui = Register()
sup_ui = Profile()


acc_ui.setupUi(acc_win)
sin_ui.setupUi(sin_win)
sup_ui.setupUi(sup_win)




def handle_login():
    email = acc_ui.Email_Vod.text()
    password = acc_ui.Pass_vod.text()
    myCursor.execute("SELECT * FROM Users WHERE Email=? AND Password=?", (email, password))
    user = myCursor.fetchone()
    if user:
        sup_ui.Name_profile_2.setText(user[1])
        sup_ui.Email_profile_2.setText(user[2])
        sup_win.show()
        acc_win.close()
    else:

        QMessageBox.information(acc_win, "Ошибка", "Неверный пароль/логин")

acc_ui.Vhod.clicked.connect(handle_login)


def handle_register():
    name = sin_ui.Name_vod_reg.text()
    email = sin_ui.Email_vod_reg.text()
    password = sin_ui.Pass_vod.text()
    try:
        good = False
        for i in list(email):
            if i == "@":
                good = True
        if good == True:
            myCursor.execute("INSERT INTO Users (UserName, Email, Password) VALUES (?, ?, ?)", (name, email, password))
            myConnection.commit()
            QMessageBox.information(sin_win, "Успешно", "Регистрация прошла успешно!")
            sin_win.close()
            acc_win.show()
        else:
            QMessageBox.information(sin_win, "Ошибка", "Почта недействительна")
    except sqlite3.IntegrityError:
        error_message = QMessageBox(QMessageBox.Warning, "Ошибка", "Этот email уже используется", QMessageBox.Ok)
        error_message.exec()

sin_ui.Zaregistr.clicked.connect(handle_register)

def handle_exit():
    sup_win.close()
    acc_win.show()

sup_ui.Vyhod.clicked.connect(handle_exit)


sin_ui.Vyhod.clicked.connect(lambda: [sin_win.close(), acc_win.show()])
acc_ui.Register.clicked.connect(lambda: [acc_win.close(), sin_win.show()])


acc_win.show()

app.exec()
myConnection.commit()
myConnection.close()