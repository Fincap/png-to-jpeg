import os

from PyQt5 import QtWidgets, QtCore, QtGui

from convert import get_file_list_from_folder, convert_png_to_jpeg, get_preview_pixmap


class MainPage(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle("png-to-jpeg")

        self.file_list = []

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

        # Convert button
        button_convert = QtWidgets.QPushButton("Convert")
        button_convert.clicked.connect(self.on_convert_clicked)

        # Selected image preview
        layout_preview = QtWidgets.QLabel("Quality preview")
        self.quality_preview_label = QtWidgets.QLabel()
        self.quality_preview_label.setMaximumSize(250, 250)

        # Add widgets to the left panel
        layout_left_panel.addWidget(label_browse_files)
        layout_left_panel.addWidget(button_browse_files)
        layout_left_panel.addWidget(QHLine())
        layout_left_panel.addWidget(label_choose_quality)
        layout_left_panel.addWidget(widget_slider_quality)
        layout_left_panel.addWidget(label_choose_destination)
        layout_left_panel.addWidget(widget_output_location)
        layout_left_panel.addWidget(button_convert)
        layout_left_panel.addWidget(layout_preview)
        layout_left_panel.addWidget(self.quality_preview_label)

        # Create right panel
        right_panel = QtWidgets.QWidget()
        layout_right_panel = QtWidgets.QVBoxLayout(right_panel)
        layout_right_panel.setAlignment(QtCore.Qt.AlignTop)

        # Found items listview
        label_found_files = QtWidgets.QLabel("Files to convert")
        self.list_found_files = QtWidgets.QListWidget()
        self.list_found_files.clicked.connect(self.refresh_preview)

        # Add widgets to right panel
        layout_right_panel.addWidget(label_found_files)
        layout_right_panel.addWidget(self.list_found_files)

        central_layout.addWidget(left_panel)
        central_layout.addWidget(right_panel)
        self.setCentralWidget(central_widget)

    def refresh_preview(self):
        if self.list_found_files.currentRow() >= 0:
            pixmap = get_preview_pixmap(self.file_list[self.list_found_files.currentRow()], self.slider_quality.value())
            self.quality_preview_label.setPixmap(pixmap)

    def on_browse_clicked(self):
        filepath = QtWidgets.QFileDialog.getExistingDirectory(self, "Open Directory")
        if filepath != '':
            self.file_list = get_file_list_from_folder(filepath)

            # Update list of files loaded
            self.list_found_files.clear()
            entries = [os.path.basename(img) for img in self.file_list]  # Only show filenames
            self.list_found_files.addItems(entries)

    def on_slider_updated(self, value):
        self.label_quality.setText(str(value))
        self.refresh_preview()

    def on_output_clicked(self):
        filepath = QtWidgets.QFileDialog.getExistingDirectory(self, "Open Directory")
        if filepath != '':
            self.text_output_location.setText(filepath)

    def on_convert_clicked(self):
        if self.file_list is not None and len(self.file_list) == 0:
            QtWidgets.QMessageBox.critical(self, "Unable to convert", "No files have been selected. Please choose a"
                                                                      " directory of PNG files to convert.")
        elif self.text_output_location.text() == '':
            QtWidgets.QMessageBox.critical(self, "Unable to convert", "Destination folder not selected. Please choose a"
                                                                      " destination directory before converting.")
        else:
            convert_png_to_jpeg(self.file_list, self.text_output_location.text(), self.slider_quality.value())
            QtWidgets.QMessageBox.information(self, "Conversion complete", "JPEG files successfully output to selected"
                                                                           " directory.")


class QHLine(QtWidgets.QFrame):
    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.setFrameShape(QtWidgets.QFrame.HLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)
