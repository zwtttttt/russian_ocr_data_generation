# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 20:19:55 2022

@author: zwt
@email: 1030456532@qq.com
"""
from PIL import Image, ImageFont, ImageDraw

"""
@TODO: (we should just create a file and randomly choose the font and set the size by opt.)
"""
def generate_strings(string: str):
    font = ImageFont.truetype("arial.ttf", 15)
    img = Image.new("RGB", (300, 50), (255, 255, 255))
    
    dr = ImageDraw.Draw(img)

    dr.text((10, 5), string, fill='#000000', font=font)

    img.show()
    img.save('./temp.png')