from PIL import Image

def decode(im):
    width, height = im.size
    lst = [ ]
    index_ago=0
    for y in range(height):
        for x in range(width):
            red, green, blue = im.getpixel((x, y))
            if (blue | green | red) == 0:
                break
            if(index_ago%3==1):
                index = (green << 8) + blue
            elif(index_ago%3==2):
                index = (red << 8) + blue
            else:
                index = (red << 8) + green
            index_ago=index
            lst.append( chr(index) )

    return ''.join(lst)


def main(filename: str):
    all_text = decode(Image.open(filename))
    with open("{}_decode.txt".format('.'.join(filename.split('.')[:-1])), "w", encoding = "utf-8") as f:
        f.write(all_text)

if __name__ == '__main__':
    main('out.bmp')
