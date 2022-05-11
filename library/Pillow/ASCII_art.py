from PIL import Image, ImageDraw, ImageFont
import random
import math
# https://python-scripts.com/pillow
# https://картинки-для-срисовки.рф/srisovka/krasivaya-golova-lisy/


def my_image():

    image = Image.open('/home/fox/Pictures/images/001.jpg')
    # image.show()

    cropped = image.crop((177, 882, 1179, 1707))
    cropped.save('/home/fox/Pictures/images/002.jpg')


def my_image2():
    BACK_COLOR = "BLACK"
    IN_IMG = '/home/fox/Pictures/images/002.jpg'
    FNT = ImageFont.truetype("/home/fox/PycharmProjects/projects_training/library/Pillow/arial.ttf", 7)

    im = Image.open(IN_IMG)
    (width, height) = im.size

    line = math.ceil(im.size[0] / 50 * 13 * 1.2)
    row = math.ceil(im.size[1] / 50 * 6 * 1.2)

    string = ''
    for i in range(row):
        for j in range(line):
            string += str(random.choice([0, 1]))
        string += '\n'

    img = Image.new('RGBA', (im.size[0], im.size[1]), BACK_COLOR)
    draw_text = ImageDraw.Draw(img)
    draw_text.text((1, 1), string, spacing=1, font=FNT, fill=0)
    img2 = Image.open(IN_IMG)
    alphaComposited = Image.alpha_composite(img2, img)

    image = alphaComposited
    new_image = Image.new("RGBA", image.size, BACK_COLOR)
    new_image.paste(image, (0, 0), image)
    new_image.convert('RGB').save('READY_RESULT.jpg', "JPEG")
    # img22 = Image.open('READY_RESULT.jpg')
    new_image.save('/home/fox/Pictures/images/002.jpg')
    new_image.show()

def hhh():
    image = Image.open('/home/fox/Pictures/images/002.jpg')
    draw = ImageDraw.Draw(image)

    # use a bitmap font
    font = ImageFont.load("/library/Pillow/arial.ttf")
    draw.text((10, 10), "hello", font=font)

    # # use a truetype font
    # font = ImageFont.truetype("arial.ttf", 15)
    #
    # draw.text((10, 25), "world", font=font)

if __name__ == '__main__':
        # my_image()
    my_image2()

