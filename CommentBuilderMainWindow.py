# Form implementation generated from reading ui file 'CommentBuilderMainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CommentBuilderMainWindow_GUI(object):
    def setupUi(self, CommentBuilderMainWindow):
        CommentBuilderMainWindow.setObjectName("CommentBuilderMainWindow")
        CommentBuilderMainWindow.resize(506, 651)
        self.centralwidget = QtWidgets.QWidget(parent=CommentBuilderMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.grpDimensionType = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.grpDimensionType.setGeometry(QtCore.QRect(30, 20, 261, 41))
        self.grpDimensionType.setStyleSheet("border: 0px solid gray;")
        self.grpDimensionType.setTitle("")
        self.grpDimensionType.setFlat(True)
        self.grpDimensionType.setObjectName("grpDimensionType")
        self.rdoProfile = QtWidgets.QRadioButton(parent=self.grpDimensionType)
        self.rdoProfile.setGeometry(QtCore.QRect(20, 10, 61, 17))
        self.rdoProfile.setChecked(True)
        self.rdoProfile.setObjectName("rdoProfile")
        self.rdoFlatness = QtWidgets.QRadioButton(parent=self.grpDimensionType)
        self.rdoFlatness.setGeometry(QtCore.QRect(80, 10, 71, 17))
        self.rdoFlatness.setObjectName("rdoFlatness")
        self.rdoPerpendicularity = QtWidgets.QRadioButton(parent=self.grpDimensionType)
        self.rdoPerpendicularity.setGeometry(QtCore.QRect(150, 10, 110, 17))
        self.rdoPerpendicularity.setObjectName("rdoPerpendicularity")
        self.grpMeasurementType = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.grpMeasurementType.setGeometry(QtCore.QRect(300, 20, 191, 41))
        self.grpMeasurementType.setStyleSheet("border: 0px solid gray;")
        self.grpMeasurementType.setTitle("")
        self.grpMeasurementType.setFlat(False)
        self.grpMeasurementType.setObjectName("grpMeasurementType")
        self.rdoInches = QtWidgets.QRadioButton(parent=self.grpMeasurementType)
        self.rdoInches.setGeometry(QtCore.QRect(10, 10, 61, 17))
        self.rdoInches.setChecked(True)
        self.rdoInches.setObjectName("rdoInches")
        self.rdoMM = QtWidgets.QRadioButton(parent=self.grpMeasurementType)
        self.rdoMM.setGeometry(QtCore.QRect(70, 10, 82, 17))
        self.rdoMM.setObjectName("rdoMM")
        self.grpAlignment = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.grpAlignment.setGeometry(QtCore.QRect(40, 70, 431, 131))
        self.grpAlignment.setObjectName("grpAlignment")
        self.cboPrimary = QtWidgets.QComboBox(parent=self.grpAlignment)
        self.cboPrimary.setGeometry(QtCore.QRect(130, 30, 131, 22))
        self.cboPrimary.setEditable(True)
        self.cboPrimary.setObjectName("cboPrimary")
        self.cboSecondary = QtWidgets.QComboBox(parent=self.grpAlignment)
        self.cboSecondary.setEnabled(False)
        self.cboSecondary.setGeometry(QtCore.QRect(130, 60, 131, 22))
        self.cboSecondary.setEditable(True)
        self.cboSecondary.setObjectName("cboSecondary")
        self.cboTertiary = QtWidgets.QComboBox(parent=self.grpAlignment)
        self.cboTertiary.setEnabled(False)
        self.cboTertiary.setGeometry(QtCore.QRect(130, 90, 131, 22))
        self.cboTertiary.setEditable(True)
        self.cboTertiary.setObjectName("cboTertiary")
        self.splitter = QtWidgets.QSplitter(parent=self.grpAlignment)
        self.splitter.setGeometry(QtCore.QRect(20, 30, 55, 81))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter.setObjectName("splitter")
        self.lblPrimary = QtWidgets.QLabel(parent=self.splitter)
        self.lblPrimary.setObjectName("lblPrimary")
        self.lblSecondary = QtWidgets.QLabel(parent=self.splitter)
        self.lblSecondary.setObjectName("lblSecondary")
        self.lblTertiary = QtWidgets.QLabel(parent=self.splitter)
        self.lblTertiary.setObjectName("lblTertiary")
        self.chkFromTo = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.chkFromTo.setGeometry(QtCore.QRect(40, 220, 70, 17))
        self.chkFromTo.setObjectName("chkFromTo")
        self.grpFromTo = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.grpFromTo.setGeometry(QtCore.QRect(40, 240, 191, 80))
        self.grpFromTo.setTitle("")
        self.grpFromTo.setObjectName("grpFromTo")
        self.lblFrom = QtWidgets.QLabel(parent=self.grpFromTo)
        self.lblFrom.setGeometry(QtCore.QRect(20, 30, 31, 16))
        self.lblFrom.setObjectName("lblFrom")
        self.txtFrom = QtWidgets.QLineEdit(parent=self.grpFromTo)
        self.txtFrom.setEnabled(False)
        self.txtFrom.setGeometry(QtCore.QRect(50, 30, 51, 20))
        self.txtFrom.setObjectName("txtFrom")
        self.lblTo = QtWidgets.QLabel(parent=self.grpFromTo)
        self.lblTo.setGeometry(QtCore.QRect(110, 30, 21, 16))
        self.lblTo.setObjectName("lblTo")
        self.txtTo = QtWidgets.QLineEdit(parent=self.grpFromTo)
        self.txtTo.setEnabled(False)
        self.txtTo.setGeometry(QtCore.QRect(130, 30, 51, 20))
        self.txtTo.setObjectName("txtTo")
        self.chkUnequallyDisposed = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.chkUnequallyDisposed.setGeometry(QtCore.QRect(240, 220, 121, 17))
        self.chkUnequallyDisposed.setObjectName("chkUnequallyDisposed")
        self.grpUnequallyDisposed = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.grpUnequallyDisposed.setGeometry(QtCore.QRect(240, 240, 141, 80))
        self.grpUnequallyDisposed.setTitle("")
        self.grpUnequallyDisposed.setObjectName("grpUnequallyDisposed")
        self.lblAmount = QtWidgets.QLabel(parent=self.grpUnequallyDisposed)
        self.lblAmount.setGeometry(QtCore.QRect(10, 30, 47, 13))
        self.lblAmount.setObjectName("lblAmount")
        self.txtAmount = QtWidgets.QLineEdit(parent=self.grpUnequallyDisposed)
        self.txtAmount.setEnabled(False)
        self.txtAmount.setGeometry(QtCore.QRect(60, 30, 71, 20))
        self.txtAmount.setInputMask("")
        self.txtAmount.setObjectName("txtAmount")
        self.grpView = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.grpView.setGeometry(QtCore.QRect(40, 340, 431, 141))
        self.grpView.setObjectName("grpView")
        self.rdoViewISO = QtWidgets.QRadioButton(parent=self.grpView)
        self.rdoViewISO.setGeometry(QtCore.QRect(20, 30, 51, 17))
        self.rdoViewISO.setChecked(True)
        self.rdoViewISO.setObjectName("rdoViewISO")
        self.rdoXPlus = QtWidgets.QRadioButton(parent=self.grpView)
        self.rdoXPlus.setGeometry(QtCore.QRect(90, 30, 51, 17))
        self.rdoXPlus.setObjectName("rdoXPlus")
        self.rdoYPlus = QtWidgets.QRadioButton(parent=self.grpView)
        self.rdoYPlus.setGeometry(QtCore.QRect(90, 50, 51, 17))
        self.rdoYPlus.setObjectName("rdoYPlus")
        self.rdoZPlus = QtWidgets.QRadioButton(parent=self.grpView)
        self.rdoZPlus.setGeometry(QtCore.QRect(90, 70, 51, 17))
        self.rdoZPlus.setObjectName("rdoZPlus")
        self.rdoXMinus = QtWidgets.QRadioButton(parent=self.grpView)
        self.rdoXMinus.setGeometry(QtCore.QRect(150, 30, 82, 17))
        self.rdoXMinus.setObjectName("rdoXMinus")
        self.rdoYMinus = QtWidgets.QRadioButton(parent=self.grpView)
        self.rdoYMinus.setGeometry(QtCore.QRect(150, 50, 82, 17))
        self.rdoYMinus.setObjectName("rdoYMinus")
        self.rdoZMinus = QtWidgets.QRadioButton(parent=self.grpView)
        self.rdoZMinus.setGeometry(QtCore.QRect(150, 70, 82, 17))
        self.rdoZMinus.setObjectName("rdoZMinus")
        self.chkSeptReq = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.chkSeptReq.setGeometry(QtCore.QRect(400, 220, 70, 17))
        self.chkSeptReq.setObjectName("chkSeptReq")
        self.chkAllAround = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.chkAllAround.setGeometry(QtCore.QRect(400, 250, 70, 17))
        self.chkAllAround.setObjectName("chkAllAround")
        self.txtOutput = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txtOutput.setGeometry(QtCore.QRect(40, 510, 371, 101))
        self.txtOutput.setObjectName("txtOutput")
        self.btnCopy = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnCopy.setGeometry(QtCore.QRect(420, 510, 51, 23))
        self.btnCopy.setObjectName("btnCopy")
        self.lblComment = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblComment.setGeometry(QtCore.QRect(40, 490, 51, 16))
        self.lblComment.setObjectName("lblComment")
        CommentBuilderMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CommentBuilderMainWindow)
        QtCore.QMetaObject.connectSlotsByName(CommentBuilderMainWindow)

    def retranslateUi(self, CommentBuilderMainWindowGUI):
        _translate = QtCore.QCoreApplication.translate
        CommentBuilderMainWindowGUI.setWindowTitle(_translate("CommentBuilderMainWindow", "MainWindow"))
        self.rdoProfile.setText(_translate("CommentBuilderMainWindow", "Profile"))
        self.rdoFlatness.setText(_translate("CommentBuilderMainWindow", "Flatness"))
        self.rdoPerpendicularity.setText(_translate("CommentBuilderMainWindow", "Perpendicularity"))
        self.rdoInches.setText(_translate("CommentBuilderMainWindow", "Inches"))
        self.rdoMM.setText(_translate("CommentBuilderMainWindow", "MM"))
        self.grpAlignment.setTitle(_translate("CommentBuilderMainWindow", "Alignment"))
        self.lblPrimary.setText(_translate("CommentBuilderMainWindow", "Primary:"))
        self.lblSecondary.setText(_translate("CommentBuilderMainWindow", "Secondary:"))
        self.lblTertiary.setText(_translate("CommentBuilderMainWindow", "Tertiary:"))
        self.chkFromTo.setText(_translate("CommentBuilderMainWindow", "From/To:"))
        self.lblFrom.setText(_translate("CommentBuilderMainWindow", "From:"))
        self.lblTo.setText(_translate("CommentBuilderMainWindow", "To:"))
        self.chkUnequallyDisposed.setText(_translate("CommentBuilderMainWindow", "Unequally Disposed:"))
        self.lblAmount.setText(_translate("CommentBuilderMainWindow", "Amount:"))
        self.grpView.setTitle(_translate("CommentBuilderMainWindow", "Looking In:"))
        self.rdoViewISO.setText(_translate("CommentBuilderMainWindow", "ISO"))
        self.rdoXPlus.setText(_translate("CommentBuilderMainWindow", "X+"))
        self.rdoYPlus.setText(_translate("CommentBuilderMainWindow", "Y+"))
        self.rdoZPlus.setText(_translate("CommentBuilderMainWindow", "Z+"))
        self.rdoXMinus.setText(_translate("CommentBuilderMainWindow", "X-"))
        self.rdoYMinus.setText(_translate("CommentBuilderMainWindow", "Y-"))
        self.rdoZMinus.setText(_translate("CommentBuilderMainWindow", "Z-"))
        self.chkSeptReq.setText(_translate("CommentBuilderMainWindow", "Sept. Req."))
        self.chkAllAround.setText(_translate("CommentBuilderMainWindow", "All Around"))
        self.btnCopy.setText(_translate("CommentBuilderMainWindow", "Copy"))
        self.lblComment.setText(_translate("CommentBuilderMainWindow", "Comment:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CommentBuilderMainWindow = QtWidgets.QMainWindow()
    ui = Ui_CommentBuilderMainWindow_GUI()
    ui.setupUi(CommentBuilderMainWindow)
    CommentBuilderMainWindow.show()
    sys.exit(app.exec())
