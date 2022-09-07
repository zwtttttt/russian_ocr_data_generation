# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 20:19:55 2022

@author: zwt
@email: 1030456532@qq.com
"""
import os
import random
import numpy as np
from typing import Iterable
from PIL import Image, ImageFont, ImageDraw

from utils.colorstr import colorstr

class Style:
    def __init__(self, opt) -> None:
        self.opt = opt
        
        # default style.
        self.DEFAULT_FONT = "arial.ttf"
        self.DEFAULT_FONT_SIZE = int(self.opt.background_size[0] // 16)
        
        self.IMG_SUFFIX = ['jpg', 'png', 'bmp']
        self.BACKGROUND_IMGS = []

    def random_size(self, flag, size):
        if isinstance(size, int): return int(size * random.uniform(0.8, 1.2)) if flag else size
        return tuple(int(s * random.uniform(0.8, 1.2)) for s in size) if flag and isinstance(size, Iterable) else size

    def strings_size(self, strings, font):
        return ImageDraw.Draw(Image.new("RGB", (1, 1), (0, 0, 0))).textsize(strings, font)

    """
    Args: 
        img - Numpy array. (h, w, c)
        size - The strings size (w, h)

    Return: 
        Numpy array
    """
    def random_crop_img(self, img, size):
        h, w, _ = img.shape
        xmin, ymin = (random.randint(0, x) for x in [w, h])
        
        # 1: xmin to right, ymin to right
        xmax, ymax = (x + size[i] if x + size[i] < [w, h][i] else [w, h][i] for i, x in enumerate([xmin, ymin]))
        # 2: xmin to left, ymin to left
        xmin, ymin = (x if [xmax, ymax][i] - size[i] == x else max(0, [xmax, ymax][i] - size[i]) for i, x in enumerate([xmin, ymin]))
        # 3: link if is still smaller than size.
        if xmax - xmin < size[0] or ymax - ymin < size[1]:
            new_img = np.ones((size[1], size[0], _))
            for i in range(size[0] // xmax + 1): # w.
                for j in range(size[1] // ymax + 1): # h.
                    new_img[ymax * j: min(ymax * (j + 1), size[1]), xmax * i: min(xmax * (i + 1), size[0]), :] = img[0: min(h, size[1] - ymax * j), 0: min(w, size[0] - xmax * i), :]
            img, xmin, ymin, xmax, ymax = np.uint8(new_img), 0, 0, size[0], size[1]

        return img[ymin: ymax, xmin: xmax, :]

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
    def background(self, strings, font):
        safe_area = 20 # 20 pixel as safe area
        safe_size = tuple(s + safe_area for s in self.strings_size(strings, font))
        size = tuple(max(self.random_size(self.opt.random_background_size, self.opt.background_size)[i], safe_size[i]) for i in range(2))
        
        if self.opt.background_path is None:
            if self.opt.random_background_color:
                # Add random color as data augmentation.
                color = tuple(random.randint(0, 256) for _ in range(3)) if random.uniform(0, 1) < 0.4 else  self.opt.background_color
            else: self.opt.background_color
            font_color = tuple(255 - c for c in color) # font color.
            
            print(f"{colorstr('background:')} size: {size} | color: {color} | fontcolor: {font_color}")
            return Image.new("RGB", size, color), font_color, safe_size
        else:
            if not os.path.exists(self.opt.background_path): raise Exception(f"The background path is not exist. pleace check it {colorstr(self.opt.background_path)}")
            bgs = [] # background imgs.
            if not self.BACKGROUND_IMGS: 
                for f in os.listdir(self.opt.background_path):
                    if f.split('.')[-1] in self.IMG_SUFFIX:
                        bgs.append(Image.open(os.path.join(self.opt.background_path, f)))
                self.BACKGROUND_IMGS = bgs
            else: bgs = self.BACKGROUND_IMGS
            bg = np.array(random.sample(bgs, 1)[0]) # random sample one bg. h, w, c
            
            # crop img or link them.
            bg = self.random_crop_img(bg, size)

            return Image.fromarray(bg), (0, 0, 0), safe_size


"""
TODO: (we should just create a file and randomly choose the font and set the size by opt.)
"""
def generate_strings(opt, strings: str):
    # Generate the style Class.
    style = Style(opt)

    font = style.font()
    bg, font_color, safe_size = style.background(strings, font)
    
    # TODO: drawtext(bg, strings, font_color, font, safe_size)
    
    dr = ImageDraw.Draw(bg)

    dr.text((10, 5), strings, fill=font_color, font=font)

    bg.show()
    bg.save('./temp.png')