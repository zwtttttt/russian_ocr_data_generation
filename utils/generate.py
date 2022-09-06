# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 20:19:55 2022

@author: zwt
@email: 1030456532@qq.com
"""
import os
import random
from typing import Iterable
from PIL import Image, ImageFont, ImageDraw

from utils.colorstr import colorstr

class Style:
    def __init__(self, opt) -> None:
        self.opt = opt
        
        # default style.
        self.DEFAULT_FONT = "arial.ttf"
        self.DEFAULT_FONT_SIZE = int(self.opt.background_size[0] // 16)

    def random_size(self, flag, size):
        if isinstance(size, int): return int(size * random.uniform(0.8, 1.2)) if flag else size
        return tuple(int(s * random.uniform(0.8, 1.2)) for s in size) if flag and isinstance(size, Iterable) else size

    def font(self):
        size = self.opt.font_size if self.opt.font_size is not None else self.DEFAULT_FONT_SIZE
        size = self.random_size(self.opt.random_font_size, size)
        
        if not os.path.exists(self.opt.font_path): 
            print(f"{colorstr('font:')} size: {size} | style: {self.DEFAULT_FONT}")
            
            return ImageFont.truetype(self.DEFAULT_FONT, size)
        
        # FIXME: use a tool to generate the bitmap font by using the ttf font file.
        # fonts = [os.path.join(self.opt.font_path, f) for f in os.listdir(self.opt.font_path)]
        # font = random.sample(fonts, 1)[0]
        # print(colorstr(f"font: {font}"))
        # return ImageFont.load_path(font)
    
    #TODO: set the backgroup color and size by using opt arguments.
    def background(self):
        size = self.random_size(self.opt.random_background_size, self.opt.background_size)
        if self.opt.background_color is not None:
            color = tuple(random.randint(0, 256) for i in range(3)) if self.opt.random_background_color else self.opt.background_color
            font_color = tuple(255 - c for c in color) # font color.
            
            print(f"{colorstr('background:')} size: {size} | color: {color} | fontcolor: {font_color}")
            return Image.new("RGB", size, color), font_color

"""
TODO: (we should just create a file and randomly choose the font and set the size by opt.)
"""
def generate_strings(opt, string: str):
    style = Style(opt)
    
    font = style.font()
    bg, font_color = style.background()
    
   
    
    dr = ImageDraw.Draw(bg)

    dr.text((10, 5), string, fill=font_color, font=font)

    bg.show()
    bg.save('./temp.png')