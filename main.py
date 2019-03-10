import sys

from PyQt5.QtWidgets import QApplication
from cdds.CDDSMainWindow import CDDS
from cdds.CDDSUI import CDDSUI

def main():
    """Main entry point to the application"""

    # Create the aplication
    app = QApplication(sys.argv)

    # Initialize the window
    window = CDDS()

    # Create the UI, and bind to the window
    ui = CDDSUI()
    ui.setupUi(window)

    # Show the window
    window.show()
    sys.exit(app.exec_())

main()