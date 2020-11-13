import sys

from PIL import Image

if __name__ == '__main__':
    im = Image.open(sys.argv[1])
    rgb_im = im.convert('RGB')
    rgb_im.save('output/colors.jpg', quality=75)
