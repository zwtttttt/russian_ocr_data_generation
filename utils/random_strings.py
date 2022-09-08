# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 19:55:54 2022

@author: zwt
@email: 1030456532@qq.com
"""

import random
import os

from utils.colorstr import colorstr

UNICODE_CN_MODE = "unicode()"
GBK2312_CN_MODE = "gbk2312()"
COMMON_CN_MODE = "common(type='cn')"
COMMON_RU_MODE = "common(type='ru')"

def unicode():
    return chr(random.randint(0x4e00, 0x9fbf))

def gbk2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xfe)
    val = f'{head:x}{body:x}'
    str = bytes.fromhex(val).decode('gb2312', errors='ignore')
    return str

def common(type='cn'):
    contents = []
    filename = os.path.join('./dict', f"{type}.txt")
    if not os.path.exists(filename): raise Exception(f"The dict of ur target language is not exist: {filename}")
    with open(filename, 'r', encoding='utf-8') as f:
        contents = f.read().splitlines()
    return contents


"""
This func will randomly generate chinese.

Parameters:
    length - this is the length of the strings.
    group - this is the size of the group. like [char1char2 char3 char4char5] the length will be 5 but the group is 3. 
    mode - the mode to get the chinese character. [gbk2312, unicode, common]

Raises:
    Exception: The size of group must smaller than length
"""
def random_chinese(length: int, group: int, mode: str) -> str:
    if group > length: 
        raise Exception(f"The size of group must smaller than length, please check it !!!\nlength: {length}, group: {group}")
    content = [eval(mode) for _ in range(length)] if mode != COMMON_CN_MODE else random.sample(eval(mode), length)
    ni = random.sample([content[i] for i in range(1, length)], group - 1)
    for n in ni: 
        content.insert(content.index(n), ' ')
    return "".join(content)

"""
This func will randomly generate russian.

Parameters:
    length - this is the length of the strings.
    group - this is the size of the group. like [char1char2 char3 char4char5] the length will be 5 but the group is 3. 
    mode - the mode to get the chinese character. [gbk2312, unicode, common]
    
Raises:
    Exception: The size of group must smaller than length
"""
def random_russian(length: int, group: int, mode: str) -> str:
    if group > length: 
        raise Exception(f"The size of group must smaller than length, please check it !!!\nlength: {length}, group: {group}")
    content = [eval(mode) for _ in range(length)] if mode != COMMON_RU_MODE else random.sample(eval(mode), length)
    ni = random.sample([content[i] for i in range(1, length)], group - 1)
    for n in ni: 
        content.insert(content.index(n), ' ')
    strings = "".join(content)

    print(f"{colorstr('strings: ')}{strings}")
    return strings
    
