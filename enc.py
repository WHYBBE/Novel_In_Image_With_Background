from PIL import Image
import math


def encode(text):
    img = Image.open('bg.jpg')
    str_len = len(text)
    width = math.ceil(str_len**0.5)
    img = img.resize((width, width))
    red = img.split()
    im = Image.new("RGB", (width, width), 0x0)

    x, y = 0, 0
    index_ago=0
    for i in text:
        color = img.getpixel((x, y))
        index = ord(i)
        if index_ago % 3 == 1:
            rgb = (color[0],  (index & 0xFF00) >> 8,  index & 0xFF)
        elif index_ago % 3 == 2:
            rgb = ((index & 0xFF00) >> 8, color[1],  index & 0xFF)
        else:
            rgb = ((index & 0xFF00) >> 8,  index & 0xFF, color[2])
        im.putpixel((x, y),  rgb)
        index_ago=index
        if x == width - 1:
            x = 0
            y += 1
        else:
            x += 1
    return im


def main(filename: str):
    with open(filename, encoding="utf-8") as f:
        all_text = f.read()

    im = encode(all_text)
    im.save("{}_layout.bmp".format('.'.join(filename.split('.')[:-1])))


if __name__ == '__main__':
    main('三体全集.txt')

#(index & 0xFF0000) >> 16
