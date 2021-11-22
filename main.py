"""
The main function
:Author:
:Create:  2021/11/22 13:27
"""
import check_for_japanese
import input_operation


def main():
    # Input system
    pre_operation_strings = input_operation.input_operation()

    # Judging system
    '''
    I need a form like check_result_information = [0,"JP",0], 
    the first one is used to give a result about whether it is this language, 
    the second is a name(can use a shorten one or full name) so I can know which language you are working on. 
    the third one is the precentage in your sentence, I will choose the highest one.
    '''
    pre_judging_list = []



    '''
    I don't care about which language you are 
    '''
    japanese_result = check_for_japanese.check_presentation(pre_operation_strings)
    pre_judging_list.append(japanese_result)
    judged_language = judge_presentage(pre_judging_list)
    if judged_language[1] == "Na":
        print("OPPs, I only accept Japanese, Korean, English, Hindī,and Russian")
    elif judged_language[1] == "JP":
        check_for_japanese.print_japanese_check(japanese_result)



def judge_presentage(pre_judging_list):
    most_possible_result = [0,"Na",0]
    for language in pre_judging_list:
        if language[0] == 0:
            continue
        if language[2] > most_possible_result[2]:
            most_possible_result = language

    return most_possible_result

main()