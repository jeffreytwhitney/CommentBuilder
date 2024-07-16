
import pyperclip
from PyQt6 import QtWidgets

from CommentBuilderMainWindow_GUI import Ui_CommentBuilderMainWindow_GUI


class CommentBuilderMainWindow(QtWidgets.QMainWindow, Ui_CommentBuilderMainWindow_GUI):
    primary_datum_list = ["Itself", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
                          "P",
                          "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    secondary_datum_list = ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                            "Q",
                            "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    #Events
    def _btn_clicked(self):
        output_text = self.txtOutput.toPlainText()
        pyperclip.copy(output_text)

    def _textbox_text_changed(self):
        self.generate_comment()

    def _checkbox_stateChanged(self):
        self.generate_comment()

    def _chkFromTo_stateChanged(self):
        self.txtFrom.setText("")
        self.txtTo.setText("")

        if self.chkFromTo.isChecked():
            self.txtFrom.setEnabled(True)
            self.txtTo.setEnabled(True)
        else:
            self.txtFrom.setEnabled(False)
            self.txtTo.setEnabled(False)

    def _chkUnequallyDisposed_stateChanged(self):
        self.txtAmount.setText("")
        self.txtAmount.setEnabled(self.chkUnequallyDisposed.isChecked())

    def _primary_datum_changed(self, index):
        if self.rdoPerpendicularity.isChecked():
            self.cboSecondary.setEnabled(False)
            self.cboTertiary.setEnabled(False)
            return

        self.cboSecondary.clear()
        self.cboTertiary.clear()
        self.cboSecondary.addItems(self.secondary_datum_list)
        self.cboTertiary.addItems(self.secondary_datum_list)

        if index > 0:
            self.cboSecondary.removeItem(index)
            self.cboTertiary.removeItem(index)

        self.cboSecondary.setCurrentIndex(0)
        self.cboTertiary.setCurrentIndex(0)
        self.cboSecondary.setEnabled(index != 0)
        self.cboTertiary.setEnabled(index != 0)
        self.generate_comment()

    def _radio_toggled(self, enabled):
        self.generate_comment()

    def _profile_toggled(self, enabled):
        self.cboPrimary.clear()
        self.cboPrimary.addItems(self.primary_datum_list)
        self.cboPrimary.setCurrentIndex(0)
        self.cboSecondary.setCurrentIndex(0)
        self.cboTertiary.setCurrentIndex(0)
        self.cboPrimary.setEnabled(True)
        self.cboSecondary.setEnabled(False)
        self.cboTertiary.setEnabled(False)
        self.chkAllAround.setEnabled(True)
        self.chkSeptReq.setEnabled(True)
        self.chkFromTo.setEnabled(True)
        self.chkUnequallyDisposed.setEnabled(True)
        self.txtAmount.setText("")
        self.txtTo.setText("")
        self.txtFrom.setText("")

    def _flatness_toggled(self, enabled):
        self.cboPrimary.setCurrentIndex(0)
        self.cboSecondary.setCurrentIndex(0)
        self.cboTertiary.setCurrentIndex(0)
        self.cboPrimary.setEnabled(False)
        self.cboSecondary.setEnabled(False)
        self.cboTertiary.setEnabled(False)
        self.chkAllAround.setChecked(False)
        self.chkSeptReq.setChecked(False)
        self.chkAllAround.setEnabled(False)
        self.chkSeptReq.setEnabled(False)
        self.chkFromTo.setEnabled(False)
        self.chkUnequallyDisposed.setEnabled(False)
        self.txtAmount.setText("")
        self.txtTo.setText("")
        self.txtFrom.setText("")
        self.generate_comment()

    def _perpendicularity_toggled(self, enabled):
        self.cboPrimary.clear()
        self.cboPrimary.addItems(self.primary_datum_list)
        self.cboPrimary.removeItem(0)
        self.cboPrimary.setCurrentIndex(0)

        self.cboSecondary.setCurrentIndex(0)
        self.cboTertiary.setCurrentIndex(0)
        self.cboPrimary.setEnabled(True)
        self.cboSecondary.setEnabled(False)
        self.cboTertiary.setEnabled(False)
        self.chkAllAround.setChecked(False)
        self.chkSeptReq.setChecked(False)
        self.chkAllAround.setEnabled(False)
        self.chkSeptReq.setEnabled(False)
        self.chkFromTo.setEnabled(False)
        self.chkUnequallyDisposed.setEnabled(False)
        self.txtAmount.setText("")
        self.txtTo.setText("")
        self.txtFrom.setText("")
        self.generate_comment()

    def _secondary_datum_changed(self, index):
        self.cboTertiary.setCurrentIndex(0)
        if self.cboSecondary.currentIndex() > 0:
            self.cboTertiary.clear()
            self.cboTertiary.addItems(self.secondary_datum_list)
            self.cboTertiary.removeItem(self.cboPrimary.currentIndex())
            self.cboTertiary.removeItem(self.cboSecondary.currentIndex())
        self.generate_comment()

    def _tertiary_datum_changed(self, index):

        self.generate_comment()

    # Public Functions
    def bind_events(self):
        self.chkAllAround.stateChanged.connect(self._checkbox_stateChanged)
        self.chkSeptReq.stateChanged.connect(self._checkbox_stateChanged)
        self.chkUnequallyDisposed.stateChanged.connect(self._chkUnequallyDisposed_stateChanged)
        self.chkFromTo.stateChanged.connect(self._chkFromTo_stateChanged)

        self.rdoProfile.toggled.connect(self._profile_toggled)
        self.rdoFlatness.toggled.connect(self._flatness_toggled)
        self.rdoPerpendicularity.toggled.connect(self._perpendicularity_toggled)
        self.rdoInches.toggled.connect(self._radio_toggled)
        self.rdoMM.toggled.connect(self._radio_toggled)
        self.rdoViewISO.toggled.connect(self._radio_toggled)
        self.rdoXMinus.toggled.connect(self._radio_toggled)
        self.rdoYMinus.toggled.connect(self._radio_toggled)
        self.rdoZMinus.toggled.connect(self._radio_toggled)
        self.rdoXPlus.toggled.connect(self._radio_toggled)
        self.rdoYPlus.toggled.connect(self._radio_toggled)
        self.rdoZPlus.toggled.connect(self._radio_toggled)

        self.cboPrimary.currentIndexChanged.connect(self._primary_datum_changed)
        self.cboSecondary.currentIndexChanged.connect(self._secondary_datum_changed)
        self.cboTertiary.currentIndexChanged.connect(self._tertiary_datum_changed)

        self.txtTo.textChanged.connect(self._textbox_text_changed)
        self.txtFrom.textChanged.connect(self._textbox_text_changed)
        self.txtTolerance.textChanged.connect(self._textbox_text_changed)
        self.txtAmount.textChanged.connect(self._textbox_text_changed)

        self.btnCopy.clicked.connect(self._btn_clicked)

    def load_comboboxes(self):
        self.cboPrimary.clear()
        self.cboSecondary.clear()
        self.cboTertiary.clear()
        self.cboPrimary.addItems(self.primary_datum_list)
        self.cboSecondary.addItems(self.secondary_datum_list)
        self.cboTertiary.addItems(self.secondary_datum_list)

    def generate_comment(self):
        comment_text = self.get_dimension_type()
        comment_text += self.get_tolerance()
        comment_text += self.get_datums()

        if self.rdoProfile.isChecked() and self.chkSeptReq.isChecked():
            comment_text += " (Sept. Req)"

        if self.rdoProfile.isChecked() and self.chkFromTo.isChecked():
            comment_text += self.get_from_to()

        if self.rdoProfile.isChecked() and self.chkUnequallyDisposed.isChecked():
            comment_text += self.get_unqually_disposed()

        comment_text += self.get_view()

        self.txtOutput.setText(comment_text)
        pyperclip.copy(comment_text)

    def get_from_to(self) -> str:
        if not self.chkFromTo.isChecked() or not self.txtFrom.text() or not self.txtTo.text():
            return ""
        return f"\r\nFrom {self.txtFrom.text().upper()} <-to-> {self.txtTo.text().upper()} on print"

    def get_unqually_disposed(self) -> str:
        if not self.chkUnequallyDisposed.isChecked() or not self.txtAmount.text():
            return ""
        try:
            numeric_amount = float(self.txtAmount.text())
            formatted_amount = self._get_formatted_numerical_value(numeric_amount)
        except ValueError:
            return ""

        return f"\r\nUnequally disposed, with {formatted_amount} outside the part."

    def get_dimension_type(self):
        if self.rdoProfile.isChecked():
            return "Profile of "
        if self.rdoFlatness.isChecked():
            return "Flatness of "
        if self.rdoPerpendicularity.isChecked():
            return "Perpendicularity of "

    def get_tolerance(self) -> str:
        try:
            tolerance_value = float(self.txtTolerance.text())
        except ValueError:
            tolerance_value = 0
        if self.chkAllAround.isChecked():
            return f"{self._get_formatted_numerical_value(tolerance_value)} all around"
        else:
            return self._get_formatted_numerical_value(tolerance_value)

    def get_datums(self) -> str:
        datum_text: str = ""
        if self.rdoFlatness.isChecked():
            return ""

        if self.rdoPerpendicularity.isChecked():
            return f" to [{self.cboPrimary.currentText()}]"

        if self.cboPrimary.currentIndex() == 0:
            return " to itself"
        else:
            datum_text = f" to [{self.cboPrimary.currentText()}]"

        if self.cboSecondary.currentIndex() > 0:
            datum_text += f"[{self.cboSecondary.currentText()}]"
        if self.cboTertiary.currentIndex() > 0:
            datum_text += f"[{self.cboTertiary.currentText()}]"
        return datum_text

    def get_view(self) -> str:
        if self.rdoViewISO.isChecked():
            return "\r\nLooking in ISO view as the part sits on the CMM"
        if self.rdoXPlus.isChecked():
            return "\r\nLooking from X+ as the part sits on the CMM"
        if self.rdoXMinus.isChecked():
            return "\r\nLooking from X- as the part sits on the CMM"
        if self.rdoYPlus.isChecked():
            return "\r\nLooking from Y+ as the part sits on the CMM"
        if self.rdoYMinus.isChecked():
            return "\r\nLooking from Y- as the part sits on the CMM"
        if self.rdoZPlus.isChecked():
            return "\r\nLooking from Z+ as the part sits on the CMM"
        if self.rdoZMinus.isChecked():
            return "\r\nLooking from Z- as the part sits on the CMM"

    # Private Functions
    def _get_formatted_numerical_value(self, numerical_value: float) -> str:
        if numerical_value <= 1 and self.rdoMM.isChecked():
            return f"{round_to_precision(numerical_value, .0001)}mm"
        return_val = f"{round_to_precision(numerical_value, .0001)}"
        return return_val[1:]


def round_to_precision(x, precision):
    # This correction required due to float errors and aims to avoid cases like:
    # 100.00501 / 0.00001 = 10000500.999999998
    # It has a downside as well - it may lead to vanishing the difference for case like
    # price = 100.5 - (correction - correction/10), precision = 1 => 101 not 100
    # 5 decimals below desired precision looks safe enough to ignore
    correction = 1e-5 if x > 0 else -1e-5
    result = round(x / precision + correction) * precision
    return round(result, find_first_meaningful_decimal(precision))


def find_first_meaningful_decimal(x):
    candidate = 0
    MAX_DECIMAL = 10
    EPSILON = 1 / 10 ** MAX_DECIMAL
    while round(x, candidate) < EPSILON:
        candidate += 1
        if candidate > MAX_DECIMAL:
            raise Exception(f'Number is too small: {x}')
    if int(x * 10 ** (candidate + 1)) == 5:
        candidate += 1
    return candidate


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dude = QtWidgets.QMainWindow()
    ui = CommentBuilderMainWindow()
    ui.setupUi(dude)
    ui.load_comboboxes()
    ui.generate_comment()
    ui.bind_events()
    dude.show()
    sys.exit(app.exec())
