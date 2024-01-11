# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import json

# notes = {
#     "Ласкаво просимо":{
#         "текст":"Вітаю в моїй програмі",
#         "теги": ["тег1", "тег2"]
#     }
# }

# with open("notes.json", "w", encoding="utf-8") as file:
#     json.dump(notes, file)


class Ui_SmartNotes(object):
    def setupUi(self, SmartNotes):
        SmartNotes.setObjectName("SmartNotes")
        SmartNotes.resize(851, 594)
        self.centralwidget = QtWidgets.QWidget(SmartNotes)
        self.centralwidget.setObjectName("centralwidget")
        self.list_notes_text = QtWidgets.QLabel(self.centralwidget)
        self.list_notes_text.setGeometry(QtCore.QRect(590, 10, 141, 21))
        self.list_notes_text.setObjectName("list_notes_text")
        self.btn_create = QtWidgets.QPushButton(self.centralwidget)
        self.btn_create.setGeometry(QtCore.QRect(590, 210, 121, 21))
        self.btn_create.setObjectName("btn_create")
        self.btn_del = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del.setGeometry(QtCore.QRect(720, 210, 121, 21))
        self.btn_del.setObjectName("btn_del")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(590, 240, 251, 23))
        self.btn_save.setObjectName("btn_save")
        self.list_tags_text = QtWidgets.QLabel(self.centralwidget)
        self.list_tags_text.setGeometry(QtCore.QRect(590, 270, 91, 16))
        self.list_tags_text.setObjectName("list_tags_text")
        self.pole = QtWidgets.QLineEdit(self.centralwidget)
        self.pole.setGeometry(QtCore.QRect(590, 470, 251, 20))
        self.pole.setObjectName("pole")
        self.btn_add_tag = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_tag.setGeometry(QtCore.QRect(590, 500, 121, 21))
        self.btn_add_tag.setObjectName("btn_add_tag")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(590, 530, 251, 23))
        self.btn_search.setObjectName("btn_search")
        self.btn_del_tag = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del_tag.setGeometry(QtCore.QRect(720, 500, 121, 21))
        self.btn_del_tag.setObjectName("btn_del_tag")
        self.text = QtWidgets.QTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(10, 10, 571, 541))
        self.text.setObjectName("text")
        self.list_notes = QtWidgets.QListWidget(self.centralwidget)
        self.list_notes.setGeometry(QtCore.QRect(590, 30, 251, 171))
        self.list_notes.setObjectName("list_notes")
        self.list_notes_2 = QtWidgets.QListWidget(self.centralwidget)
        self.list_notes_2.setGeometry(QtCore.QRect(590, 290, 251, 171))
        self.list_notes_2.setObjectName("list_notes_2")
        SmartNotes.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SmartNotes)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 851, 21))
        self.menubar.setObjectName("menubar")
        SmartNotes.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SmartNotes)
        self.statusbar.setObjectName("statusbar")
        SmartNotes.setStatusBar(self.statusbar)

        self.retranslateUi(SmartNotes)
        QtCore.QMetaObject.connectSlotsByName(SmartNotes)

        self.list_notes.itemClicked.connect(self.show_notes)
        self.btn_create.clicked.connect(self.add_note)
        self.btn_del.clicked.connect(self.del_notes)
        self.btn_save.clicked.connect(self.save_note)

    def show_notes(self):
        key = self.list_notes.selectedItems()[0].text()
        self.text.setText(notes[key]["текст"])
        self.list_notes_2.clear()
        self.list_notes_2.addItems(notes[key]["теги"])

    def retranslateUi(self, SmartNotes):
        _translate = QtCore.QCoreApplication.translate
        SmartNotes.setWindowTitle(_translate("SmartNotes", "MainWindow"))
        self.list_notes_text.setText(_translate("SmartNotes", "Список заміток"))
        self.btn_create.setText(_translate("SmartNotes", "Створити замітку"))
        self.btn_del.setText(_translate("SmartNotes", "Видалити замітку"))
        self.btn_save.setText(_translate("SmartNotes", "Зберегти замітку"))
        self.list_tags_text.setText(_translate("SmartNotes", "Список тегів"))
        self.pole.setText(_translate("SmartNotes", "Введіть тег..."))
        self.btn_add_tag.setText(_translate("SmartNotes", "Додати до замітки"))
        self.btn_search.setText(_translate("SmartNotes", "Шукати замітку по тегу"))
        self.btn_del_tag.setText(_translate("SmartNotes", "Відкріпити від замітки"))


    def add_note(self):
        name, ok = QtWidgets.QInputDialog.getText(self.centralwidget, "Додати замітку", "Назва замітки:")
        if name != "" and ok:
            notes[name] = {"текст": "", "теги": []}
            self.list_notes.addItem(name)

    def del_notes(self):
        if self.list_notes.selectedItems():
            key = self.list_notes.selectedItems()[0].text()
            del notes[key]
            self.list_notes.clear()
            self.text.clear()
            self.list_tags_text.clear()
            self.list_notes.addItems(notes)
            
            with open("notes.json", "w", encoding="utf-8") as file:
                json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        else:
            win = QtWidgets.QMessageBox()
            win.setText("Замітка для видалення не вибрана!")
            win.exec()

    def save_note(self):
        if self.list_notes.selectedItems():
            key = self.list_notes.selectedItems()[0].text()
            notes[key]["текст"] = self.text.toPlainText()
            with open("notes.json", "w", encoding="utf-8") as file:
                json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        else:
            win = QtWidgets.QMessageBox()
            win.setText("Замітка для збереження не вибрана!")
            win.exec()




        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SmartNotes = QtWidgets.QMainWindow()
    ui = Ui_SmartNotes()
    ui.setupUi(SmartNotes)
    SmartNotes.show()
    with open("notes.json", "r", encoding = "utf-8") as file:
        notes = json.load(file)
    ui.list_notes.addItems(notes)




    sys.exit(app.exec_())
