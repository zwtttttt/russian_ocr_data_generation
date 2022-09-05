# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 20:19:55 2022

@author: zwt
@email: 1030456532@qq.com
"""
import os
import random
from PIL import Image, ImageFont, ImageDraw

from utils.colorstr import colorstr

class Style:
    def __init__(self, opt) -> None:
        self.opt = opt
        
        # default style.
        self.DEFAULT_FONT = "arial.ttf"
        self.DEFAULT_SIZE = 16

    def font(self):
        font_size = max(self.DEFAULT_SIZE, self.opt.font_size)
        font_size = int(font_size * random.uniform(0.8, 1.2)) if self.opt.multi_size else font_size
        
        if not os.path.exists(self.opt.font_path): 
            print(
                f"{colorstr('warning:')} The font folder is not exist ! please check it: {self.opt.font_path}", 
                f"we will use the default font to replace it: {self.DEFAULT_FONT}", 
                sep='\n'
            )
            print(f"font: size: {font_size} | style: {self.DEFAULT_FONT}")
            return ImageFont.truetype(self.DEFAULT_FONT, font_size)
        
        # FIXME: use a tool to generate the bitmap font by using the ttf font file.
        # fonts = [os.path.join(self.opt.font_path, f) for f in os.listdir(self.opt.font_path)]
        # font = random.sample(fonts, 1)[0] if self.opt.random_font else fonts[0]
        # print(colorstr(f"font: {font}"))
        # return ImageFont.load_path(font)
    
    def background(self):
        #TODO: set the backgroup color and size by using opt arguments.
        pass

"""
@TODO: (we should just create a file and randomly choose the font and set the size by opt.)
"""
def generate_strings(opt, string: str):
    style = Style(opt)
    
    font = style.font()
    
    img = Image.new("RGB", (300, 50), (255, 255, 255))
    
    dr = ImageDraw.Draw(img)

    dr.text((10, 5), string, fill='#000000', font=font)

    img.show()
    img.save('./temp.png')