# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 21:18:32 2022

@author: zwt
@email: 1030456532@qq.com
"""
import argparse
import utils.random_strings as rs
import utils.generate_data as generate

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', type=int, default=10, help='the count of the screen shots.')
    parser.add_argument('--s_length', type=int, default=10, help='the length of the strings.')
    parser.add_argument('--s_group', type=int, default=4, help='the group of the strings. <- just like this sentence, group is 5.')
    parser.add_argument('--save_path', type=str, default='./data', help='the path u wanna save the img data.')
    
    # the args of the screen shot.
    parser.add_argument('--xmin', type=int, default=900, help='lef top x')
    parser.add_argument('--ymin', type=int, default=900, help='lef top y')
    parser.add_argument('--xmax', type=int, default=900, help='right bottom x')
    parser.add_argument('--ymax', type=int, default=900, help='right bottom y')
    return parser
    
def main(opt):
    # 1. random strings.
    strings = rs.random_russian(opt.s_length, opt.s_group, rs.COMMON_RU_MODE)

    # 2. generate the data pic. 
    generate.generate_strings(strings)
    
if __name__ == "__main__":
    opt = parse().parse_args()
    main(opt)