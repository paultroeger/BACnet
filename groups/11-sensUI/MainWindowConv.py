# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(954, 668)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(1600, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tabConfigSensors = QtWidgets.QWidget()
        self.tabConfigSensors.setObjectName("tabConfigSensors")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tabConfigSensors)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frameConfigSensors = QtWidgets.QFrame(self.tabConfigSensors)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameConfigSensors.sizePolicy().hasHeightForWidth())
        self.frameConfigSensors.setSizePolicy(sizePolicy)
        self.frameConfigSensors.setFrameShape(QtWidgets.QFrame.Box)
        self.frameConfigSensors.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameConfigSensors.setObjectName("frameConfigSensors")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameConfigSensors)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frameConfigSensorsControl = QtWidgets.QFrame(self.frameConfigSensors)
        self.frameConfigSensorsControl.setMinimumSize(QtCore.QSize(600, 0))
        self.frameConfigSensorsControl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameConfigSensorsControl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameConfigSensorsControl.setObjectName("frameConfigSensorsControl")
        self.formLayout = QtWidgets.QFormLayout(self.frameConfigSensorsControl)
        self.formLayout.setObjectName("formLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.label_3 = QtWidgets.QLabel(self.frameConfigSensorsControl)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEditConfigNodeName = QtWidgets.QLineEdit(self.frameConfigSensorsControl)
        self.lineEditConfigNodeName.setObjectName("lineEditConfigNodeName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditConfigNodeName)
        self.label_4 = QtWidgets.QLabel(self.frameConfigSensorsControl)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frameConfigSensorsControl)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frameConfigSensorsControl)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.doubleSpinBoxConfigNodePositionLatitude = QtWidgets.QDoubleSpinBox(self.frameConfigSensorsControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBoxConfigNodePositionLatitude.sizePolicy().hasHeightForWidth())
        self.doubleSpinBoxConfigNodePositionLatitude.setSizePolicy(sizePolicy)
        self.doubleSpinBoxConfigNodePositionLatitude.setDecimals(6)
        self.doubleSpinBoxConfigNodePositionLatitude.setMinimum(-90.0)
        self.doubleSpinBoxConfigNodePositionLatitude.setMaximum(90.0)
        self.doubleSpinBoxConfigNodePositionLatitude.setObjectName("doubleSpinBoxConfigNodePositionLatitude")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxConfigNodePositionLatitude)
        self.doubleSpinBoxConfigNodePositionLongitude = QtWidgets.QDoubleSpinBox(self.frameConfigSensorsControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBoxConfigNodePositionLongitude.sizePolicy().hasHeightForWidth())
        self.doubleSpinBoxConfigNodePositionLongitude.setSizePolicy(sizePolicy)
        self.doubleSpinBoxConfigNodePositionLongitude.setDecimals(6)
        self.doubleSpinBoxConfigNodePositionLongitude.setMinimum(-180.0)
        self.doubleSpinBoxConfigNodePositionLongitude.setMaximum(180.0)
        self.doubleSpinBoxConfigNodePositionLongitude.setObjectName("doubleSpinBoxConfigNodePositionLongitude")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxConfigNodePositionLongitude)
        self.label_7 = QtWidgets.QLabel(self.frameConfigSensorsControl)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.doubleSpinBoxConfigNodePositionAltitude = QtWidgets.QDoubleSpinBox(self.frameConfigSensorsControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBoxConfigNodePositionAltitude.sizePolicy().hasHeightForWidth())
        self.doubleSpinBoxConfigNodePositionAltitude.setSizePolicy(sizePolicy)
        self.doubleSpinBoxConfigNodePositionAltitude.setMinimum(-14000.0)
        self.doubleSpinBoxConfigNodePositionAltitude.setMaximum(100000000.0)
        self.doubleSpinBoxConfigNodePositionAltitude.setObjectName("doubleSpinBoxConfigNodePositionAltitude")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxConfigNodePositionAltitude)
        self.frame = QtWidgets.QFrame(self.frameConfigSensorsControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(50, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.checkBoxConfigNodeSensorTemperature = QtWidgets.QCheckBox(self.frame)
        self.checkBoxConfigNodeSensorTemperature.setObjectName("checkBoxConfigNodeSensorTemperature")
        self.horizontalLayout_10.addWidget(self.checkBoxConfigNodeSensorTemperature)
        self.checkBoxConfigNodeSensorAirPressure = QtWidgets.QCheckBox(self.frame)
        self.checkBoxConfigNodeSensorAirPressure.setObjectName("checkBoxConfigNodeSensorAirPressure")
        self.horizontalLayout_10.addWidget(self.checkBoxConfigNodeSensorAirPressure)
        self.checkBoxConfigNodeSensorRelativeHumidity = QtWidgets.QCheckBox(self.frame)
        self.checkBoxConfigNodeSensorRelativeHumidity.setObjectName("checkBoxConfigNodeSensorRelativeHumidity")
        self.horizontalLayout_10.addWidget(self.checkBoxConfigNodeSensorRelativeHumidity)
        self.checkBoxConfigNodeSensorBrightness = QtWidgets.QCheckBox(self.frame)
        self.checkBoxConfigNodeSensorBrightness.setObjectName("checkBoxConfigNodeSensorBrightness")
        self.horizontalLayout_10.addWidget(self.checkBoxConfigNodeSensorBrightness)
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.frame)
        self.label_8 = QtWidgets.QLabel(self.frameConfigSensorsControl)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_2 = QtWidgets.QLabel(self.frameConfigSensorsControl)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.frame1 = QtWidgets.QFrame(self.frameConfigSensorsControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy)
        self.frame1.setObjectName("frame1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.spinBoxConfigNodeMeasurementInterval = QtWidgets.QSpinBox(self.frame1)
        self.spinBoxConfigNodeMeasurementInterval.setMaximum(100000000)
        self.spinBoxConfigNodeMeasurementInterval.setObjectName("spinBoxConfigNodeMeasurementInterval")
        self.horizontalLayout_3.addWidget(self.spinBoxConfigNodeMeasurementInterval)
        self.comboBoxConfigNodeMeasurementInterval = QtWidgets.QComboBox(self.frame1)
        self.comboBoxConfigNodeMeasurementInterval.setEditable(True)
        self.comboBoxConfigNodeMeasurementInterval.setObjectName("comboBoxConfigNodeMeasurementInterval")
        self.horizontalLayout_3.addWidget(self.comboBoxConfigNodeMeasurementInterval)
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.frame1)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.formLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frameConfigSensorsControl)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.horizontalLayout.addWidget(self.frameConfigSensorsControl)
        self.frameConfigSensorsOverview = QtWidgets.QFrame(self.frameConfigSensors)
        self.frameConfigSensorsOverview.setMinimumSize(QtCore.QSize(300, 0))
        self.frameConfigSensorsOverview.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frameConfigSensorsOverview.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameConfigSensorsOverview.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameConfigSensorsOverview.setObjectName("frameConfigSensorsOverview")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frameConfigSensorsOverview)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frameConfigSensorsOverview)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.tableView = QtWidgets.QTableView(self.frameConfigSensorsOverview)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_3.addWidget(self.tableView)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout.addWidget(self.frameConfigSensorsOverview)
        self.horizontalLayout_2.addWidget(self.frameConfigSensors)
        self.tabWidget.addTab(self.tabConfigSensors, "")
        self.tabViews = QtWidgets.QWidget()
        self.tabViews.setObjectName("tabViews")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tabViews)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frameViewsSettings = QtWidgets.QFrame(self.tabViews)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameViewsSettings.sizePolicy().hasHeightForWidth())
        self.frameViewsSettings.setSizePolicy(sizePolicy)
        self.frameViewsSettings.setMinimumSize(QtCore.QSize(400, 0))
        self.frameViewsSettings.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.frameViewsSettings.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameViewsSettings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameViewsSettings.setObjectName("frameViewsSettings")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameViewsSettings)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frameViewsSettingsName = QtWidgets.QFrame(self.frameViewsSettings)
        self.frameViewsSettingsName.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameViewsSettingsName.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameViewsSettingsName.setObjectName("frameViewsSettingsName")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frameViewsSettingsName)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.labelViewsSettingsNameLabel = QtWidgets.QLabel(self.frameViewsSettingsName)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelViewsSettingsNameLabel.setFont(font)
        self.labelViewsSettingsNameLabel.setObjectName("labelViewsSettingsNameLabel")
        self.horizontalLayout_9.addWidget(self.labelViewsSettingsNameLabel)
        self.lineEditViewsSettingsNameValue = QtWidgets.QLineEdit(self.frameViewsSettingsName)
        self.lineEditViewsSettingsNameValue.setObjectName("lineEditViewsSettingsNameValue")
        self.horizontalLayout_9.addWidget(self.lineEditViewsSettingsNameValue)
        self.verticalLayout_2.addWidget(self.frameViewsSettingsName)
        self.frameViewsSettingsYAxis = QtWidgets.QFrame(self.frameViewsSettings)
        self.frameViewsSettingsYAxis.setMinimumSize(QtCore.QSize(0, 300))
        self.frameViewsSettingsYAxis.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameViewsSettingsYAxis.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameViewsSettingsYAxis.setLineWidth(1)
        self.frameViewsSettingsYAxis.setObjectName("frameViewsSettingsYAxis")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frameViewsSettingsYAxis)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayoutViewsSettingsYAxisFirst = QtWidgets.QVBoxLayout()
        self.verticalLayoutViewsSettingsYAxisFirst.setObjectName("verticalLayoutViewsSettingsYAxisFirst")
        self.frameViewsSettingsYAxisFirstControls = QtWidgets.QFrame(self.frameViewsSettingsYAxis)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameViewsSettingsYAxisFirstControls.sizePolicy().hasHeightForWidth())
        self.frameViewsSettingsYAxisFirstControls.setSizePolicy(sizePolicy)
        self.frameViewsSettingsYAxisFirstControls.setMinimumSize(QtCore.QSize(0, 150))
        self.frameViewsSettingsYAxisFirstControls.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameViewsSettingsYAxisFirstControls.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameViewsSettingsYAxisFirstControls.setObjectName("frameViewsSettingsYAxisFirstControls")
        self.formLayout_4 = QtWidgets.QFormLayout(self.frameViewsSettingsYAxisFirstControls)
        self.formLayout_4.setObjectName("formLayout_4")
        self.labelViewsSettingsYAxisFirstControlsMeasurementSize = QtWidgets.QLabel(
            self.frameViewsSettingsYAxisFirstControls)
        self.labelViewsSettingsYAxisFirstControlsMeasurementSize.setObjectName(
            "labelViewsSettingsYAxisFirstControlsMeasurementSize")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole,
                                    self.labelViewsSettingsYAxisFirstControlsMeasurementSize)
        self.comboBoxViewsSettingsYAxisFirstControlsMeasurementSize = QtWidgets.QComboBox(
            self.frameViewsSettingsYAxisFirstControls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.comboBoxViewsSettingsYAxisFirstControlsMeasurementSize.sizePolicy().hasHeightForWidth())
        self.comboBoxViewsSettingsYAxisFirstControlsMeasurementSize.setSizePolicy(sizePolicy)
        self.comboBoxViewsSettingsYAxisFirstControlsMeasurementSize.setObjectName(
            "comboBoxViewsSettingsYAxisFirstControlsMeasurementSize")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole,
                                    self.comboBoxViewsSettingsYAxisFirstControlsMeasurementSize)
        self.labelViewsSettingsYAxisFirstControlsAxisLabel = QtWidgets.QLabel(self.frameViewsSettingsYAxisFirstControls)
        self.labelViewsSettingsYAxisFirstControlsAxisLabel.setObjectName(
            "labelViewsSettingsYAxisFirstControlsAxisLabel")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.LabelRole,
                                    self.labelViewsSettingsYAxisFirstControlsAxisLabel)
        self.lineEditViewsSettingsYAxisFirstControlsAxisLabel = QtWidgets.QLineEdit(
            self.frameViewsSettingsYAxisFirstControls)
        self.lineEditViewsSettingsYAxisFirstControlsAxisLabel.setObjectName(
            "lineEditViewsSettingsYAxisFirstControlsAxisLabel")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.FieldRole,
                                    self.lineEditViewsSettingsYAxisFirstControlsAxisLabel)
        self.checkBoxViewsSettingsYAxisFirstControlsActive = QtWidgets.QCheckBox(
            self.frameViewsSettingsYAxisFirstControls)
        self.checkBoxViewsSettingsYAxisFirstControlsActive.setObjectName(
            "checkBoxViewsSettingsYAxisFirstControlsActive")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole,
                                    self.checkBoxViewsSettingsYAxisFirstControlsActive)
        self.labelViewsSettingsYAxisFirstControlsActive = QtWidgets.QLabel(self.frameViewsSettingsYAxisFirstControls)
        self.labelViewsSettingsYAxisFirstControlsActive.setObjectName("labelViewsSettingsYAxisFirstControlsActive")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelViewsSettingsYAxisFirstControlsActive)
        self.verticalLayoutViewsSettingsYAxisFirst.addWidget(self.frameViewsSettingsYAxisFirstControls)
        self.listViewViewsSettingsYAxisFirstSensors = QtWidgets.QListView(self.frameViewsSettingsYAxis)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.listViewViewsSettingsYAxisFirstSensors.sizePolicy().hasHeightForWidth())
        self.listViewViewsSettingsYAxisFirstSensors.setSizePolicy(sizePolicy)
        self.listViewViewsSettingsYAxisFirstSensors.setObjectName("listViewViewsSettingsYAxisFirstSensors")
        self.verticalLayoutViewsSettingsYAxisFirst.addWidget(self.listViewViewsSettingsYAxisFirstSensors)
        self.horizontalLayout_8.addLayout(self.verticalLayoutViewsSettingsYAxisFirst)
        self.verticalLayoutViewsSettingsYAxisSecond = QtWidgets.QVBoxLayout()
        self.verticalLayoutViewsSettingsYAxisSecond.setObjectName("verticalLayoutViewsSettingsYAxisSecond")
        self.frameViewsSettingsYAxisSecondControls = QtWidgets.QFrame(self.frameViewsSettingsYAxis)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameViewsSettingsYAxisSecondControls.sizePolicy().hasHeightForWidth())
        self.frameViewsSettingsYAxisSecondControls.setSizePolicy(sizePolicy)
        self.frameViewsSettingsYAxisSecondControls.setMinimumSize(QtCore.QSize(0, 150))
        self.frameViewsSettingsYAxisSecondControls.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameViewsSettingsYAxisSecondControls.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameViewsSettingsYAxisSecondControls.setObjectName("frameViewsSettingsYAxisSecondControls")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frameViewsSettingsYAxisSecondControls)
        self.formLayout_3.setObjectName("formLayout_3")
        self.labelViewsSettingsYAxisSecondControlsMeasurementSize = QtWidgets.QLabel(
            self.frameViewsSettingsYAxisSecondControls)
        self.labelViewsSettingsYAxisSecondControlsMeasurementSize.setObjectName(
            "labelViewsSettingsYAxisSecondControlsMeasurementSize")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole,
                                    self.labelViewsSettingsYAxisSecondControlsMeasurementSize)
        self.comboBoxViewsSettingsYAxisSecondControlsMeasurementSize = QtWidgets.QComboBox(
            self.frameViewsSettingsYAxisSecondControls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.comboBoxViewsSettingsYAxisSecondControlsMeasurementSize.sizePolicy().hasHeightForWidth())
        self.comboBoxViewsSettingsYAxisSecondControlsMeasurementSize.setSizePolicy(sizePolicy)
        self.comboBoxViewsSettingsYAxisSecondControlsMeasurementSize.setObjectName(
            "comboBoxViewsSettingsYAxisSecondControlsMeasurementSize")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole,
                                    self.comboBoxViewsSettingsYAxisSecondControlsMeasurementSize)
        self.labelViewsSettingsYAxisSecondControlsAxisLabel = QtWidgets.QLabel(
            self.frameViewsSettingsYAxisSecondControls)
        self.labelViewsSettingsYAxisSecondControlsAxisLabel.setObjectName(
            "labelViewsSettingsYAxisSecondControlsAxisLabel")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.LabelRole,
                                    self.labelViewsSettingsYAxisSecondControlsAxisLabel)
        self.lineEditViewsSettingsYAxisSecondControlsAxisLabel = QtWidgets.QLineEdit(
            self.frameViewsSettingsYAxisSecondControls)
        self.lineEditViewsSettingsYAxisSecondControlsAxisLabel.setObjectName(
            "lineEditViewsSettingsYAxisSecondControlsAxisLabel")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole,
                                    self.lineEditViewsSettingsYAxisSecondControlsAxisLabel)
        self.checkBoxViewsSettingsYAxisSecondControlsActive = QtWidgets.QCheckBox(
            self.frameViewsSettingsYAxisSecondControls)
        self.checkBoxViewsSettingsYAxisSecondControlsActive.setObjectName(
            "checkBoxViewsSettingsYAxisSecondControlsActive")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole,
                                    self.checkBoxViewsSettingsYAxisSecondControlsActive)
        self.labelViewsSettingsYAxisSecondControlsActive = QtWidgets.QLabel(self.frameViewsSettingsYAxisSecondControls)
        self.labelViewsSettingsYAxisSecondControlsActive.setObjectName("labelViewsSettingsYAxisSecondControlsActive")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole,
                                    self.labelViewsSettingsYAxisSecondControlsActive)
        self.verticalLayoutViewsSettingsYAxisSecond.addWidget(self.frameViewsSettingsYAxisSecondControls)
        self.listViewViewsSettingsYAxisSecondSensors = QtWidgets.QListView(self.frameViewsSettingsYAxis)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.listViewViewsSettingsYAxisSecondSensors.sizePolicy().hasHeightForWidth())
        self.listViewViewsSettingsYAxisSecondSensors.setSizePolicy(sizePolicy)
        self.listViewViewsSettingsYAxisSecondSensors.setObjectName("listViewViewsSettingsYAxisSecondSensors")
        self.verticalLayoutViewsSettingsYAxisSecond.addWidget(self.listViewViewsSettingsYAxisSecondSensors)
        self.horizontalLayout_8.addLayout(self.verticalLayoutViewsSettingsYAxisSecond)
        self.verticalLayout_2.addWidget(self.frameViewsSettingsYAxis)
        self.frame_2 = QtWidgets.QFrame(self.frameViewsSettings)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.pushButtonViewsSettingsSave = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonViewsSettingsSave.setObjectName("pushButtonViewsSettingsSave")
        self.horizontalLayout_11.addWidget(self.pushButtonViewsSettingsSave)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout_5.addWidget(self.frameViewsSettings)
        self.frameViewsOverview = QtWidgets.QFrame(self.tabViews)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameViewsOverview.sizePolicy().hasHeightForWidth())
        self.frameViewsOverview.setSizePolicy(sizePolicy)
        self.frameViewsOverview.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frameViewsOverview.setObjectName("frameViewsOverview")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frameViewsOverview)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_9 = QtWidgets.QLabel(self.frameViewsOverview)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.listViewViewsOverviewControlsViews = QtWidgets.QListView(self.frameViewsOverview)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewViewsOverviewControlsViews.sizePolicy().hasHeightForWidth())
        self.listViewViewsOverviewControlsViews.setSizePolicy(sizePolicy)
        self.listViewViewsOverviewControlsViews.setObjectName("listViewViewsOverviewControlsViews")
        self.verticalLayout.addWidget(self.listViewViewsOverviewControlsViews)
        self.frameViewsOverviewControls = QtWidgets.QFrame(self.frameViewsOverview)
        self.frameViewsOverviewControls.setMinimumSize(QtCore.QSize(0, 10))
        self.frameViewsOverviewControls.setObjectName("frameViewsOverviewControls")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frameViewsOverviewControls)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButtonViewsOverviewControlsNew = QtWidgets.QPushButton(self.frameViewsOverviewControls)
        self.pushButtonViewsOverviewControlsNew.setObjectName("pushButtonViewsOverviewControlsNew")
        self.horizontalLayout_6.addWidget(self.pushButtonViewsOverviewControlsNew)
        self.pushButtonViewsOverviewControlsDelete = QtWidgets.QPushButton(self.frameViewsOverviewControls)
        self.pushButtonViewsOverviewControlsDelete.setObjectName("pushButtonViewsOverviewControlsDelete")
        self.horizontalLayout_6.addWidget(self.pushButtonViewsOverviewControlsDelete)
        self.verticalLayout.addWidget(self.frameViewsOverviewControls)
        self.horizontalLayout_5.addWidget(self.frameViewsOverview)
        self.tabWidget.addTab(self.tabViews, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 954, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHilfe = QtWidgets.QMenu(self.menubar)
        self.menuHilfe.setObjectName("menuHilfe")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHilfe.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Name:"))
        self.label_4.setText(_translate("MainWindow", "Position:"))
        self.label_5.setText(_translate("MainWindow", "Breitengrad:"))
        self.label_6.setText(_translate("MainWindow", "Längengrad:"))
        self.doubleSpinBoxConfigNodePositionLatitude.setPrefix(_translate("MainWindow", "Lat="))
        self.doubleSpinBoxConfigNodePositionLatitude.setSuffix(_translate("MainWindow", "°"))
        self.doubleSpinBoxConfigNodePositionLongitude.setPrefix(_translate("MainWindow", "Long="))
        self.doubleSpinBoxConfigNodePositionLongitude.setSuffix(_translate("MainWindow", "°"))
        self.label_7.setText(_translate("MainWindow", "Normalhöhennull:"))
        self.doubleSpinBoxConfigNodePositionAltitude.setPrefix(_translate("MainWindow", "NHN="))
        self.doubleSpinBoxConfigNodePositionAltitude.setSuffix(_translate("MainWindow", " m"))
        self.checkBoxConfigNodeSensorTemperature.setText(_translate("MainWindow", "Temperatur"))
        self.checkBoxConfigNodeSensorAirPressure.setText(_translate("MainWindow", "Luftdruck"))
        self.checkBoxConfigNodeSensorRelativeHumidity.setText(_translate("MainWindow", "Relative Luftfeuchtigkeit"))
        self.checkBoxConfigNodeSensorBrightness.setText(_translate("MainWindow", "Helligkeit"))
        self.label_8.setText(_translate("MainWindow", "Sensoren:"))
        self.label_2.setText(_translate("MainWindow", "Mess-Intervall:"))
        self.pushButton_2.setText(_translate("MainWindow", "Speichern"))
        self.label.setText(_translate("MainWindow", "Knoten:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConfigSensors),
                                  _translate("MainWindow", "Konfiguration"))
        self.labelViewsSettingsNameLabel.setText(_translate("MainWindow", "Ansicht:"))
        self.labelViewsSettingsYAxisFirstControlsMeasurementSize.setText(_translate("MainWindow", "Messgrösse:"))
        self.labelViewsSettingsYAxisFirstControlsAxisLabel.setText(_translate("MainWindow", "Bezeichnung:"))
        self.checkBoxViewsSettingsYAxisFirstControlsActive.setText(_translate("MainWindow", "Aktiv"))
        self.labelViewsSettingsYAxisFirstControlsActive.setText(_translate("MainWindow", "Linke Y-Achse"))
        self.labelViewsSettingsYAxisSecondControlsMeasurementSize.setText(_translate("MainWindow", "Messgrösse:"))
        self.labelViewsSettingsYAxisSecondControlsAxisLabel.setText(_translate("MainWindow", "Bezeichnung:"))
        self.checkBoxViewsSettingsYAxisSecondControlsActive.setText(_translate("MainWindow", "Aktiv"))
        self.labelViewsSettingsYAxisSecondControlsActive.setText(_translate("MainWindow", "Rechte Y-Achse"))
        self.pushButtonViewsSettingsSave.setText(_translate("MainWindow", "Speichern"))
        self.label_9.setText(_translate("MainWindow", "Ansichten:"))
        self.pushButtonViewsOverviewControlsNew.setText(_translate("MainWindow", "Neu"))
        self.pushButtonViewsOverviewControlsDelete.setText(_translate("MainWindow", "Löschen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabViews), _translate("MainWindow", "Ansichten"))
        self.menuFile.setTitle(_translate("MainWindow", "Datei"))
        self.menuHilfe.setTitle(_translate("MainWindow", "Hilfe"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())