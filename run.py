# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 21:18:32 2022

@author: zwt
@email: 1030456532@qq.com
"""
import argparse
from utils.random_strings import COMMON_RU_MODE
from utils.random_strings import random_russian
from utils.generate import generate_strings

def parse():
    parser = argparse.ArgumentParser()
    # strings arguments.
    parser.add_argument('--count', type=int, default=10, help='the count of the screen shots.')
    parser.add_argument('--length', type=int, default=10, help='the length of the strings.')
    parser.add_argument('--group', type=int, default=4, help='the group of the strings. <- just like this sentence, group is 5.')
    
    # font style.
    parser.add_argument('--font_size', type=int, default=16, help='size of the letter. font size.')
    parser.add_argument('--random_font', type=int, default=1, help='[0, 1] 0: default font, 1: random font in the font path files.')
    parser.add_argument('--multi_size', type=int, default=1, help='[0, 1] 0: stable font size, 1: multi size in [fontsize * 0.8, fontsize * 1.2].')
    
    # background style. #TODO
    
    # path arguments.
    parser.add_argument('--save_path', type=str, default='./data', help='the path u wanna save the img data.')
    parser.add_argument('--font_path', type=str, default='./style/fontss', help='the path for the font file.')
    parser.add_argument('--background_path', type=str, default='./style/bg', help='the path for the background file.')

    
    return parser
    
def main(opt):
    # 1. random strings.
    strings = random_russian(opt.length, opt.group, COMMON_RU_MODE)

    # 2. generate the data pic. 
    generate_strings(opt, strings)
    
if __name__ == "__main__":
    opt = parse().parse_args()
    main(opt)