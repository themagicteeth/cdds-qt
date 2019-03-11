# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cdds.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 625)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 781, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.createManifestTab = QtWidgets.QWidget()
        self.createManifestTab.setObjectName("createManifestTab")
        self.packageNameLabel = QtWidgets.QLabel(self.createManifestTab)
        self.packageNameLabel.setGeometry(QtCore.QRect(20, 90, 101, 16))
        self.packageNameLabel.setObjectName("packageNameLabel")
        self.vendorComboBox = QtWidgets.QComboBox(self.createManifestTab)
        self.vendorComboBox.setGeometry(QtCore.QRect(310, 110, 121, 31))
        self.vendorComboBox.setObjectName("vendorComboBox")
        self.vendorComboBox.addItem("")
        self.vendorComboBox.addItem("")
        self.vendorComboBox.addItem("")
        self.packageNameInput = QtWidgets.QPlainTextEdit(self.createManifestTab)
        self.packageNameInput.setGeometry(QtCore.QRect(20, 110, 281, 30))
        self.packageNameInput.setObjectName("packageNameInput")
        self.skuSpinBox = QtWidgets.QSpinBox(self.createManifestTab)
        self.skuSpinBox.setGeometry(QtCore.QRect(440, 110, 141, 30))
        self.skuSpinBox.setMinimum(1)
        self.skuSpinBox.setMaximum(9999999)
        self.skuSpinBox.setObjectName("skuSpinBox")
        self.browsePushButton = QtWidgets.QPushButton(self.createManifestTab)
        self.browsePushButton.setGeometry(QtCore.QRect(310, 40, 80, 31))
        self.browsePushButton.setObjectName("browsePushButton")
        self.archiveInput = QtWidgets.QPlainTextEdit(self.createManifestTab)
        self.archiveInput.setGeometry(QtCore.QRect(20, 40, 281, 30))
        self.archiveInput.setObjectName("archiveInput")
        self.vendorLabel = QtWidgets.QLabel(self.createManifestTab)
        self.vendorLabel.setGeometry(QtCore.QRect(310, 90, 101, 16))
        self.vendorLabel.setObjectName("vendorLabel")
        self.skuLabel = QtWidgets.QLabel(self.createManifestTab)
        self.skuLabel.setGeometry(QtCore.QRect(440, 90, 101, 16))
        self.skuLabel.setObjectName("skuLabel")
        self.archiveLabel = QtWidgets.QLabel(self.createManifestTab)
        self.archiveLabel.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.archiveLabel.setObjectName("archiveLabel")
        self.packageFilesTreeView = QtWidgets.QTreeView(self.createManifestTab)
        self.packageFilesTreeView.setGeometry(QtCore.QRect(20, 180, 371, 341))
        self.packageFilesTreeView.setAcceptDrops(True)
        self.packageFilesTreeView.setDragEnabled(True)
        self.packageFilesTreeView.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.packageFilesTreeView.setObjectName("packageFilesTreeView")
        self.packageFilesLabel = QtWidgets.QLabel(self.createManifestTab)
        self.packageFilesLabel.setGeometry(QtCore.QRect(20, 160, 101, 16))
        self.packageFilesLabel.setObjectName("packageFilesLabel")
        self.fileContentsView = QtWidgets.QGraphicsView(self.createManifestTab)
        self.fileContentsView.setGeometry(QtCore.QRect(400, 180, 371, 291))
        self.fileContentsView.setObjectName("fileContentsView")
        self.fileContentsLabel = QtWidgets.QLabel(self.createManifestTab)
        self.fileContentsLabel.setGeometry(QtCore.QRect(400, 160, 101, 16))
        self.fileContentsLabel.setObjectName("fileContentsLabel")
        self.uuidInput = QtWidgets.QPlainTextEdit(self.createManifestTab)
        self.uuidInput.setGeometry(QtCore.QRect(400, 40, 281, 30))
        self.uuidInput.setReadOnly(True)
        self.uuidInput.setObjectName("uuidInput")
        self.uuidLabel = QtWidgets.QLabel(self.createManifestTab)
        self.uuidLabel.setGeometry(QtCore.QRect(400, 20, 101, 16))
        self.uuidLabel.setObjectName("uuidLabel")
        self.generateUuidButton = QtWidgets.QPushButton(self.createManifestTab)
        self.generateUuidButton.setGeometry(QtCore.QRect(690, 40, 81, 31))
        self.generateUuidButton.setObjectName("generateUuidButton")
        self.randomSkuButton = QtWidgets.QPushButton(self.createManifestTab)
        self.randomSkuButton.setGeometry(QtCore.QRect(590, 110, 91, 31))
        self.randomSkuButton.setObjectName("randomSkuButton")
        self.pushButton = QtWidgets.QPushButton(self.createManifestTab)
        self.pushButton.setGeometry(QtCore.QRect(659, 490, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.createManifestTab, "")
        self.productDetailsTab = QtWidgets.QWidget()
        self.productDetailsTab.setEnabled(True)
        self.productDetailsTab.setObjectName("productDetailsTab")
        self.productImageView = QtWidgets.QGraphicsView(self.productDetailsTab)
        self.productImageView.setGeometry(QtCore.QRect(20, 20, 251, 321))
        self.productImageView.setObjectName("productImageView")
        self.authorsInput = QtWidgets.QPlainTextEdit(self.productDetailsTab)
        self.authorsInput.setGeometry(QtCore.QRect(290, 40, 471, 31))
        self.authorsInput.setObjectName("authorsInput")
        self.authorsLabel = QtWidgets.QLabel(self.productDetailsTab)
        self.authorsLabel.setGeometry(QtCore.QRect(290, 20, 201, 16))
        self.authorsLabel.setObjectName("authorsLabel")
        self.audienceComboBox = QtWidgets.QComboBox(self.productDetailsTab)
        self.audienceComboBox.setGeometry(QtCore.QRect(290, 110, 471, 31))
        self.audienceComboBox.setObjectName("audienceComboBox")
        self.audienceComboBox.addItem("")
        self.audienceComboBox.addItem("")
        self.audienceComboBox.addItem("")
        self.audienceLabel = QtWidgets.QLabel(self.productDetailsTab)
        self.audienceLabel.setGeometry(QtCore.QRect(290, 90, 61, 16))
        self.audienceLabel.setObjectName("audienceLabel")
        self.selectImageButton = QtWidgets.QPushButton(self.productDetailsTab)
        self.selectImageButton.setGeometry(QtCore.QRect(160, 400, 111, 31))
        self.selectImageButton.setObjectName("selectImageButton")
        self.defaultRadioButton = QtWidgets.QRadioButton(self.productDetailsTab)
        self.defaultRadioButton.setGeometry(QtCore.QRect(20, 420, 100, 21))
        self.defaultRadioButton.setChecked(True)
        self.defaultRadioButton.setObjectName("defaultRadioButton")
        self.customRadioButton = QtWidgets.QRadioButton(self.productDetailsTab)
        self.customRadioButton.setGeometry(QtCore.QRect(20, 440, 100, 21))
        self.customRadioButton.setObjectName("customRadioButton")
        self.imageSizeLabel = QtWidgets.QLabel(self.productDetailsTab)
        self.imageSizeLabel.setGeometry(QtCore.QRect(20, 400, 81, 16))
        self.imageSizeLabel.setObjectName("imageSizeLabel")
        self.widthSpinBox = QtWidgets.QSpinBox(self.productDetailsTab)
        self.widthSpinBox.setEnabled(False)
        self.widthSpinBox.setGeometry(QtCore.QRect(20, 350, 91, 31))
        self.widthSpinBox.setMaximum(500)
        self.widthSpinBox.setProperty("value", 119)
        self.widthSpinBox.setObjectName("widthSpinBox")
        self.heightSpinBox = QtWidgets.QSpinBox(self.productDetailsTab)
        self.heightSpinBox.setEnabled(False)
        self.heightSpinBox.setGeometry(QtCore.QRect(180, 350, 91, 31))
        self.heightSpinBox.setMaximum(500)
        self.heightSpinBox.setProperty("value", 148)
        self.heightSpinBox.setObjectName("heightSpinBox")
        self.descriptionInput = QtWidgets.QPlainTextEdit(self.productDetailsTab)
        self.descriptionInput.setGeometry(QtCore.QRect(290, 190, 471, 151))
        self.descriptionInput.setObjectName("descriptionInput")
        self.descriptionLabel = QtWidgets.QLabel(self.productDetailsTab)
        self.descriptionLabel.setGeometry(QtCore.QRect(290, 170, 81, 16))
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.nextButton = QtWidgets.QPushButton(self.productDetailsTab)
        self.nextButton.setGeometry(QtCore.QRect(660, 490, 111, 31))
        self.nextButton.setObjectName("nextButton")
        self.tabWidget.addTab(self.productDetailsTab, "")
        self.smartContentTab = QtWidgets.QWidget()
        self.smartContentTab.setObjectName("smartContentTab")
        self.fileSelectListView = QtWidgets.QListView(self.smartContentTab)
        self.fileSelectListView.setGeometry(QtCore.QRect(10, 40, 256, 481))
        self.fileSelectListView.setObjectName("fileSelectListView")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.smartContentTab)
        self.plainTextEdit.setGeometry(QtCore.QRect(280, 40, 311, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.smartContentTab)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 40, 80, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.archiveLabel_2 = QtWidgets.QLabel(self.smartContentTab)
        self.archiveLabel_2.setGeometry(QtCore.QRect(280, 20, 101, 16))
        self.archiveLabel_2.setObjectName("archiveLabel_2")
        self.archiveLabel_3 = QtWidgets.QLabel(self.smartContentTab)
        self.archiveLabel_3.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.archiveLabel_3.setObjectName("archiveLabel_3")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.smartContentTab)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(280, 110, 311, 111))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.archiveLabel_4 = QtWidgets.QLabel(self.smartContentTab)
        self.archiveLabel_4.setGeometry(QtCore.QRect(280, 90, 101, 16))
        self.archiveLabel_4.setObjectName("archiveLabel_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.smartContentTab)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 110, 80, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.smartContentTab)
        self.pushButton_4.setGeometry(QtCore.QRect(600, 150, 80, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.smartContentTab)
        self.pushButton_5.setGeometry(QtCore.QRect(600, 190, 80, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.smartContentTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.packageNameLabel.setText(_translate("MainWindow", "Package Name"))
        self.vendorComboBox.setItemText(0, _translate("MainWindow", "Daz3D"))
        self.vendorComboBox.setItemText(1, _translate("MainWindow", "Renderosity"))
        self.vendorComboBox.setItemText(2, _translate("MainWindow", "Renderotica"))
        self.browsePushButton.setToolTip(_translate("MainWindow", "Browse for a zip archive"))
        self.browsePushButton.setText(_translate("MainWindow", "Browse..."))
        self.archiveInput.setToolTip(_translate("MainWindow", "Enter the path to the zip archive, or browse to select one"))
        self.vendorLabel.setText(_translate("MainWindow", "Vendor"))
        self.skuLabel.setText(_translate("MainWindow", "SKU"))
        self.archiveLabel.setText(_translate("MainWindow", "Archive"))
        self.packageFilesLabel.setText(_translate("MainWindow", "Package Files"))
        self.fileContentsLabel.setText(_translate("MainWindow", "File Contents"))
        self.uuidLabel.setText(_translate("MainWindow", "Global UUID"))
        self.generateUuidButton.setText(_translate("MainWindow", "Generate"))
        self.randomSkuButton.setText(_translate("MainWindow", "Random SKU"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.createManifestTab), _translate("MainWindow", "Create Manifest"))
        self.authorsLabel.setText(_translate("MainWindow", "Authors (seperated by comma)"))
        self.audienceComboBox.setItemText(0, _translate("MainWindow", "Children"))
        self.audienceComboBox.setItemText(1, _translate("MainWindow", "Teens"))
        self.audienceComboBox.setItemText(2, _translate("MainWindow", "Adults"))
        self.audienceLabel.setText(_translate("MainWindow", "Audience"))
        self.selectImageButton.setText(_translate("MainWindow", "Select Image"))
        self.defaultRadioButton.setText(_translate("MainWindow", "Default"))
        self.customRadioButton.setText(_translate("MainWindow", "Custom"))
        self.imageSizeLabel.setText(_translate("MainWindow", "Image Size"))
        self.descriptionLabel.setText(_translate("MainWindow", "Description"))
        self.nextButton.setText(_translate("MainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.productDetailsTab), _translate("MainWindow", "Product Details"))
        self.pushButton_2.setText(_translate("MainWindow", "Select"))
        self.archiveLabel_2.setText(_translate("MainWindow", "Content Type"))
        self.archiveLabel_3.setText(_translate("MainWindow", "Files"))
        self.archiveLabel_4.setText(_translate("MainWindow", "Category"))
        self.pushButton_3.setText(_translate("MainWindow", "Add"))
        self.pushButton_4.setText(_translate("MainWindow", "Edit"))
        self.pushButton_5.setText(_translate("MainWindow", "Remove"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.smartContentTab), _translate("MainWindow", "Smart Content Metadata"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


