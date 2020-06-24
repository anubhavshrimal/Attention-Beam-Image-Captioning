# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModelDetails.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from MainWindowUI import Ui_MainWindow
import os

default_args = {
    'model':
    '../models/BEST_checkpoint_coco_5_cap_per_img_5_min_word_freq.pth.tar',
    'word_map': '../models/WORDMAP_coco_5_cap_per_img_5_min_word_freq.json',
    'beam': '4'
}


class Ui_ModelDetails(object):
    def __init__(self, *args, **kwargs):
        super(Ui_ModelDetails, self).__init__(*args, **kwargs)

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

        self.modelCheckpointText.setText(default_args['model'])
        self.wordMapPathText.setText(default_args['word_map'])
        self.beamWidthSizeText.setText(default_args['beam'])

        self.pushButton.clicked.connect(self.open_main_window)

        self.retranslateUi(ModelDetails)
        QtCore.QMetaObject.connectSlotsByName(ModelDetails)

    def open_main_window(self):
        model_path = self.modelCheckpointText.text()
        wordmap_path = self.wordMapPathText.text()
        try:
            beam_width = int(self.beamWidthSizeText.text())
        except:
            self.alert('Beam width must be an integer')
            return

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window, model_path, wordmap_path, beam_width)
        self.window.show()

    def retranslateUi(self, ModelDetails):
        _translate = QtCore.QCoreApplication.translate
        ModelDetails.setWindowTitle(_translate("ModelDetails", "MainWindow"))
        self.pushButton.setText(_translate("ModelDetails", "Ok"))
        self.modelCheckpointLabel.setText(
            _translate("ModelDetails", "Model Checkpoint Path:"))
        self.beamWidthSizeLabel.setText(
            _translate("ModelDetails", "Beam Width Size:"))
        self.wordMapPathLabel.setText(
            _translate("ModelDetails", "WordMap Path:"))

    def alert(self, s):
        """
        Handle errors by displaying alerts.
        """
        err = QErrorMessage(self)
        err.showMessage(s)

if __name__ == "__main__":
    if not os.path.exists('./cam_images'):
        os.makedirs('./cam_images')

    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModelDetails = QtWidgets.QMainWindow()
    ui = Ui_ModelDetails()
    ui.setupUi(ModelDetails)
    ModelDetails.show()
    sys.exit(app.exec_())
