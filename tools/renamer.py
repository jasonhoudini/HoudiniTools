import sys
sys.path.append("..")
from utils import osUtils
from PySide2 import QtWidgets, QtUiTools

class RenameWidget(QtWidgets.QWidget):
    def __init__(self):
        super(RenameWidget, self).__init__()
        ui_file = "E:/HoudiniTools/ui/Renamer.ui"
        self.ui = QtUiTools.QUiLoader().load(ui_file, parentWidget=self)

        # 为每个按钮链接指令
        self.ui.selectBtn.clicked.connect(self.selectDir)
        self.ui.renameBtn.clicked.connect(self.rename)

    def selectDir(self):
        assetDir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select dir", "E:/test")
        self.ui.dirLineEdit.setText(assetDir)

    def rename(self):
        if self.ui.prependRadBtn.isChecked():
            mode = "prepend"
        elif self.ui.replaceRadBtn.isChecked():
            mode = "replace"

        osUtils.rename(self.ui.dirLineEdit.text(),self.ui.textLineEdit.text(), mode, self.ui.replaceLineEdit.text())
        print("sad")

def main():
    app = QtWidgets.QApplication(sys.argv)
    win = RenameWidget()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()