import sys
from PySide2 import QtWidgets, QtUiTools
import yagmail


class EmailWidget(QtWidgets.QWidget):
    def __init__(self):
        super(EmailWidget, self).__init__()
        ui_file = "E:/HoudiniTools/ui/Emailer.ui"
        self.ui = QtUiTools.QUiLoader().load(ui_file, parentWidget=self)

        # 为每个按钮链接指令
        self.ui.sendBtn.clicked.connect(self.send)

    def send(self):
        yag = yagmail.SMTP(user="zcy980401@gmail.com", password="zcy19980401.")
        to = self.ui.toLineEdit.text()
        subject = self.ui.subjectLineEdit.text()
        body = self.ui.bodyTextEdit.toPlainText()
        yag.send(to, subject, body)


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = EmailWidget()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()