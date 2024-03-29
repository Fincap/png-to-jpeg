import logging
import os
from io import BytesIO

from PIL import Image
from PyQt5 import QtGui


def convert_png_to_jpeg(file_paths: list, destination_folder: str, quality: int):
    """
    Converts all the given PNG files into JPEGs of the given quality.
    :param file_paths: A list of file paths pointing to each PNG file to be converted.
    :param destination_folder: The folder where the converted images will be saved to.
    :param quality: Quality of the output JPEG files on a scale from 0 (worst) to 95 (best).
    """

    # If the output directory doesn't exist, it needs to be created first.
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for file in file_paths:
        # Generate new file name (i.e. given "/path/to/image.png", produce "output/folder/image.jpg"
        file_name_with_extension = os.path.basename(file)
        file_name_no_extension = os.path.splitext(file_name_with_extension)[0]
        output_file_name = file_name_no_extension + '.jpg'
        output_file_location = destination_folder + os.sep + output_file_name

        # Load the image and convert it to JPEG
        im = Image.open(file)
        rgb_im = im.convert('RGB')
        rgb_im.save(output_file_location, quality=quality)

        logging.info("Converted image: %s, saved to: %s" % (file_name_with_extension, output_file_location))

    logging.info("Image conversion complete.")


def get_file_list_from_folder(folder_to_check: str) -> list:
    """
    Generates a list of PNG files found within the given folder.
    :param folder_to_check: The folder to check for PNG files.
    :return: List of absolute file paths found.
    """
    file_path_list = []
    for file in os.listdir(folder_to_check):
        if file.endswith('.png'):
            abs_path = folder_to_check + os.sep + file
            file_path_list.append(abs_path)

    return file_path_list


def get_preview_pixmap(filepath: str, quality: int) -> QtGui.QPixmap:
    """
    Returns a QPixmap showing the result of a conversion of the given file and given quality.
    :param filepath: Path to the PNG file being converted.
    :param quality: Quality of the output JPEG file
    :return: QPixmap of converted JPEG
    """

    im = Image.open(filepath)
    rgb_im = im.convert('RGB')
    output = BytesIO()
    rgb_im.save(output, format="JPEG", quality=quality)
    return QtGui.QPixmap.fromImage(QtGui.QImage.fromData(output.getvalue()))
