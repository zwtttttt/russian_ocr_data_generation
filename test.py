# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 15:45:48 2022

@author: zwt
@email: 1030456532@qq.com
"""

from PIL import Image, ImageFont, ImageDraw

font = ImageFont.truetype("arial.ttf", 15)

text = 'овшщфоц'

img = Image.new("RGB", (300, 50), (255, 255, 255))

dr = ImageDraw.Draw(img)

dr.text((10, 5), text, fill='#000000', font=font)

img.show()
img.save('./temp.png')