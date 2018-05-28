# <editor-fold desc="编码检测">

# pip install chardet

import chardet

ch = chardet.detect('hello,world'.encode('utf-8'))
print(ch)  # {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}

a = '再见了，心爱的'.encode('gbk')
print(chardet.detect(a))  # {'encoding': 'GB2312', 'confidence': 0.99, 'language': 'Chinese'}

# </editor-fold>

# <editor-fold desc="图像处理">

# pip install pillow

from PIL import Image, ImageFilter

im = Image.open('kkk.jpg')

(w, h) = im.size

print("图片尺寸：%sx%s" % (w, h))

# 缩放图片
im.thumbnail((w / 2, h / 2))

im.save('scale.jpg', 'jpeg')

# 模糊效果图片
im.filter(ImageFilter.BLUR)

im.save('blur.jpg', 'jpeg')

# 图片验证码
from PIL import ImageDraw, ImageFont
import random


def randChar():
    return chr(random.randint(65, 90))


def randColor():
    return (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255))


def randColor2():
    return (random.randint(60, 255), random.randint(60, 255), random.randint(60, 255))


# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=randColor())
# 输出文字:
for t in range(6):
    draw.text((40 * t + 10, random.randint(0, 20)), randChar(), font=font, fill=randColor2())

# 模糊:
# image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')

# </editor-fold>
