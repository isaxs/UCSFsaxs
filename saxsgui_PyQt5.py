# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saxsgui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SAXSgui(object):
    def setupUi(self, SAXSgui):
        SAXSgui.setObjectName("SAXSgui")
        SAXSgui.resize(925, 630)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SAXSgui.sizePolicy().hasHeightForWidth())
        SAXSgui.setSizePolicy(sizePolicy)
        SAXSgui.setMinimumSize(QtCore.QSize(925, 630))
        SAXSgui.setFocusPolicy(QtCore.Qt.StrongFocus)
        SAXSgui.setWindowOpacity(1.0)
        SAXSgui.setAutoFillBackground(False)
        SAXSgui.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(SAXSgui)
        self.centralwidget.setObjectName("centralwidget")
        self.Console = QtWidgets.QTabWidget(self.centralwidget)
        self.Console.setGeometry(QtCore.QRect(50, 30, 821, 541))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Console.sizePolicy().hasHeightForWidth())
        self.Console.setSizePolicy(sizePolicy)
        self.Console.setObjectName("Console")
        self.fourierspace_tab = QtWidgets.QWidget()
        self.fourierspace_tab.setObjectName("fourierspace_tab")
        self.fourierView = GraphicsLayoutWidget(self.fourierspace_tab)
        self.fourierView.setGeometry(QtCore.QRect(10, 0, 511, 491))
        self.fourierView.setObjectName("fourierView")
        self.checkLogY = QtWidgets.QCheckBox(self.fourierspace_tab)
        self.checkLogY.setGeometry(QtCore.QRect(540, 10, 131, 20))
        self.checkLogY.setObjectName("checkLogY")
        self.checkLogX = QtWidgets.QCheckBox(self.fourierspace_tab)
        self.checkLogX.setGeometry(QtCore.QRect(540, 40, 131, 20))
        self.checkLogX.setObjectName("checkLogX")
        self.beamview = GraphicsLayoutWidget(self.fourierspace_tab)
        self.beamview.setGeometry(QtCore.QRect(540, 300, 261, 191))
        self.beamview.setObjectName("beamview")
        self.label_8 = QtWidgets.QLabel(self.fourierspace_tab)
        self.label_8.setGeometry(QtCore.QRect(550, 280, 121, 16))
        self.label_8.setObjectName("label_8")
        self.nskip_spinbox = QtWidgets.QSpinBox(self.fourierspace_tab)
        self.nskip_spinbox.setGeometry(QtCore.QRect(550, 80, 57, 24))
        self.nskip_spinbox.setMaximum(1000)
        self.nskip_spinbox.setObjectName("nskip_spinbox")
        self.label_19 = QtWidgets.QLabel(self.fourierspace_tab)
        self.label_19.setGeometry(QtCore.QRect(620, 80, 161, 16))
        self.label_19.setObjectName("label_19")
        self.nskip2_spinbox = QtWidgets.QSpinBox(self.fourierspace_tab)
        self.nskip2_spinbox.setGeometry(QtCore.QRect(550, 110, 57, 24))
        self.nskip2_spinbox.setMinimum(0)
        self.nskip2_spinbox.setMaximum(1000)
        self.nskip2_spinbox.setProperty("value", 0)
        self.nskip2_spinbox.setObjectName("nskip2_spinbox")
        self.label_20 = QtWidgets.QLabel(self.fourierspace_tab)
        self.label_20.setGeometry(QtCore.QRect(620, 110, 161, 16))
        self.label_20.setObjectName("label_20")
        self.label_22 = QtWidgets.QLabel(self.fourierspace_tab)
        self.label_22.setGeometry(QtCore.QRect(550, 160, 62, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.fourierspace_tab)
        self.label_23.setGeometry(QtCore.QRect(550, 180, 62, 16))
        self.label_23.setObjectName("label_23")
        self.qmin_label = QtWidgets.QLabel(self.fourierspace_tab)
        self.qmin_label.setGeometry(QtCore.QRect(605, 160, 206, 16))
        self.qmin_label.setObjectName("qmin_label")
        self.qmax_label = QtWidgets.QLabel(self.fourierspace_tab)
        self.qmax_label.setGeometry(QtCore.QRect(605, 180, 206, 16))
        self.qmax_label.setObjectName("qmax_label")
        self.Console.addTab(self.fourierspace_tab, "")
        self.guinierkratky_tab = QtWidgets.QWidget()
        self.guinierkratky_tab.setObjectName("guinierkratky_tab")
        self.primaryanalysis_view = GraphicsLayoutWidget(self.guinierkratky_tab)
        self.primaryanalysis_view.setGeometry(QtCore.QRect(20, 10, 781, 401))
        self.primaryanalysis_view.setObjectName("primaryanalysis_view")
        self.groupBox_4 = QtWidgets.QGroupBox(self.guinierkratky_tab)
        self.groupBox_4.setEnabled(True)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 410, 341, 91))
        self.groupBox_4.setObjectName("groupBox_4")
        self.qRgmin = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.qRgmin.setGeometry(QtCore.QRect(10, 30, 62, 24))
        self.qRgmin.setMaximum(1.0)
        self.qRgmin.setSingleStep(0.05)
        self.qRgmin.setProperty("value", 1.0)
        self.qRgmin.setObjectName("qRgmin")
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setGeometry(QtCore.QRect(80, 30, 62, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(80, 60, 62, 16))
        self.label_17.setObjectName("label_17")
        self.qRgmax = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.qRgmax.setGeometry(QtCore.QRect(10, 60, 62, 24))
        self.qRgmax.setMaximum(3.0)
        self.qRgmax.setSingleStep(0.05)
        self.qRgmax.setProperty("value", 1.3)
        self.qRgmax.setObjectName("qRgmax")
        self.guinierminpts = QtWidgets.QLineEdit(self.groupBox_4)
        self.guinierminpts.setGeometry(QtCore.QRect(180, 30, 61, 21))
        self.guinierminpts.setObjectName("guinierminpts")
        self.label_18 = QtWidgets.QLabel(self.groupBox_4)
        self.label_18.setGeometry(QtCore.QRect(250, 30, 71, 16))
        self.label_18.setObjectName("label_18")
        self.autoguinier_button = QtWidgets.QPushButton(self.groupBox_4)
        self.autoguinier_button.setGeometry(QtCore.QRect(210, 55, 91, 26))
        self.autoguinier_button.setStyleSheet("background-color: #F1BF29; font-size: 12px; color: green;")
        self.autoguinier_button.setObjectName("autoguinier_button")
        self.runprimaryanalysis = QtWidgets.QPushButton(self.guinierkratky_tab)
        self.runprimaryanalysis.setGeometry(QtCore.QRect(580, 435, 111, 26))
        self.runprimaryanalysis.setStyleSheet("background-color: #F1BF29; font-size: 12px; color: blue;")
        self.runprimaryanalysis.setObjectName("runprimaryanalysis")
        self.lb_guinier_spinbox = QtWidgets.QSpinBox(self.guinierkratky_tab)
        self.lb_guinier_spinbox.setGeometry(QtCore.QRect(410, 435, 57, 24))
        self.lb_guinier_spinbox.setObjectName("lb_guinier_spinbox")
        self.ub_guinier_spinbox = QtWidgets.QSpinBox(self.guinierkratky_tab)
        self.ub_guinier_spinbox.setGeometry(QtCore.QRect(495, 435, 57, 24))
        self.ub_guinier_spinbox.setMaximum(200)
        self.ub_guinier_spinbox.setObjectName("ub_guinier_spinbox")
        self.label_6 = QtWidgets.QLabel(self.guinierkratky_tab)
        self.label_6.setGeometry(QtCore.QRect(475, 440, 16, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.guinierkratky_tab)
        self.label_7.setGeometry(QtCore.QRect(380, 440, 26, 16))
        self.label_7.setObjectName("label_7")
        self.label_21 = QtWidgets.QLabel(self.guinierkratky_tab)
        self.label_21.setGeometry(QtCore.QRect(375, 470, 91, 16))
        self.label_21.setObjectName("label_21")
        self.qRg_label = QtWidgets.QLabel(self.guinierkratky_tab)
        self.qRg_label.setGeometry(QtCore.QRect(465, 470, 126, 16))
        self.qRg_label.setObjectName("qRg_label")
        self.label_4 = QtWidgets.QLabel(self.guinierkratky_tab)
        self.label_4.setGeometry(QtCore.QRect(375, 490, 36, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.guinierkratky_tab)
        self.label_5.setGeometry(QtCore.QRect(470, 490, 36, 16))
        self.label_5.setObjectName("label_5")
        self.guinierRg_label = QtWidgets.QLabel(self.guinierkratky_tab)
        self.guinierRg_label.setGeometry(QtCore.QRect(405, 490, 62, 16))
        self.guinierRg_label.setObjectName("guinierRg_label")
        self.I0_label = QtWidgets.QLabel(self.guinierkratky_tab)
        self.I0_label.setGeometry(QtCore.QRect(500, 490, 151, 16))
        self.I0_label.setObjectName("I0_label")
        self.Console.addTab(self.guinierkratky_tab, "")
        self.realspace_tab = QtWidgets.QWidget()
        self.realspace_tab.setObjectName("realspace_tab")
        self.realspaceView = GraphicsLayoutWidget(self.realspace_tab)
        self.realspaceView.setGeometry(QtCore.QRect(10, 0, 531, 491))
        self.realspaceView.setObjectName("realspaceView")
        self.groupBox_3 = QtWidgets.QGroupBox(self.realspace_tab)
        self.groupBox_3.setGeometry(QtCore.QRect(550, 0, 261, 141))
        self.groupBox_3.setObjectName("groupBox_3")
        self.Nr_input = QtWidgets.QLineEdit(self.groupBox_3)
        self.Nr_input.setGeometry(QtCore.QRect(10, 100, 71, 21))
        self.Nr_input.setObjectName("Nr_input")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(90, 70, 166, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(90, 40, 41, 16))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(90, 100, 121, 16))
        self.label_3.setObjectName("label_3")
        self.logalpha_input = QtWidgets.QLineEdit(self.groupBox_3)
        self.logalpha_input.setGeometry(QtCore.QRect(10, 70, 71, 21))
        self.logalpha_input.setObjectName("logalpha_input")
        self.dmax_input = QtWidgets.QLineEdit(self.groupBox_3)
        self.dmax_input.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.dmax_input.setObjectName("dmax_input")
        self.groupBox = QtWidgets.QGroupBox(self.realspace_tab)
        self.groupBox.setGeometry(QtCore.QRect(550, 210, 151, 101))
        self.groupBox.setObjectName("groupBox")
        self.varianceweighted = QtWidgets.QCheckBox(self.groupBox)
        self.varianceweighted.setGeometry(QtCore.QRect(10, 30, 131, 20))
        self.varianceweighted.setObjectName("varianceweighted")
        self.smeared = QtWidgets.QCheckBox(self.groupBox)
        self.smeared.setGeometry(QtCore.QRect(10, 55, 87, 20))
        self.smeared.setObjectName("smeared")
        self.solvepr_button = QtWidgets.QPushButton(self.realspace_tab)
        self.solvepr_button.setGeometry(QtCore.QRect(630, 440, 114, 32))
        self.solvepr_button.setStyleSheet("background-color: #0085ff; color: #ffffff;")
        self.solvepr_button.setObjectName("solvepr_button")
        self.iftresultout = QtWidgets.QLineEdit(self.realspace_tab)
        self.iftresultout.setGeometry(QtCore.QRect(550, 400, 261, 21))
        self.iftresultout.setObjectName("iftresultout")
        self.saveiftresult = QtWidgets.QCheckBox(self.realspace_tab)
        self.saveiftresult.setGeometry(QtCore.QRect(550, 370, 241, 20))
        self.saveiftresult.setObjectName("saveiftresult")
        self.Console.addTab(self.realspace_tab, "")
        self.bayesianift_tab = QtWidgets.QWidget()
        self.bayesianift_tab.setObjectName("bayesianift_tab")
        self.biftgridView = matplotlibWidget(self.bayesianift_tab)
        self.biftgridView.setGeometry(QtCore.QRect(10, 0, 401, 411))
        self.biftgridView.setObjectName("biftgridView")
        self.groupBox_2 = QtWidgets.QGroupBox(self.bayesianift_tab)
        self.groupBox_2.setGeometry(QtCore.QRect(420, 0, 381, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.Nalpha = QtWidgets.QLineEdit(self.groupBox_2)
        self.Nalpha.setGeometry(QtCore.QRect(10, 30, 51, 21))
        self.Nalpha.setObjectName("Nalpha")
        self.Ndmax = QtWidgets.QLineEdit(self.groupBox_2)
        self.Ndmax.setGeometry(QtCore.QRect(10, 60, 51, 21))
        self.Ndmax.setObjectName("Ndmax")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(70, 30, 91, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(70, 60, 101, 16))
        self.label_10.setObjectName("label_10")
        self.minlogalpha = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.minlogalpha.setGeometry(QtCore.QRect(20, 120, 62, 24))
        self.minlogalpha.setMinimum(-100.0)
        self.minlogalpha.setMaximum(100.0)
        self.minlogalpha.setProperty("value", 4.0)
        self.minlogalpha.setObjectName("minlogalpha")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(20, 100, 111, 16))
        self.label_11.setObjectName("label_11")
        self.maxlogalpha = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.maxlogalpha.setGeometry(QtCore.QRect(110, 120, 62, 24))
        self.maxlogalpha.setMinimum(-100.0)
        self.maxlogalpha.setMaximum(100.0)
        self.maxlogalpha.setProperty("value", 10.0)
        self.maxlogalpha.setObjectName("maxlogalpha")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(220, 100, 111, 16))
        self.label_13.setObjectName("label_13")
        self.mindmax = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.mindmax.setGeometry(QtCore.QRect(220, 120, 62, 24))
        self.mindmax.setDecimals(3)
        self.mindmax.setMaximum(9999.0)
        self.mindmax.setObjectName("mindmax")
        self.maxdmax = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.maxdmax.setGeometry(QtCore.QRect(310, 120, 62, 24))
        self.maxdmax.setDecimals(3)
        self.maxdmax.setMaximum(9999.0)
        self.maxdmax.setObjectName("maxdmax")
        self.calcbiftgrid = QtWidgets.QPushButton(self.bayesianift_tab)
        self.calcbiftgrid.setGeometry(QtCore.QRect(520, 180, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.calcbiftgrid.setFont(font)
        self.calcbiftgrid.setStyleSheet("background-color: #6495ed; color: #ffffff;")
        self.calcbiftgrid.setObjectName("calcbiftgrid")
        self.label_12 = QtWidgets.QLabel(self.bayesianift_tab)
        self.label_12.setGeometry(QtCore.QRect(510, 120, 10, 16))
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(self.bayesianift_tab)
        self.label_14.setGeometry(QtCore.QRect(710, 120, 10, 16))
        self.label_14.setObjectName("label_14")
        self.refinebift = QtWidgets.QPushButton(self.bayesianift_tab)
        self.refinebift.setGeometry(QtCore.QRect(515, 325, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.refinebift.setFont(font)
        self.refinebift.setStyleSheet("background-color:#87cc83; color: #ffffff;")
        self.refinebift.setObjectName("refinebift")
        self.line = QtWidgets.QFrame(self.bayesianift_tab)
        self.line.setGeometry(QtCore.QRect(420, 270, 391, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Console.addTab(self.bayesianift_tab, "")
        SAXSgui.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SAXSgui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 925, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        SAXSgui.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SAXSgui)
        self.statusbar.setObjectName("statusbar")
        SAXSgui.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(SAXSgui)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(SAXSgui)
        self.actionClose.setObjectName("actionClose")
        self.actionExit = QtWidgets.QAction(SAXSgui)
        self.actionExit.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionExit.setObjectName("actionExit")
        self.actionGuinier_Plot = QtWidgets.QAction(SAXSgui)
        self.actionGuinier_Plot.setObjectName("actionGuinier_Plot")
        self.actionKratky_Plot = QtWidgets.QAction(SAXSgui)
        self.actionKratky_Plot.setObjectName("actionKratky_Plot")
        self.actionSAXSMoW = QtWidgets.QAction(SAXSgui)
        self.actionSAXSMoW.setObjectName("actionSAXSMoW")
        self.actionFoXS_fit = QtWidgets.QAction(SAXSgui)
        self.actionFoXS_fit.setObjectName("actionFoXS_fit")
        self.actionLoad_Beam_Profile = QtWidgets.QAction(SAXSgui)
        self.actionLoad_Beam_Profile.setObjectName("actionLoad_Beam_Profile")
        self.actionSave_as_GNOM_file = QtWidgets.QAction(SAXSgui)
        self.actionSave_as_GNOM_file.setObjectName("actionSave_as_GNOM_file")
        self.actionSAXSMoW_2 = QtWidgets.QAction(SAXSgui)
        self.actionSAXSMoW_2.setObjectName("actionSAXSMoW_2")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_as_GNOM_file)
        self.menuFile.addAction(self.actionLoad_Beam_Profile)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(SAXSgui)
        self.Console.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SAXSgui)

    def retranslateUi(self, SAXSgui):
        _translate = QtCore.QCoreApplication.translate
        SAXSgui.setWindowTitle(_translate("SAXSgui", "UCSFsaxs v0.6"))
        self.checkLogY.setText(_translate("SAXSgui", "Log-scale Y-axis"))
        self.checkLogX.setText(_translate("SAXSgui", "Log-scale X-axis"))
        self.label_8.setText(_translate("SAXSgui", "Beam Profile"))
        self.label_19.setText(_translate("SAXSgui", "Initial Points to skip"))
        self.label_20.setText(_translate("SAXSgui", "End Points to skip"))
        self.label_22.setText(_translate("SAXSgui", "q_min : "))
        self.label_23.setText(_translate("SAXSgui", "q_max : "))
        self.qmin_label.setText(_translate("SAXSgui", "None"))
        self.qmax_label.setText(_translate("SAXSgui", "None"))
        self.Console.setTabText(self.Console.indexOf(self.fourierspace_tab), _translate("SAXSgui", "Fourier Space (Scattering)"))
        self.groupBox_4.setTitle(_translate("SAXSgui", "Automated Guinier Analysis"))
        self.label_16.setText(_translate("SAXSgui", "qRg_min"))
        self.label_17.setText(_translate("SAXSgui", "qRg_max"))
        self.guinierminpts.setText(_translate("SAXSgui", "10"))
        self.label_18.setText(_translate("SAXSgui", "Min. points"))
        self.autoguinier_button.setText(_translate("SAXSgui", "Do it (Auto)!"))
        self.runprimaryanalysis.setText(_translate("SAXSgui", "Do it (Manual)!"))
        self.label_6.setText(_translate("SAXSgui", "to"))
        self.label_7.setText(_translate("SAXSgui", "Fit"))
        self.label_21.setText(_translate("SAXSgui", "current qRg : "))
        self.qRg_label.setText(_translate("SAXSgui", "None"))
        self.label_4.setText(_translate("SAXSgui", "Rg : "))
        self.label_5.setText(_translate("SAXSgui", "I(0):"))
        self.guinierRg_label.setText(_translate("SAXSgui", "None"))
        self.I0_label.setText(_translate("SAXSgui", "None"))
        self.Console.setTabText(self.Console.indexOf(self.guinierkratky_tab), _translate("SAXSgui", "Guinier, Kratky Plots"))
        self.groupBox_3.setTitle(_translate("SAXSgui", "IFT parameters"))
        self.label_2.setText(_translate("SAXSgui", "Log(alpha) - Smoothness"))
        self.label.setText(_translate("SAXSgui", "Dmax"))
        self.label_3.setText(_translate("SAXSgui", "# of points in P(r)"))
        self.groupBox.setTitle(_translate("SAXSgui", "Data Parameters"))
        self.varianceweighted.setText(_translate("SAXSgui", "σ^2 weighted"))
        self.smeared.setText(_translate("SAXSgui", "Smeared"))
        self.solvepr_button.setText(_translate("SAXSgui", "Solve P(r)!"))
        self.saveiftresult.setText(_translate("SAXSgui", "Save File? Enter file name below:"))
        self.Console.setTabText(self.Console.indexOf(self.realspace_tab), _translate("SAXSgui", "Real Space"))
        self.groupBox_2.setTitle(_translate("SAXSgui", "Grid Search Parameters"))
        self.Nalpha.setText(_translate("SAXSgui", "10"))
        self.Ndmax.setText(_translate("SAXSgui", "10"))
        self.label_9.setText(_translate("SAXSgui", "No. of alpha"))
        self.label_10.setText(_translate("SAXSgui", "No. of Dmax"))
        self.label_11.setText(_translate("SAXSgui", "log(alpha) Range"))
        self.label_13.setText(_translate("SAXSgui", "Dmax Range"))
        self.calcbiftgrid.setText(_translate("SAXSgui", "Calculate Grid"))
        self.label_12.setText(_translate("SAXSgui", "-"))
        self.label_14.setText(_translate("SAXSgui", "-"))
        self.refinebift.setText(_translate("SAXSgui", "Refine Solution (Simplex)"))
        self.Console.setTabText(self.Console.indexOf(self.bayesianift_tab), _translate("SAXSgui", "BayesianIFT"))
        self.menuFile.setTitle(_translate("SAXSgui", "File"))
        self.actionOpen.setText(_translate("SAXSgui", "Open"))
        self.actionOpen.setToolTip(_translate("SAXSgui", "Open SAXS data file"))
        self.actionClose.setText(_translate("SAXSgui", "Close"))
        self.actionExit.setText(_translate("SAXSgui", "Exit Program"))
        self.actionGuinier_Plot.setText(_translate("SAXSgui", "Guinier Plot"))
        self.actionKratky_Plot.setText(_translate("SAXSgui", "Kratky Plot"))
        self.actionSAXSMoW.setText(_translate("SAXSgui", "SAXSMoW"))
        self.actionFoXS_fit.setText(_translate("SAXSgui", "FoXS fit ..."))
        self.actionLoad_Beam_Profile.setText(_translate("SAXSgui", "Load Beam Profile"))
        self.actionSave_as_GNOM_file.setText(_translate("SAXSgui", "Save as GNOM file ..."))
        self.actionSAXSMoW_2.setText(_translate("SAXSgui", "SAXSMoW"))

from mplWidget import matplotlibWidget
from pyqtgraph import GraphicsLayoutWidget