"""Main entry point to the application"""

import sys

from PyQt5.QtWidgets import QApplication
from cdds.CDDSMainWindow import CDDS
from cdds.CDDSUI import CDDSUI

if __name__ == "__main__":
    # Create the aplication
    APP = QApplication(sys.argv)

    # Initialize the window
    WINDOW = CDDS()

    # Create the UI, and bind to the window
    UI = CDDSUI()
    UI.setupUi(WINDOW)

    # Show the window
    WINDOW.show()
    sys.exit(APP.exec_())
