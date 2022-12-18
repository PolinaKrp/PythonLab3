import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Task1 import create_csv_annotation
from Task2 import create_copy_dataset
from Task3 import create_randomname_file
from Task5 import IteratorTask1


class Ui_MainWindow(object):

    def setupUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        '''This function was created automatically by qtdesigner.
        Fields are being initialized here'''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #CCCCFF")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 550, 470))
        self.frame.setStyleSheet("background-color: #99FFCC;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 0, 350, 41))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(95)
        self.label.setFont(font)
        self.label.setStyleSheet("color: black;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(160, 100, 251, 170))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(
            r"C:\Users\79276\Desktop\Lab3Sem3\dataset"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.PathToDataset = QtWidgets.QLineEdit(self.centralwidget)
        self.PathToDataset.setGeometry(QtCore.QRect(60, 280, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PathToDataset.setFont(font)
        self.PathToDataset.setStyleSheet("background-color: #CCCCFF;\n"
                                         "border: 2px solid ##99FFCC;\n"
                                         "border-radius: 10px;\n"
                                         "color: black;")
        self.PathToDataset.setAlignment(QtCore.Qt.AlignCenter)
        self.PathToDataset.setObjectName("PathToDataset")
        self.NextLeopard = QtWidgets.QPushButton(self.centralwidget)
        self.NextLeopard.setGeometry(QtCore.QRect(30, 360, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.NextLeopard.setFont(font)
        self.NextLeopard.setStyleSheet("QPushButton{\n"
                                    "color:black;\n"
                                    "background-color: #CCCCFF;\n"
                                    "border-radius: 10;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed{\n"
                                    "    background-color:#FFCCFF;\n"
                                    "}\n"
                                    "")
        self.NextLeopard.setObjectName("NextLeopard")
        self.NextTiger = QtWidgets.QPushButton(self.centralwidget)
        self.NextTiger.setGeometry(QtCore.QRect(280, 360, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.NextTiger.setFont(font)
        self.NextTiger.setStyleSheet("QPushButton{\n"
                                     "color:black;\n"
                                     "background-color: #CCCCFF;\n"
                                     "border-radius: 10;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed{\n"
                                     "    background-color:#FFCCFF;\n"
                                     "}\n"
                                     "")
        self.NextTiger.setObjectName("NextTiger")
        self.CreateAnnotation = QtWidgets.QPushButton(self.centralwidget)
        self.CreateAnnotation.setGeometry(QtCore.QRect(110, 420, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.CreateAnnotation.setFont(font)
        self.CreateAnnotation.setStyleSheet("QPushButton{\n"
                                            "color:black;\n"
                                            "background-color: #CCCCFF;\n"
                                            "border-radius: 10;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed{\n"
                                            "    background-color:#FFCCFF;\n"
                                            "}\n"
                                            "")
        self.CreateAnnotation.setObjectName("CreateAnnotation")
        self.PathToDirOfDataset = QtWidgets.QLineEdit(self.centralwidget)
        self.PathToDirOfDataset.setGeometry(QtCore.QRect(60, 480, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PathToDirOfDataset.setFont(font)
        self.PathToDirOfDataset.setStyleSheet("background-color: #99FFCC;\n"
                                              "border: 2px solid #CCCCFF;\n"
                                              "border-radius: 10px;\n"
                                              "color: black;")
        self.PathToDirOfDataset.setAlignment(QtCore.Qt.AlignCenter)
        self.PathToDirOfDataset.setObjectName("PathToDirOfDataset")
        self.Task1 = QtWidgets.QPushButton(self.centralwidget)
        self.Task1.setGeometry(QtCore.QRect(30, 560, 121, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.Task1.setFont(font)
        self.Task1.setStyleSheet("QPushButton{\n"
                                 "color:black;\n"
                                 "background-color: #99FFCC;\n"
                                 "border-radius: 10;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed{\n"
                                 "    background-color:#CCFFCC;\n"
                                 "}\n"
                                 "")
        self.Task1.setObjectName("Task1")
        self.Task2 = QtWidgets.QPushButton(self.centralwidget)
        self.Task2.setGeometry(QtCore.QRect(180, 560, 131, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.Task2.setFont(font)
        self.Task2.setStyleSheet("QPushButton{\n"
                                 "color:black;\n"
                                 "background-color: #99FFCC;\n"
                                 "border-radius: 10;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed{\n"
                                 "    background-color:#CCFFCC;\n"
                                 "}\n"
                                 "")
        self.Task2.setObjectName("Task2")
        self.Task3 = QtWidgets.QPushButton(self.centralwidget)
        self.Task3.setGeometry(QtCore.QRect(330, 560, 131, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.Task3.setFont(font)
        self.Task3.setStyleSheet("QPushButton{\n"
                                 "color:black;\n"
                                 "background-color: #99FFCC;\n"
                                 "border-radius: 10;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed{\n"
                                 "    background-color:#CCFFCC;\n"
                                 "}\n"
                                 "")
        self.Task3.setObjectName("Task3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.__iterator_leopard = IteratorTask1()
        self.__iterator_tiger = IteratorTask1()
        self.add_functions()


    def retranslateUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        '''This function gives names to elements of buttons, labels etc,
        which was created in setupUI function'''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Dataset creator"))
        self.PathToDataset.setText(_translate(
            "MainWindow", "Enter path to dataset"))
        self.NextLeopard.setText(_translate("MainWindow", "Next leopard"))
        self.NextTiger.setText(_translate("MainWindow", "Next tiger"))
        self.CreateAnnotation.setText(
            _translate("MainWindow", "Create annotation"))
        self.PathToDirOfDataset.setText(_translate(
            "MainWindow", "Enter path to dir of dataset"))
        self.Task1.setText(_translate("MainWindow", "Task1"))
        self.Task2.setText(_translate("MainWindow", "Task2"))
        self.Task3.setText(_translate("MainWindow", "Task3"))


    def add_functions(self) -> None:
        '''This function adds an event handler.'''
        self.CreateAnnotation.clicked.connect(self.create_annotation)
        self.NextLeopard.clicked.connect(self.next_leopard)
        self.NextTiger.clicked.connect(self.next_tiger)
        self.Task1.clicked.connect(self.task1_exec)
        self.Task2.clicked.connect(self.task2_exec)
        self.Task3.clicked.connect(self.task3_exec)


    def next_leopard(self) -> None:
        '''This function is Iterator.
        It displays the next image of leopard on the screen untill the end.
        After that it begins with start.'''
        if self.__iterator_leopard.path == "":
            path = self.PathToDataset.text()
            if os.path.isdir(path):
                self.__iterator_leopard.path_init(os.path.join(path, "leopard"))
                self.__iterator_leopard.file_names_init()
                self.__iterator_leopard.limit_init()
                self.label_2.setPixmap(QtGui.QPixmap(
                self.__iterator_leopard.__next__()))
            else:
                self.ErrorMessage()
        else:
            self.label_2.setPixmap(QtGui.QPixmap(
            self.__iterator_leopard.__next__()))


    def next_tiger(self) -> None:
        '''This function is Iterator.
        It displays the next image of tiger on the screen untill the end.
        After that it begins with start.'''
        if self.__iterator_tiger.path == "":
            path = self.PathToDataset.text()
            if os.path.isdir(path):
                self.__iterator_tiger.path_init(os.path.join(path, "tiger"))
                self.__iterator_tiger.file_names_init()
                self.__iterator_tiger.limit_init()
                self.label_2.setPixmap(QtGui.QPixmap(
                self.__iterator_tiger.__next__()))
            else:
                self.ErrorMessage()
        else:
            self.label_2.setPixmap(QtGui.QPixmap(
            self.__iterator_tiger.__next__()))



    def create_annotation(self) -> None:
        '''This function creates csv file with abs path of class of dataset.'''
        path_to_dataset = self.PathToDataset.text()
        if os.path.isdir(path_to_dataset):
            try:
                create_csv_annotation(
                path_to_dataset.split("\\")[-1], "annotation.csv")
            except:
                self.ErrorMessage2()
        else:
            self.ErrorMessage()

