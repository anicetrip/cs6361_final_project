"""
:Discription: 
:Author:  17566
:Create:  2021/11/22 19:02
"""

def get_kor_charset(start, end):
    COMPLETE_RANGE = (int(start, 16), int(end, 16))
    COMPLETE_SET = frozenset(chr(code) for code in range(COMPLETE_RANGE[0], COMPLETE_RANGE[1]+1))
    COMPLETE_LIST = sorted(COMPLETE_SET)
    return COMPLETE_LIST

def get_kor_charsetList():
    start = 'ac00'
    end = 'd7a3'
    chars = get_kor_charset(start, end)
    return chars


