import logging
import os

from PIL import Image


def convert_png_to_jpeg(file_paths: list, destination_folder: str, quality: int):
    """
    Converts all the given PNG files into JPEGs of the given quality.
    :param file_paths: A list of file paths pointing to each PNG file to be converted.
    :param destination_folder: The folder where the converted images will be saved to.
    :param quality: Quality of the output JPEG files on a scale from 0 (worst) to 95 (best).
    """

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
