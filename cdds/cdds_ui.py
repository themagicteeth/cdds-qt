from cdds.UI import Ui_MainWindow


class CDDSUi(Ui_MainWindow):
    """Create the UI from the generated UI file"""

    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)


#         def openFile(self):
#   fileName = QFileDialog.getOpenFileName()
#   ui.browsePushButton.clicked.connect(openFile)
