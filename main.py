import sys

from PIL import Image

if __name__ == '__main__':
    im = Image.open(sys.argv[0])
    rgb_im = im.convert('RGB')
    rgb_im.save('colors.jpg', quality=75)
