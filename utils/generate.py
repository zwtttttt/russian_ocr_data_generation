# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 20:19:55 2022

@author: zwt
@email: 1030456532@qq.com
"""
import os
import warnings
from PIL import Image, ImageFont, ImageDraw

from utils.colorstr import colorstr

class Style:
    def __init__(self, opt) -> None:
        # default style.
        self.DEFAULT_FONT = "arial.ttf"


        self.opt = opt

    def font(self):
        if not os.path.exists(self.opt.font_path): 
            warnings.warn(
                f'\nThe font folder is not exist ! please check it: {colorstr(self.opt.font_path)}'
                f'\nwe will use the default font to replace it: {colorstr(self.DEFAULT_FONT)}'
            )
        
        fonts = os.listdir(self.opt.font_path)
        

"""
@TODO: (we should just create a file and randomly choose the font and set the size by opt.)
"""
def generate_strings(opt, string: str):
    style = Style(opt)
    style.font()
    
    font = ImageFont.truetype("arial.ttf", 15)
    img = Image.new("RGB", (300, 50), (255, 255, 255))
    
    dr = ImageDraw.Draw(img)

    dr.text((10, 5), string, fill='#000000', font=font)

    img.show()
    img.save('./temp.png')