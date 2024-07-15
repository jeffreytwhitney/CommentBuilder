from PyQt6 import QtWidgets

from CommentBuilderMainWindow_GUI import Ui_CommentBuilderMainWindow_GUI


class CommentBuilderMainWindow(QtWidgets.QMainWindow, Ui_CommentBuilderMainWindow_GUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


    def bind_events(self):
        self.chkAllAround.stateChanged.connect(self._checkbox_stateChanged)
        self.chkSeptReq.stateChanged.connect(self._checkbox_stateChanged)

        self.chkUnequallyDisposed.stateChanged.connect(self._chkUnequallyDisposed_stateChanged)
        self.chkFromTo.stateChanged.connect(self._chkFromTo_stateChanged)

    #Events
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


    #Public Functions
    def generate_comment(self):
        comment_text: str = ""
        comment_text = self.get_dimension_type()
        comment_text += self.get_tolerance()
        self.txtOutput.setText(comment_text)

    def get_dimension_type(self):
        if self.rdoProfile.isChecked():
            return "Profile Of "
        if self.rdoFlatness.isChecked():
            return "Flatness Of "
        if self.rdoPerpendicularity.isChecked():
            return "Perpendicularity Of "

    def get_tolerance(self) -> str:
        try:
            tolerance_value = float(self.txtTolerance.text())
        except ValueError:
            tolerance_value = 0
        if self.chkAllAround.isChecked():
            return f"{self._get_formatted_numerical_value(tolerance_value)} all around"
        else:
            return self._get_formatted_numerical_value(tolerance_value)


    #Private Functions
    def _get_formatted_numerical_value(self, numerical_value: float) -> str:
        if numerical_value <= 1 and self.rdoMM.isChecked():
            return f"0{round_to_precision(numerical_value, .0001)}"
        else:
            return f"{round_to_precision(numerical_value, .0001)}"


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
    ui.generate_comment()
    ui.bind_events()
    dude.show()
    sys.exit(app.exec())
