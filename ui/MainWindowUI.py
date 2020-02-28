# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
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

import os
import sys
import time

from ShowCaptionUI import Ui_ShowCaption
from getCaption import caption

class Ui_MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(Ui_MainWindow, self).__init__(*args, **kwargs)
        self.save_path = "./cam_images"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(646, 157)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.available_cameras = QCameraInfo.availableCameras()

        self.viewfinder = QCameraViewfinder()
        self.viewfinder.show()
        # self.setCentralWidget(self.viewfinder)

        self.select_camera(0)

        self.captureImage = QtWidgets.QPushButton(self.centralwidget)
        self.captureImage.setGeometry(QtCore.QRect(280, 10, 113, 32))
        self.captureImage.setObjectName("captureImage")
        self.captureImage.clicked.connect(self.take_photo)

        self.captionImage = QtWidgets.QPushButton(self.centralwidget)
        self.captionImage.setGeometry(QtCore.QRect(280, 80, 113, 32))
        self.captionImage.setObjectName("captionImage")
        self.captionImage.clicked.connect(self.open_show_caption)

        self.imagePath = QtWidgets.QLineEdit(self.centralwidget)
        self.imagePath.setGeometry(QtCore.QRect(150, 51, 371, 20))
        self.imagePath.setObjectName("imagePath")

        self.imagePathLabel = QtWidgets.QLabel(self.centralwidget)
        self.imagePathLabel.setGeometry(QtCore.QRect(70, 50, 81, 21))
        self.imagePathLabel.setObjectName("imagePathLabel")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 646, 22))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")

        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Attention Beam Image Captioner"))
        self.captureImage.setText(_translate("MainWindow", "Capture"))
        self.captionImage.setText(_translate("MainWindow", "Caption Image"))
        self.imagePathLabel.setText(_translate("MainWindow", "Image Path:"))

    def select_camera(self, i):
        self.camera = QCamera(self.available_cameras[i])
        self.camera.setViewfinder(self.viewfinder)
        self.camera.setCaptureMode(QCamera.CaptureStillImage)
        self.camera.error.connect(lambda: self.alert(self.camera.errorString()))
        self.camera.start()

        self.capture = QCameraImageCapture(self.camera)
        self.capture.error.connect(lambda i, e, s: self.alert(s))
        self.capture.imageCaptured.connect(lambda d, i: self.statusBar.showMessage("Image %04d captured" % self.save_seq))

        self.current_camera_name = self.available_cameras[i].description()
        self.save_seq = 0

    def take_photo(self):
        timestamp = time.strftime("%d-%b-%Y-%H_%M_%S")
        image_path = os.path.join(self.save_path, "%s-%04d-%s.jpg" % (
            self.current_camera_name,
            self.save_seq,
            timestamp
        ))
        self.capture.capture(image_path)
        self.save_seq += 1

        self.imagePath.setText(image_path)
    
    def alert(self, s):
        """
        Handle errors coming from QCamera dn QCameraImageCapture by displaying alerts.
        """
        err = QErrorMessage(self)
        err.showMessage(s)

    def open_show_caption(self):
        image_path = self.imagePath.text()
        
        if len(image_path) == 0 or not os.path.exists(image_path):
            self.alert('Image path is not valid!!')
            return
        
        imageCaptionText = caption(image_path)

        if imageCaptionText is None:
            self.alert('Pretrained model files not found.')
            return

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ShowCaption()
        self.ui.setupUi(self.window, imageCaptionText, image_path)
        self.window.show()

if __name__ == "__main__":
    if not os.path.exists('./cam_images'):
        os.makedirs('./cam_images')

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
