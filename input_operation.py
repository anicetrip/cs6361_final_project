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
    input_sentences = input_sentences.rstrip('0123456789１２３４５６７８９０．％')
    punc_CN_EN = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《{}'
    input_sentences = re.sub(r"[%s]+" %punc_CN_EN, "", input_sentences)
    return input_sentences
