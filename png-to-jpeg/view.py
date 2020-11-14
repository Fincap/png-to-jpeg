from PyQt5 import QtWidgets, QtCore

from convert import get_file_list_from_folder


class MainPage(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle("png-to-jpeg")

        self.file_list = None

        # Create central widget
        central_widget = QtWidgets.QWidget()
        central_layout = QtWidgets.QHBoxLayout(central_widget)

        # Create left panel
        left_panel = QtWidgets.QWidget()
        layout_left_panel = QtWidgets.QVBoxLayout(left_panel)
        layout_left_panel.setAlignment(QtCore.Qt.AlignTop)

        # Browse
        label_browse_files = QtWidgets.QLabel("Choose a directory of PNG files to convert.")
        button_browse_files = QtWidgets.QPushButton("Browse...")
        button_browse_files.clicked.connect(self.on_browse_clicked)

        # Quality slider
        label_choose_quality = QtWidgets.QLabel("Choose output quality.")
        widget_slider_quality = QtWidgets.QWidget()
        layout_slider_quality = QtWidgets.QHBoxLayout(widget_slider_quality)
        self.slider_quality = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_quality.setMinimum(0)
        self.slider_quality.setMaximum(95)
        self.slider_quality.setValue(75)
        self.slider_quality.valueChanged.connect(self.on_slider_updated)
        self.label_quality = QtWidgets.QLabel(str(self.slider_quality.value()))
        layout_slider_quality.addWidget(self.slider_quality)
        layout_slider_quality.addWidget(self.label_quality)

        # Output location
        label_choose_destination = QtWidgets.QLabel("Choose output destination directory.")
        widget_output_location = QtWidgets.QWidget()
        layout_output_location = QtWidgets.QHBoxLayout(widget_output_location)
        self.text_output_location = QtWidgets.QLineEdit()
        self.text_output_location.setReadOnly(True)
        button_output_location = QtWidgets.QPushButton("Browse...")
        button_output_location.clicked.connect(self.on_output_clicked)
        layout_output_location.addWidget(self.text_output_location)
        layout_output_location.addWidget(button_output_location)

        # Add widgets to the left panel
        layout_left_panel.addWidget(label_browse_files)
        layout_left_panel.addWidget(button_browse_files)
        layout_left_panel.addWidget(QHLine())
        layout_left_panel.addWidget(label_choose_quality)
        layout_left_panel.addWidget(widget_slider_quality)
        layout_left_panel.addWidget(label_choose_destination)
        layout_left_panel.addWidget(widget_output_location)

        central_layout.addWidget(left_panel)
        self.setCentralWidget(central_widget)

    def on_browse_clicked(self):
        filepath = QtWidgets.QFileDialog.getExistingDirectory(self, "Open Directory")
        if filepath != '':
            self.file_list = get_file_list_from_folder(filepath)
            print(self.file_list)

    def on_slider_updated(self, value):
        self.label_quality.setText(str(value))

    def on_output_clicked(self):
        filepath = QtWidgets.QFileDialog.getExistingDirectory(self, "Open Directory")
        if filepath != '':
            self.text_output_location.setText(filepath)


class QHLine(QtWidgets.QFrame):
    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.setFrameShape(QtWidgets.QFrame.HLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)
