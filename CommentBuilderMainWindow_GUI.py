from PyQt6 import QtCore, QtWidgets, QtGui


class Ui_CommentBuilderMainWindow_GUI(object):

    def setupUi(self, CommentBuilderMainWindowGUI):
        CommentBuilderMainWindowGUI.setObjectName("CommentBuilderMainWindowGUI")
        CommentBuilderMainWindowGUI.resize(506, 683)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("cb.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        CommentBuilderMainWindowGUI.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=CommentBuilderMainWindowGUI)
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
        self.rdoPerpendicularity.setGeometry(QtCore.QRect(150, 10, 111, 17))
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
        self.grpAlignment.setGeometry(QtCore.QRect(40, 110, 431, 131))
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
        self.chkFromTo.setGeometry(QtCore.QRect(40, 260, 70, 17))
        self.chkFromTo.setObjectName("chkFromTo")
        self.grpFromTo = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.grpFromTo.setGeometry(QtCore.QRect(40, 280, 191, 80))
        self.grpFromTo.setTitle("")
        self.grpFromTo.setObjectName("grpFromTo")
        self.lblFrom = QtWidgets.QLabel(parent=self.grpFromTo)
        self.lblFrom.setGeometry(QtCore.QRect(15, 30, 31, 16))
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
        self.chkUnequallyDisposed.setGeometry(QtCore.QRect(240, 260, 131, 17))
        self.chkUnequallyDisposed.setObjectName("chkUnequallyDisposed")
        self.grpUnequallyDisposed = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.grpUnequallyDisposed.setGeometry(QtCore.QRect(240, 280, 141, 80))
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
        self.grpView.setGeometry(QtCore.QRect(40, 380, 431, 141))
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
        self.chkSeptReq.setGeometry(QtCore.QRect(400, 260, 81, 17))
        self.chkSeptReq.setObjectName("chkSeptReq")
        self.chkAllAround = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.chkAllAround.setGeometry(QtCore.QRect(400, 290, 81, 17))
        self.chkAllAround.setObjectName("chkAllAround")
        self.txtOutput = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txtOutput.setGeometry(QtCore.QRect(40, 550, 371, 101))
        self.txtOutput.setObjectName("txtOutput")
        self.btnCopy = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnCopy.setGeometry(QtCore.QRect(420, 550, 51, 23))
        self.btnCopy.setObjectName("btnCopy")
        self.lblComment = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblComment.setGeometry(QtCore.QRect(40, 530, 61, 16))
        self.lblComment.setObjectName("lblComment")
        self.lblTolerance = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblTolerance.setGeometry(QtCore.QRect(50, 70, 61, 16))
        self.lblTolerance.setObjectName("lblTolerance")
        self.txtTolerance = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtTolerance.setGeometry(QtCore.QRect(110, 70, 113, 20))
        self.txtTolerance.setObjectName("txtTolerance")
        CommentBuilderMainWindowGUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(CommentBuilderMainWindowGUI)
        QtCore.QMetaObject.connectSlotsByName(CommentBuilderMainWindowGUI)

    def retranslateUi(self, CommentBuilderMainWindowGUI):
        _translate = QtCore.QCoreApplication.translate
        CommentBuilderMainWindowGUI.setWindowTitle(_translate("CommentBuilderMainWindowGUI", "Content Builder"))
        self.rdoProfile.setText(_translate("CommentBuilderMainWindowGUI", "Profile"))
        self.rdoFlatness.setText(_translate("CommentBuilderMainWindowGUI", "Flatness"))
        self.rdoPerpendicularity.setText(_translate("CommentBuilderMainWindowGUI", "Perpendicularity"))
        self.rdoInches.setText(_translate("CommentBuilderMainWindowGUI", "Inches"))
        self.rdoMM.setText(_translate("CommentBuilderMainWindowGUI", "MM"))
        self.grpAlignment.setTitle(_translate("CommentBuilderMainWindowGUI", "Alignment"))
        self.lblPrimary.setText(_translate("CommentBuilderMainWindowGUI", "Primary:"))
        self.lblSecondary.setText(_translate("CommentBuilderMainWindowGUI", "Secondary:"))
        self.lblTertiary.setText(_translate("CommentBuilderMainWindowGUI", "Tertiary:"))
        self.chkFromTo.setText(_translate("CommentBuilderMainWindowGUI", "From/To:"))
        self.lblFrom.setText(_translate("CommentBuilderMainWindowGUI", "From:"))
        self.lblTo.setText(_translate("CommentBuilderMainWindowGUI", "To:"))
        self.chkUnequallyDisposed.setText(_translate("CommentBuilderMainWindowGUI", "Unequally Disposed:"))
        self.lblAmount.setText(_translate("CommentBuilderMainWindowGUI", "Amount:"))
        self.grpView.setTitle(_translate("CommentBuilderMainWindowGUI", "Looking In:"))
        self.rdoViewISO.setText(_translate("CommentBuilderMainWindowGUI", "ISO"))
        self.rdoXPlus.setText(_translate("CommentBuilderMainWindowGUI", "X+"))
        self.rdoYPlus.setText(_translate("CommentBuilderMainWindowGUI", "Y+"))
        self.rdoZPlus.setText(_translate("CommentBuilderMainWindowGUI", "Z+"))
        self.rdoXMinus.setText(_translate("CommentBuilderMainWindowGUI", "X-"))
        self.rdoYMinus.setText(_translate("CommentBuilderMainWindowGUI", "Y-"))
        self.rdoZMinus.setText(_translate("CommentBuilderMainWindowGUI", "Z-"))
        self.chkSeptReq.setText(_translate("CommentBuilderMainWindowGUI", "Sept. Req."))
        self.chkAllAround.setText(_translate("CommentBuilderMainWindowGUI", "All Around"))
        self.btnCopy.setText(_translate("CommentBuilderMainWindowGUI", "Copy"))
        self.lblComment.setText(_translate("CommentBuilderMainWindowGUI", "Comment:"))
        self.lblTolerance.setText(_translate("CommentBuilderMainWindowGUI", "Tolerance:"))
        self.txtTolerance.setText(_translate("CommentBuilderMainWindowGUI", ".001"))





if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dude = QtWidgets.QMainWindow()
    ui = Ui_CommentBuilderMainWindow_GUI()
    ui.setupUi(dude)
    dude.show()
    sys.exit(app.exec())
