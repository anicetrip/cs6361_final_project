# The requirement for your code part



## Preface

You can give me multiple files, but In one of them for each language analysis, You should provide me two function in my required form, you can make your own function names and value names, but in one of each language you should make a comment to tell me which one I should use.

## The Comment for the Functions at Beginning which you Provide your Functions:

```python
'''
code maker:
language name:
language name in your code:
<Your function name>:judge result:
<Your function name>:output function
'''
```

## Form of Functions:

### Judge the Result:

This function used for find out whether the function may be one language and the percentage of having their own language characters.

```python
def judge_result(String:text)->[int,String,int]:result:
```

In the list of input, the text should be what you want to judge.

In the list of result, the first one value is a `int`, if it equals 1, it means that it might be this language, if it equals 0, it means that it is not possible to be this language.

The second one is the name you want to show in the code, It should be a English name or short name in English.

The third one is the percentage   of the possibility, it should not be 0.

If you want to test by your self instead of in my code, you should make a input function instead of put that into the judge_result function.



### Output Function:

This function is used for you to show your result about whether it is the language you are judging. In this function, you should provide 2 situation, if it is the language or not, print out what you what to print for these two situation.

```python
def output_function([int,String,int]:result):
```



In the list of input, it would be the same as `result` in` judge_result`.



## Easy testing function:

```python
#test.py
import <your .py file>

input = input("input your sentences. \n")
judge_result = <your .py file>.judge_result(input)
<your .py file>.output_function(judge_result)
output_function

```



