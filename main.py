"""Main entry point to the application"""

import sys

from PyQt5.QtWidgets import QApplication
from cdds.cdds_main_window import CDDSMainWindow
from cdds.cdds_ui import CDDSUi

if __name__ == "__main__":
    # Create the aplication
    APP = QApplication(sys.argv)

    # Initialize the window
    WINDOW = CDDSMainWindow()

    # Create the UI, and bind to the window
    UI = CDDSUi()
    UI.setupUi(WINDOW)

    # Show the window
    WINDOW.show()
    sys.exit(APP.exec_())
