# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 743)
        self.horizontalLayout = QtWidgets.QHBoxLayout(MainWindow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CreateZone = QtWidgets.QVBoxLayout()
        self.CreateZone.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.CreateZone.setContentsMargins(0, 0, -1, -1)
        self.CreateZone.setSpacing(6)
        self.CreateZone.setObjectName("CreateZone")
        self.SaveLoad = QtWidgets.QHBoxLayout()
        self.SaveLoad.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.SaveLoad.setContentsMargins(-1, -1, -1, 0)
        self.SaveLoad.setSpacing(16)
        self.SaveLoad.setObjectName("SaveLoad")
        self.ButtSaveAprox = QtWidgets.QPushButton(MainWindow)
        self.ButtSaveAprox.setObjectName("ButtSaveAprox")
        self.SaveLoad.addWidget(self.ButtSaveAprox)
        self.ButtLoadAprox = QtWidgets.QPushButton(MainWindow)
        self.ButtLoadAprox.setEnabled(True)
        self.ButtLoadAprox.setMaximumSize(QtCore.QSize(16777215, 23))
        self.ButtLoadAprox.setAutoDefault(False)
        self.ButtLoadAprox.setDefault(False)
        self.ButtLoadAprox.setObjectName("ButtLoadAprox")
        self.SaveLoad.addWidget(self.ButtLoadAprox)
        self.CreateZone.addLayout(self.SaveLoad)
        self.Espec = QtWidgets.QLabel(MainWindow)
        self.Espec.setEnabled(True)
        self.Espec.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Espec.setAutoFillBackground(False)
        self.Espec.setFrameShape(QtWidgets.QFrame.Box)
        self.Espec.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Espec.setTextFormat(QtCore.Qt.AutoText)
        self.Espec.setScaledContents(False)
        self.Espec.setObjectName("Espec")
        self.CreateZone.addWidget(self.Espec)
        self.FiltersOptions = QtWidgets.QHBoxLayout()
        self.FiltersOptions.setObjectName("FiltersOptions")
        self.CBAprox = QtWidgets.QComboBox(MainWindow)
        self.CBAprox.setObjectName("CBAprox")
        self.CBAprox.addItem("")
        self.CBAprox.addItem("")
        self.CBAprox.addItem("")
        self.CBAprox.addItem("")
        self.CBAprox.addItem("")
        self.CBAprox.addItem("")
        self.CBAprox.addItem("")
        self.CBAprox.addItem("")
        self.FiltersOptions.addWidget(self.CBAprox)
        self.CBFilters = QtWidgets.QComboBox(MainWindow)
        self.CBFilters.setObjectName("CBFilters")
        self.CBFilters.addItem("")
        self.CBFilters.addItem("")
        self.CBFilters.addItem("")
        self.CBFilters.addItem("")
        self.CBFilters.addItem("")
        self.CBFilters.addItem("")
        self.FiltersOptions.addWidget(self.CBFilters)
        self.CreateZone.addLayout(self.FiltersOptions)
        self.Orden = QtWidgets.QHBoxLayout()
        self.Orden.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.Orden.setObjectName("Orden")
        self.LOrden = QtWidgets.QLabel(MainWindow)
        self.LOrden.setObjectName("LOrden")
        self.Orden.addWidget(self.LOrden)
        self.CheckMinOrden = QtWidgets.QCheckBox(MainWindow)
        self.CheckMinOrden.setObjectName("CheckMinOrden")
        self.Orden.addWidget(self.CheckMinOrden)
        self.NumOrden = QtWidgets.QSpinBox(MainWindow)
        self.NumOrden.setObjectName("NumOrden")
        self.Orden.addWidget(self.NumOrden)
        self.CreateZone.addLayout(self.Orden)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(MainWindow)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.CheckQmax = QtWidgets.QCheckBox(MainWindow)
        self.CheckQmax.setObjectName("CheckQmax")
        self.horizontalLayout_6.addWidget(self.CheckQmax)
        self.SpinBoxQ = QtWidgets.QDoubleSpinBox(MainWindow)
        self.SpinBoxQ.setObjectName("SpinBoxQ")
        self.horizontalLayout_6.addWidget(self.SpinBoxQ)
        self.label_11 = QtWidgets.QLabel(MainWindow)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.CheckDesnorm = QtWidgets.QCheckBox(MainWindow)
        self.CheckDesnorm.setObjectName("CheckDesnorm")
        self.horizontalLayout_6.addWidget(self.CheckDesnorm)
        self.SpinBoxDesnorm = QtWidgets.QSpinBox(MainWindow)
        self.SpinBoxDesnorm.setMaximum(100)
        self.SpinBoxDesnorm.setObjectName("SpinBoxDesnorm")
        self.horizontalLayout_6.addWidget(self.SpinBoxDesnorm)
        self.CreateZone.addLayout(self.horizontalLayout_6)
        self.GridSpecs = QtWidgets.QGridLayout()
        self.GridSpecs.setHorizontalSpacing(6)
        self.GridSpecs.setVerticalSpacing(16)
        self.GridSpecs.setObjectName("GridSpecs")
        self.label_Ap = QtWidgets.QLabel(MainWindow)
        self.label_Ap.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Ap.setObjectName("label_Ap")
        self.GridSpecs.addWidget(self.label_Ap, 2, 2, 1, 1)
        self.SpinBoxFpplus = QtWidgets.QDoubleSpinBox(MainWindow)
        self.SpinBoxFpplus.setMaximum(999999.99)
        self.SpinBoxFpplus.setObjectName("SpinBoxFpplus")
        self.GridSpecs.addWidget(self.SpinBoxFpplus, 1, 1, 1, 1)
        self.SpinBoxGain = QtWidgets.QDoubleSpinBox(MainWindow)
        self.SpinBoxGain.setMaximum(999.99)
        self.SpinBoxGain.setObjectName("SpinBoxGain")
        self.GridSpecs.addWidget(self.SpinBoxGain, 1, 3, 1, 1)
        self.label_fpm = QtWidgets.QLabel(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_fpm.setFont(font)
        self.label_fpm.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fpm.setObjectName("label_fpm")
        self.GridSpecs.addWidget(self.label_fpm, 2, 0, 1, 1)
        self.SpinBoxTol = QtWidgets.QDoubleSpinBox(MainWindow)
        self.SpinBoxTol.setObjectName("SpinBoxTol")
        self.GridSpecs.addWidget(self.SpinBoxTol, 5, 3, 1, 1)
        self.label_fap = QtWidgets.QLabel(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_fap.setFont(font)
        self.label_fap.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fap.setObjectName("label_fap")
        self.GridSpecs.addWidget(self.label_fap, 3, 0, 1, 1)
        self.label_fam = QtWidgets.QLabel(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_fam.setFont(font)
        self.label_fam.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fam.setObjectName("label_fam")
        self.GridSpecs.addWidget(self.label_fam, 5, 0, 1, 1)
        self.CBAmpUnit = QtWidgets.QComboBox(MainWindow)
        self.CBAmpUnit.setObjectName("CBAmpUnit")
        self.CBAmpUnit.addItem("")
        self.CBAmpUnit.addItem("")
        self.GridSpecs.addWidget(self.CBAmpUnit, 0, 3, 1, 1)
        self.SpinBoxFaminus = QtWidgets.QDoubleSpinBox(MainWindow)
        self.SpinBoxFaminus.setMaximum(999999.99)
        self.SpinBoxFaminus.setObjectName("SpinBoxFaminus")
        self.GridSpecs.addWidget(self.SpinBoxFaminus, 5, 1, 1, 1)
        self.label_fpp = QtWidgets.QLabel(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_fpp.setFont(font)
        self.label_fpp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fpp.setObjectName("label_fpp")
        self.GridSpecs.addWidget(self.label_fpp, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setObjectName("label")
        self.GridSpecs.addWidget(self.label, 0, 0, 1, 1)
        self.SpinBoxAp = QtWidgets.QDoubleSpinBox(MainWindow)
        self.SpinBoxAp.setMaximum(999.99)
        self.SpinBoxAp.setObjectName("SpinBoxAp")
        self.GridSpecs.addWidget(self.SpinBoxAp, 2, 3, 1, 1)
        self.SpinBoxFpminus = QtWidgets.QDoubleSpinBox(MainWindow)
        self.SpinBoxFpminus.setMaximum(999999.99)
        self.SpinBoxFpminus.setObjectName("SpinBoxFpminus")
        self.GridSpecs.addWidget(self.SpinBoxFpminus, 2, 1, 1, 1)
        self.SpinBoxFaplus = QtWidgets.QDoubleSpinBox(MainWindow)
        self.SpinBoxFaplus.setMaximum(999999.99)
        self.SpinBoxFaplus.setObjectName("SpinBoxFaplus")
        self.GridSpecs.addWidget(self.SpinBoxFaplus, 3, 1, 1, 1)
        self.SpinBoxAa = QtWidgets.QDoubleSpinBox(MainWindow)
        self.SpinBoxAa.setMaximum(999.99)
        self.SpinBoxAa.setObjectName("SpinBoxAa")
        self.GridSpecs.addWidget(self.SpinBoxAa, 3, 3, 1, 1)
        self.label_Aa = QtWidgets.QLabel(MainWindow)
        self.label_Aa.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Aa.setObjectName("label_Aa")
        self.GridSpecs.addWidget(self.label_Aa, 3, 2, 1, 1)
        self.CBFreqUnit = QtWidgets.QComboBox(MainWindow)
        self.CBFreqUnit.setObjectName("CBFreqUnit")
        self.CBFreqUnit.addItem("")
        self.CBFreqUnit.addItem("")
        self.CBFreqUnit.addItem("")
        self.GridSpecs.addWidget(self.CBFreqUnit, 0, 1, 1, 1)
        self.label_tol = QtWidgets.QLabel(MainWindow)
        self.label_tol.setEnabled(True)
        self.label_tol.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_tol.setObjectName("label_tol")
        self.GridSpecs.addWidget(self.label_tol, 5, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setObjectName("label_2")
        self.GridSpecs.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_Go = QtWidgets.QLabel(MainWindow)
        self.label_Go.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Go.setObjectName("label_Go")
        self.GridSpecs.addWidget(self.label_Go, 1, 2, 1, 1)
        self.label_ft = QtWidgets.QLabel(MainWindow)
        self.label_ft.setObjectName("label_ft")
        self.GridSpecs.addWidget(self.label_ft, 6, 0, 1, 1)
        self.SpinBoxFt = QtWidgets.QDoubleSpinBox(MainWindow)
        self.SpinBoxFt.setObjectName("SpinBoxFt")
        self.SpinBoxFt.setMaximum(999999.99)
        self.GridSpecs.addWidget(self.SpinBoxFt, 6, 1, 1, 1)
        self.label_retgroup = QtWidgets.QLabel(MainWindow)
        self.label_retgroup.setObjectName("label_retgroup")
        self.GridSpecs.addWidget(self.label_retgroup, 6, 2, 1, 1)
        self.SpinBoxRetGroup = QtWidgets.QDoubleSpinBox(MainWindow)
        self.SpinBoxRetGroup.setObjectName("SpinBoxRetGroup")
        self.GridSpecs.addWidget(self.SpinBoxRetGroup, 6, 3, 1, 1)
        self.CreateZone.addLayout(self.GridSpecs)
        self.ButtonCreateFilter = QtWidgets.QPushButton(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonCreateFilter.setFont(font)
        self.ButtonCreateFilter.setObjectName("ButtonCreateFilter")
        self.CreateZone.addWidget(self.ButtonCreateFilter)
        self.Filter_Image = QtWidgets.QLabel(MainWindow)
        self.Filter_Image.setMinimumSize(QtCore.QSize(95, 95))
        self.Filter_Image.setText("")
        self.Filter_Image.setObjectName("Filter_Image")
        self.CreateZone.addWidget(self.Filter_Image)
        self.horizontalLayout.addLayout(self.CreateZone)
        self.GraphZone = QtWidgets.QVBoxLayout()
        self.GraphZone.setSpacing(6)
        self.GraphZone.setObjectName("GraphZone")
        self.GraphsWidget = QtWidgets.QTabWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GraphsWidget.sizePolicy().hasHeightForWidth())
        self.GraphsWidget.setSizePolicy(sizePolicy)
        self.GraphsWidget.setMinimumSize(QtCore.QSize(780, 390))
        self.GraphsWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.GraphsWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.GraphsWidget.setTabBarAutoHide(False)
        self.GraphsWidget.setObjectName("GraphsWidget")
        self.MagTab = QtWidgets.QWidget()
        self.MagTab.setObjectName("MagTab")
        self.GraphsWidget.addTab(self.MagTab, "")
        self.AtenTab = QtWidgets.QWidget()
        self.AtenTab.setObjectName("AtenTab")
        self.GraphsWidget.addTab(self.AtenTab, "")
        self.FaseTab = QtWidgets.QWidget()
        self.FaseTab.setObjectName("FaseTab")
        self.GraphsWidget.addTab(self.FaseTab, "")
        self.RetGrupTab = QtWidgets.QWidget()
        self.RetGrupTab.setObjectName("RetGrupTab")
        self.GraphsWidget.addTab(self.RetGrupTab, "")
        self.PazTab = QtWidgets.QWidget()
        self.PazTab.setObjectName("PazTab")
        self.GraphsWidget.addTab(self.PazTab, "")
        self.RespImpTab = QtWidgets.QWidget()
        self.RespImpTab.setObjectName("RespImpTab")
        self.GraphsWidget.addTab(self.RespImpTab, "")
        self.RespEscTab = QtWidgets.QWidget()
        self.RespEscTab.setObjectName("RespEscTab")
        self.GraphsWidget.addTab(self.RespEscTab, "")
        self.GraphZone.addWidget(self.GraphsWidget)
        self.groupBox = QtWidgets.QGroupBox(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 1221212))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.FilterList = QtWidgets.QListWidget(self.groupBox)
        self.FilterList.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FilterList.sizePolicy().hasHeightForWidth())
        self.FilterList.setSizePolicy(sizePolicy)
        self.FilterList.setResizeMode(QtWidgets.QListView.Adjust)
        self.FilterList.setObjectName("FilterList")
        self.verticalLayout.addWidget(self.FilterList)
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.GraphZone.addWidget(self.groupBox)
        self.horizontalLayout.addLayout(self.GraphZone)

        self.retranslateUi(MainWindow)
        self.GraphsWidget.setCurrentIndex(6)
        self.CheckMinOrden.clicked['bool'].connect(self.NumOrden.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Filter Tool G4"))
        self.ButtSaveAprox.setText(_translate("MainWindow", "Save"))
        self.ButtLoadAprox.setText(_translate("MainWindow", "Load Aprox"))
        self.Espec.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Especificaciones</span></p></body></html>"))
        self.CBAprox.setItemText(0, _translate("MainWindow", "Aproximación"))
        self.CBAprox.setItemText(1, _translate("MainWindow", "Butterworth"))
        self.CBAprox.setItemText(2, _translate("MainWindow", "Chebyshev 1"))
        self.CBAprox.setItemText(3, _translate("MainWindow", "Chebyshev 2"))
        self.CBAprox.setItemText(4, _translate("MainWindow", "Bessel"))
        self.CBAprox.setItemText(5, _translate("MainWindow", "Legendre"))
        self.CBAprox.setItemText(6, _translate("MainWindow", "Gauss"))
        self.CBAprox.setItemText(7, _translate("MainWindow", "Cauer"))
        self.CBFilters.setItemText(0, _translate("MainWindow", "Tipo de Filtro"))
        self.CBFilters.setItemText(1, _translate("MainWindow", "LP"))
        self.CBFilters.setItemText(2, _translate("MainWindow", "HP"))
        self.CBFilters.setItemText(3, _translate("MainWindow", "BP"))
        self.CBFilters.setItemText(4, _translate("MainWindow", "BR"))
        self.CBFilters.setItemText(5, _translate("MainWindow", "Group Delay"))
        self.LOrden.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Orden:</span></p></body></html>"))
        self.CheckMinOrden.setText(_translate("MainWindow", "Mínimo"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Q</span><span style=\" font-size:10pt; font-weight:600; vertical-align:sub;\">MAX:</span></p></body></html>"))
        self.CheckQmax.setText(_translate("MainWindow", "Auto"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Desnorm:</span></p></body></html>"))
        self.CheckDesnorm.setText(_translate("MainWindow", "Auto"))
        self.label_Ap.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">A</span><span style=\" font-size:10pt; font-weight:600; vertical-align:sub;\">p</span></p></body></html>"))
        self.label_fpm.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">fp</span><span style=\" font-size:10pt; font-weight:600; vertical-align:super;\">-</span></p></body></html>"))
        self.label_fap.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">fa</span><span style=\" font-size:10pt; font-weight:600; vertical-align:super;\">+</span></p></body></html>"))
        self.label_fam.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">fa</span><span style=\" font-size:10pt; font-weight:600; vertical-align:super;\">-</span></p></body></html>"))
        self.CBAmpUnit.setItemText(0, _translate("MainWindow", "dB"))
        self.CBAmpUnit.setItemText(1, _translate("MainWindow", "unit"))
        self.label_fpp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">fp</span><span style=\" font-size:10pt; font-weight:600; vertical-align:super;\">+</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Frecuencia en"))
        self.label_Aa.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">A</span><span style=\" font-size:10pt; font-weight:600; vertical-align:sub;\">a</span></p></body></html>"))
        self.CBFreqUnit.setItemText(0, _translate("MainWindow", "Hz"))
        self.CBFreqUnit.setItemText(1, _translate("MainWindow", "kHz"))
        self.CBFreqUnit.setItemText(2, _translate("MainWindow", "MHz"))
        self.label_tol.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Tol</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Amplitud en"))
        self.label_Go.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Gain</span></p></body></html>"))
        self.label_ft.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Ft</span></p></body></html>"))
        self.label_retgroup.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Ret. Group</span></p></body></html>"))
        self.ButtonCreateFilter.setText(_translate("MainWindow", "Crear Filtro"))
        self.GraphsWidget.setTabText(self.GraphsWidget.indexOf(self.MagTab), _translate("MainWindow", "Magnitud"))
        self.GraphsWidget.setTabText(self.GraphsWidget.indexOf(self.AtenTab), _translate("MainWindow", "Atenuación"))
        self.GraphsWidget.setTabText(self.GraphsWidget.indexOf(self.FaseTab), _translate("MainWindow", "Fase"))
        self.GraphsWidget.setTabText(self.GraphsWidget.indexOf(self.RetGrupTab), _translate("MainWindow", "Ret. Grupo"))
        self.GraphsWidget.setTabText(self.GraphsWidget.indexOf(self.PazTab), _translate("MainWindow", "P and Z"))
        self.GraphsWidget.setTabText(self.GraphsWidget.indexOf(self.RespImpTab), _translate("MainWindow", "Resp. Imp."))
        self.GraphsWidget.setTabText(self.GraphsWidget.indexOf(self.RespEscTab), _translate("MainWindow", "Resp. Esc."))
        self.groupBox.setTitle(_translate("MainWindow", "Lista de Filtros"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
