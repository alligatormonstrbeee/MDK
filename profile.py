from PyQt6 import QtCore, QtGui, QtWidgets

class Profile(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(405, 318)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Vyhod = QtWidgets.QPushButton(self.centralwidget)
        self.Vyhod.setGeometry(QtCore.QRect(190, 260, 75, 23))
        self.Vyhod.setObjectName("Vyhod")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Typewriter")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.Name_profile = QtWidgets.QLabel(self.centralwidget)
        self.Name_profile.setGeometry(QtCore.QRect(20, 50, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Name_profile.setFont(font)
        self.Name_profile.setObjectName("Name_profile")

        self.Name_profile_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Name_profile_2.setGeometry(QtCore.QRect(20, 90, 113, 20))
        self.Name_profile_2.setObjectName("Name_profile_2")

        self.Email_profile = QtWidgets.QLabel(self.centralwidget)
        self.Email_profile.setGeometry(QtCore.QRect(20, 120, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Email_profile.setFont(font)
        self.Email_profile.setObjectName("Email_profile")

        self.Email_profile_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Email_profile_2.setGeometry(QtCore.QRect(20, 160, 113, 20))
        self.Email_profile_2.setObjectName("Email_profile_2")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 60, 231, 161))
        self.label_2.setText("")
        try:
            self.label_2.setPixmap(QtGui.QPixmap("balenci.jpg"))
        except Exception as e:
            print(f"Ошибка при загрузке изображения: {e}")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 461, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главное Окно"))
        self.Vyhod.setText(_translate("MainWindow", "Выход"))
        self.label.setText(_translate("MainWindow", "Профиль"))
        self.Name_profile.setText(_translate("MainWindow", "Имя"))
        self.Email_profile.setText(_translate("MainWindow", "Эл. почта"))

    def setName(self, name):
        self.Name_profile_2.setText(name)

    def setEmail(self, email):
        self.Email_profile_2.setText(email)

    def getName(self):
        return self.Name_profile_2.text()

    def getEmail(self):
        return self.Email_profile_2.text()
