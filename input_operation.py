"""
:Discription: input operation
:Author:  17566$
:Create:  2021/11/22$ 13:32$
"""
import re, string


def input_operation():
    '''

    :return: dealing with inputs
    '''
    print("I can judge whether your sentences are  Japanese, Korean, English, Hindī,and Russian!")
    input_sentences = input("input your sentences \n")
    input_sentences = input_sentences.replace("\n", "")
    input_sentences = stringQ2B(input_sentences)
    input_sentences = input_sentences.rstrip('0123456789１２３４５６７８９０．％')
    punc_CN_EN = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《{}'
    input_sentences = re.sub(r"[%s]+" %punc_CN_EN, "", input_sentences)
    return input_sentences




def stringQ2B(ustring):
    """把字符串全角转半角"""
    return "".join([Q2B(uchar) for uchar in ustring])


def Q2B(uchar):
    """单个字符 全角转半角"""
    inside_code = ord(uchar)
    if inside_code == 0x3000:
        inside_code = 0x0020
    else:
        inside_code -= 0xfee0
    if inside_code < 0x0020 or inside_code > 0x7e: #转完之后不是半角字符返回原来的字符
        return uchar
    return chr(inside_code)
