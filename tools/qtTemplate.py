import sys
from PySide2 import QtWidgets, QtUiTools

class EmailWidget(QtWidgets.QWidget):
    def __init__(self):
        super(EmailWidget, self).__init__()
        ui_file = ""
        self.ui = QtUiTools.QUiLoader().load(ui_file, parentWidget=self)

        # 为每个按钮链接指令
        self.ui.sendBtn.clicked.connect(self.send)

    def send(self):
        print("send an email")

def main():
    app = QtWidgets.QApplication(sys.argv)
    win = EmailWidget()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()