# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModelDetails.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ModelDetails(object):
    def setupUi(self, ModelDetails):
        ModelDetails.setObjectName("ModelDetails")
        ModelDetails.resize(610, 259)
        self.centralwidget = QtWidgets.QWidget(ModelDetails)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 150, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.modelCheckpointLabel = QtWidgets.QLabel(self.centralwidget)
        self.modelCheckpointLabel.setGeometry(QtCore.QRect(30, 29, 151, 21))
        self.modelCheckpointLabel.setObjectName("modelCheckpointLabel")
        self.modelCheckpointText = QtWidgets.QLineEdit(self.centralwidget)
        self.modelCheckpointText.setGeometry(QtCore.QRect(190, 30, 371, 20))
        self.modelCheckpointText.setObjectName("modelCheckpointText")
        self.beamWidthSizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.beamWidthSizeLabel.setGeometry(QtCore.QRect(30, 109, 151, 21))
        self.beamWidthSizeLabel.setObjectName("beamWidthSizeLabel")
        self.beamWidthSizeText = QtWidgets.QLineEdit(self.centralwidget)
        self.beamWidthSizeText.setGeometry(QtCore.QRect(190, 110, 371, 20))
        self.beamWidthSizeText.setObjectName("beamWidthSizeText")
        self.wordMapPathLabel = QtWidgets.QLabel(self.centralwidget)
        self.wordMapPathLabel.setGeometry(QtCore.QRect(30, 69, 151, 21))
        self.wordMapPathLabel.setObjectName("wordMapPathLabel")
        self.wordMapPathText = QtWidgets.QLineEdit(self.centralwidget)
        self.wordMapPathText.setGeometry(QtCore.QRect(190, 70, 371, 20))
        self.wordMapPathText.setObjectName("wordMapPathText")
        ModelDetails.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ModelDetails)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 22))
        self.menubar.setObjectName("menubar")
        ModelDetails.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ModelDetails)
        self.statusbar.setObjectName("statusbar")
        ModelDetails.setStatusBar(self.statusbar)

        self.retranslateUi(ModelDetails)
        QtCore.QMetaObject.connectSlotsByName(ModelDetails)

    def retranslateUi(self, ModelDetails):
        _translate = QtCore.QCoreApplication.translate
        ModelDetails.setWindowTitle(_translate("ModelDetails", "MainWindow"))
        self.pushButton.setText(_translate("ModelDetails", "Ok"))
        self.modelCheckpointLabel.setText(_translate("ModelDetails", "Model Checkpoint Path:"))
        self.beamWidthSizeLabel.setText(_translate("ModelDetails", "Beam Width Size:"))
        self.wordMapPathLabel.setText(_translate("ModelDetails", "WordMap Path:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModelDetails = QtWidgets.QMainWindow()
    ui = Ui_ModelDetails()
    ui.setupUi(ModelDetails)
    ModelDetails.show()
    sys.exit(app.exec_())
