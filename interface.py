# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from sklearn.svm import SVC
import numpy as np
import cv2
import os
import joblib


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1220, 850)
                MainWindow.setMinimumSize(QtCore.QSize(1220, 850))
                MainWindow.setMaximumSize(QtCore.QSize(1220, 850))
                MainWindow.setStyleSheet("")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setStyleSheet("")
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(0, 0, 1221, 811))
                self.label.setAutoFillBackground(False)
                self.label.setStyleSheet("QLabel {\n"
                "    background-image: url(C:/Users/Len/Desktop/MASTER-SDSI/S2/TPs/MLProject/icons/ibg.jpg);\n"
                "    background-color: rgb(0,0,0,.8);\n"
                "}")
                self.label.setText("")
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(150, 20, 911, 621))
                self.label_2.setStyleSheet("z-index: 1;\n"
                "background-color: rgb(0, 0, 0, .85);\n"
                "border: 4px solid #405cf5;\n"
                "border-radius: 8px;")
                self.label_2.setText("")
                self.label_2.setScaledContents(True)
                self.label_2.setObjectName("label_2")
                self.openImage = QtWidgets.QPushButton(self.centralwidget)
                self.openImage.setGeometry(QtCore.QRect(260, 660, 241, 61))
                self.openImage.setStyleSheet("\n"
                "QPushButton {\n"
                "  appearance: button;\n"
                "  backface-visibility: hidden;\n"
                "  background-color: #405cf5;\n"
                "  border-radius: 6px;\n"
                "  border-width: 0;\n"
                "  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
                "  box-sizing: border-box;\n"
                "  color: #fff;\n"
                "  cursor: pointer;\n"
                "  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
                "  font-size: 100%;\n"
                "  height: 44px;\n"
                "  line-height: 1.15;\n"
                "  margin: 12px 0 0;\n"
                "  outline: none;\n"
                "  overflow: hidden;\n"
                "  padding: 0 25px;\n"
                "  position: relative;\n"
                "  text-align: center;\n"
                "  text-transform: none;\n"
                "  transform: translateZ(0);\n"
                "  transition: all .2s,box-shadow .08s ease-in;\n"
                "  user-select: none;\n"
                "  -webkit-user-select: none;\n"
                "  touch-action: manipulation;\n"
                "  width: 100%;\n"
                "}\n"
                "\n"
                "QPushButton:disabled {\n"
                "  cursor: default;\n"
                "}\n"
                "\n"
                "QPushButton:focus {\n"
                "  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset, rgba(50, 50, 93, .2) 0 6px 15px 0, rgba(0, 0, 0, .1) 0 2px 2px 0, rgba(50, 151, 211, .3) 0 0 0 4px;\n"
                "}\n"
                "\n"
                "QPushButton:hover {\n"
                "    background-color: #405ce0;\n"
                "}")
                self.openImage.setObjectName("openImage")
                self.classifier = QtWidgets.QPushButton(self.centralwidget)
                self.classifier.setGeometry(QtCore.QRect(720, 660, 241, 61))
                self.classifier.setStyleSheet("\n"
                "QPushButton {\n"
                "  appearance: button;\n"
                "  backface-visibility: hidden;\n"
                "  background-color: #405cf5;\n"
                "  border-radius: 6px;\n"
                "  border-width: 0;\n"
                "  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
                "  box-sizing: border-box;\n"
                "  color: #fff;\n"
                "  cursor: pointer;\n"
                "  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
                "  font-size: 100%;\n"
                "  height: 44px;\n"
                "  line-height: 1.15;\n"
                "  margin: 12px 0 0;\n"
                "  outline: none;\n"
                "  overflow: hidden;\n"
                "  padding: 0 25px;\n"
                "  position: relative;\n"
                "  text-align: center;\n"
                "  text-transform: none;\n"
                "  transform: translateZ(0);\n"
                "  transition: all .2s,box-shadow .08s ease-in;\n"
                "  user-select: none;\n"
                "  -webkit-user-select: none;\n"
                "  touch-action: manipulation;\n"
                "  width: 100%;\n"
                "}\n"
                "\n"
                "QPushButton:disabled {\n"
                "  cursor: default;\n"
                "}\n"
                "\n"
                "QPushButton:focus {\n"
                "  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset, rgba(50, 50, 93, .2) 0 6px 15px 0, rgba(0, 0, 0, .1) 0 2px 2px 0, rgba(50, 151, 211, .3) 0 0 0 4px;\n"
                "}\n"
                "\n"
                "QPushButton:hover {\n"
                "    background-color: #405ce0;\n"
                "}")
                self.classifier.setObjectName("classifier")
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 1220, 26))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                self.loadModel()
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.openImage.setText(_translate("MainWindow", "Ouvrir"))
                self.openImage.clicked.connect(self.loadImage)
                self.classifier.setText(_translate("MainWindow", "Classifier"))
                self.classifier.clicked.connect(self.predict)
        
        def loadImage(self):
                self.filename = QtWidgets.QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
                self.image = cv2.imread(self.filename)
                # self.image = cv2.resize(self.image, [501, 441])
                # self.firstImage = self.image.copy()
                self.setPhoto(self.image)
        
        def setPhoto(self,image):
                frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = QtGui.QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QtGui.QImage.Format_RGB888)
                try:
                        self.label_2.setPixmap(QtGui.QPixmap.fromImage(image))
                except Exception as e:
                        print(e)
        
        def loadModel(self):
                self.types = ['Limitation de vitesse 20', 'Limitation de vitesse 30', 'Limitation de vitesse 50', 'Limitation de vitesse 60', 'Limitation de vitesse 70', 'Limitation de vitesse 80',
                        'Fin de limitation de vitesse 80', 'Limitation de vitesse 100', 'Limitation de vitesse 120', 'Le depassement est interdit', 'Le depassement est interdit aux camions',
                        'Croisement d\'une route prioritaire', 'Prioritaire d\'une route', 'Cedez le passage à l\'intersection', 'Arret à l\'intersection', 'Circulation interdite dans les 2 sens',
                        'Acces interdit aux camions', 'Sens interdit', 'Danger non specifie', 'Virage a gauche', 'Virage a droite', 'Serie de virages dont le premier est a gauche', 'Cassis', 
                        'Chaussee glissante', 'Retrecissement de chaussee par la droite', 'Travaux', 'Croisement avec feux tricolores', 'Passage pieton', 'Passage d\'ecoliers', 'Debouche de cyclistes',
                        'Neige', 'Passage d\'animaux sauvages', 'Fin de toutes les interdictions', 'Direction obligatoire a la prochaine intersection : a droite', 'Direction obligatoire a la prochaine intersection : a gauche',
                        'Direction obligatoire a la prochaine intersection : tout droit', 'Directions obligatoires a la prochaine intersection : tout droit ou a droite',
                        'Directions obligatoires a la prochaine intersection : tout droit ou a gauche', 'Obligation de contournement par la droite', 'Obligation de contournement par la gauche',
                        'Roundabout', 'Fin d’interdiction de depasser', 'Fin d’interdiction de depasser pour les camions']
                self.model = joblib.load('svc_model_32.joblib')
        
        def predict(self):
                try:
                        img = self.image

                        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

                        lower_red = np.array([0, 50, 50])
                        upper_red = np.array([10, 255, 255])
                        mask1 = cv2.inRange(hsv, lower_red, upper_red)

                        lower_red = np.array([170, 50, 50])
                        upper_red = np.array([180, 255, 255])
                        mask2 = cv2.inRange(hsv, lower_red, upper_red)

                        red_mask = mask1 + mask2

                        lower_blue = np.array([100, 50, 50])
                        upper_blue = np.array([130, 255, 255])
                        blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)

                        mask = red_mask + blue_mask

                        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
                        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
                        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

                        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


                        for cnt in contours:
                                area = cv2.contourArea(cnt)
                                if area > 500:
                                        (x, y, w, h) = cv2.boundingRect(cnt)
                                        aspect_ratio = float(w)/h
                                        if aspect_ratio >= 0.8 and aspect_ratio <= 1.2:
                                                if np.sum(red_mask[y:y+h, x:x+w]) > np.sum(blue_mask[y:y+h, x:x+w]):
                                                        roi = img[y-20:y+h+20, x-35:x+w+35]
                                                        roi = cv2.resize(roi, [32, 32])
                                                        pr = self.model.predict([roi.flatten()])
                                                        cv2.rectangle(img, (x,y), (x+w,y+h), (255, 255, 255), 2)  # Red sign
                                                        print(pr[0])
                                                        title = self.types[int(pr[0])]
                                                        font = cv2.FONT_HERSHEY_SIMPLEX
                                                        font_scale = 0.5
                                                        thickness = 1
                                                        text_size, _ = cv2.getTextSize(title, font, font_scale, thickness)
                                                        text_x = x + int((w - text_size[0]) / 2)
                                                        text_y = y - text_size[1]
                                                        cv2.putText(img, title, (text_x, text_y), font, font_scale, (0, 0, 255), thickness, cv2.LINE_AA)
                                                else:
                                                        roi = img[y-20:y+h+20, x-35:x+w+35]
                                                        roi = cv2.resize(roi, [32, 32])
                                                        pr = self.model.predict([roi.flatten()])
                                                        cv2.rectangle(img, (x,y), (x+w,y+h), (255, 255, 255), 2)  # Blue sign
                                                        print(pr[0])
                                                        title = self.types[int(pr[0])]
                                                        font = cv2.FONT_HERSHEY_SIMPLEX
                                                        font_scale = 0.5
                                                        thickness = 1
                                                        text_size, _ = cv2.getTextSize(title, font, font_scale, thickness)
                                                        text_x = x + int((w - text_size[0]) / 2)
                                                        text_y = y - text_size[1]
                                                        cv2.putText(img, title, (text_x, text_y), font, font_scale, (0, 0, 255), thickness, cv2.LINE_AA)

                        self.setPhoto(img)
                except Exception as e:
                        print(e)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
