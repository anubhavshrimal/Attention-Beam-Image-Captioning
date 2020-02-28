# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShowCaption.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShowCaption(object):
    def setupUi(self, ShowCaption, imageCaptionText, image_path):
        ShowCaption.setObjectName("ShowCaption")
        ShowCaption.resize(646, 460)
        self.centralwidget = QtWidgets.QWidget(ShowCaption)
        self.centralwidget.setObjectName("centralwidget")

        self.captionTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.captionTextBox.setGeometry(QtCore.QRect(150, 290, 371, 81))
        self.captionTextBox.setObjectName("captionTextBox")
        self.captionTextBox.setText(imageCaptionText)

        self.imageCaptionLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageCaptionLabel.setGeometry(QtCore.QRect(40, 320, 91, 20))
        self.imageCaptionLabel.setObjectName("imageCaptionLabel")

        self.imageDisplayLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageDisplayLabel.setGeometry(QtCore.QRect(130, 10, 411, 261))
        self.imageDisplayLabel.setText("")
        self.imageDisplayLabel.setObjectName("imageDisplayLabel")

        self.imageDisplayLabel.setScaledContents(True)
        self.imageDisplayLabel.setPixmap(QtGui.QPixmap(image_path))

        ShowCaption.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ShowCaption)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 646, 22))
        self.menubar.setObjectName("menubar")
        ShowCaption.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ShowCaption)
        self.statusbar.setObjectName("statusbar")
        ShowCaption.setStatusBar(self.statusbar)

        self.retranslateUi(ShowCaption)
        QtCore.QMetaObject.connectSlotsByName(ShowCaption)

    def retranslateUi(self, ShowCaption):
        _translate = QtCore.QCoreApplication.translate
        ShowCaption.setWindowTitle(_translate("ShowCaption", "ShowCaption"))
        self.imageCaptionLabel.setText(_translate("ShowCaption", "Image Caption:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShowCaption = QtWidgets.QMainWindow()
    ui = Ui_ShowCaption()
    ui.setupUi(ShowCaption)
    ShowCaption.show()
    sys.exit(app.exec_())
