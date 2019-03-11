# -*- coding: utf-8 -*-

"""Main entry point to the application"""

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAbstractItemView

from ui.cdds_ui import Ui_MainWindow
from util.manifest_utils import generate_uuid


def set_uuid():
    """Sets the UUID input field to a randomly genrated UUID"""
    UI.uuidInput.setPlainText(generate_uuid())


def set_sku():
    """Sets the SKU input field to a randomly generated SKU"""
    from util.manifest_utils import generate_sku
    UI.skuSpinBox.setValue(generate_sku())


def set_archive(file_name):
    """Takes a selected archive and sets the archive and content name input fields"""
    from util.manifest_utils import generate_dim_name
    content_name = generate_dim_name(file_name)
    UI.archiveInput.setPlainText(file_name)
    set_tree(file_name)
    #model = set_file_model()
    # https://stackoverflow.com/questions/48121711/drag-and-drop-within-pyqt5-treeview
    # https://github.com/baoboa/pyqt5/blob/master/examples/itemviews/dirview.py
    # UI.packageFilesTreeView.setModel(model)
    # UI.packageFilesTreeView.setRootIndex(file_name)
    UI.packageNameInput.setPlainText(content_name)


def set_tree(file_name):
    from PyQt5.QtWidgets import QFileSystemModel
    from PyQt5.QtCore import QDir

    model = QFileSystemModel()
    model.setRootPath('')
    model.setReadOnly(False)

    rootIndex = model.index(QDir.cleanPath(file_name))

    UI.packageFilesTreeView.setModel(model)
    UI.packageFilesTreeView.setRootIndex(rootIndex)


def browse():
    """Opens a file dialogue and process the selected file"""
    file_name = QFileDialog.getOpenFileName()[0]
    if file_name:
        set_archive(file_name)
        #model = set_file_model(file_name)
        # UI.packageFilesTreeView.setModel(model)


# def set_file_model():
 #   """Create a file system view"""
   # from PyQt5.QtWidgets import QFileSystemModel

    #model = QFileSystemModel()
    # model.setRootPath('')
    # model.setReadOnly(False)

    # return model


if __name__ == "__main__":
    # Create the aplication
    APP = QApplication(sys.argv)

    # Initialize the window
    WINDOW = QMainWindow()

    # Create the UI, and bind to the window
    UI = Ui_MainWindow()
    UI.setupUi(WINDOW)

    UI.uuidInput.setPlainText(generate_uuid())
    UI.generateUuidButton.clicked.connect(set_uuid)
    UI.randomSkuButton.clicked.connect(set_sku)
    UI.browsePushButton.clicked.connect(browse)

    #MODEL = set_file_model()
    # UI.packageFilesTreeView.setModel(MODEL)

    # Show the window
    WINDOW.show()
    sys.exit(APP.exec_())
