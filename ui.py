from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1117, 898)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text = QtWidgets.QTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(10, 10, 561, 861))
        self.text.setObjectName("text")
        self.list_nontes_label = QtWidgets.QLabel(self.centralwidget)
        self.list_nontes_label.setGeometry(QtCore.QRect(590, 20, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.list_nontes_label.setFont(font)
        self.list_nontes_label.setObjectName("list_nontes_label")
        self.list_notes = QtWidgets.QListWidget(self.centralwidget)
        self.list_notes.setGeometry(QtCore.QRect(590, 50, 501, 251))
        self.list_notes.setObjectName("list_notes")
        self.btn_create_note = QtWidgets.QPushButton(self.centralwidget)
        self.btn_create_note.setGeometry(QtCore.QRect(590, 310, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_create_note.setFont(font)
        self.btn_create_note.setObjectName("btn_create_note")
        self.btn_del_note = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del_note.setGeometry(QtCore.QRect(850, 310, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_del_note.setFont(font)
        self.btn_del_note.setObjectName("btn_del_note")
        self.btn_save_note = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save_note.setGeometry(QtCore.QRect(590, 360, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_save_note.setFont(font)
        self.btn_save_note.setObjectName("btn_save_note")
        self.list_tag_label = QtWidgets.QLabel(self.centralwidget)
        self.list_tag_label.setGeometry(QtCore.QRect(590, 420, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.list_tag_label.setFont(font)
        self.list_tag_label.setObjectName("list_tag_label")
        self.list_tags = QtWidgets.QListWidget(self.centralwidget)
        self.list_tags.setGeometry(QtCore.QRect(590, 460, 501, 251))
        self.list_tags.setObjectName("list_tags")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(590, 830, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_search.setFont(font)
        self.btn_search.setObjectName("btn_search")
        self.btn_del_tag = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del_tag.setGeometry(QtCore.QRect(850, 780, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_del_tag.setFont(font)
        self.btn_del_tag.setObjectName("btn_del_tag")
        self.btn_add_tag = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_tag.setGeometry(QtCore.QRect(590, 780, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_add_tag.setFont(font)
        self.btn_add_tag.setObjectName("btn_add_tag")
        self.line_search = QtWidgets.QLineEdit(self.centralwidget)
        self.line_search.setGeometry(QtCore.QRect(590, 730, 501, 31))
        self.line_search.setObjectName("line_search")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Розумні замітки"))
        self.list_nontes_label.setText(_translate("mainWindow", "Список заміток"))
        self.btn_create_note.setText(_translate("mainWindow", "Створти замітку"))
        self.btn_del_note.setText(_translate("mainWindow", "Видалити замітку"))
        self.btn_save_note.setText(_translate("mainWindow", "Зберегти замітку"))
        self.list_tag_label.setText(_translate("mainWindow", "Список тегів"))
        self.btn_search.setText(_translate("mainWindow", "Шукати замітки по тегу"))
        self.btn_del_tag.setText(_translate("mainWindow", "Відкріпити від замітки"))
        self.btn_add_tag.setText(_translate("mainWindow", "Додати до замітки"))
        self.line_search.setPlaceholderText(_translate("mainWindow", "Введіть тег..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
