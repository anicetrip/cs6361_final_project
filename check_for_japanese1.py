# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 14:45:14 2021

@author: siobh
"""
# Import lists
from lists_japanese import hiragana
from lists_japanese import katakana

# Make a list to store a combined list of hiragana and katakana characters
kana = []

# Combine the two alphabets into one big list
for i in hiragana:
    kana.append(i)

for i in katakana:
    kana.append(i)


# Set values in variables
characters_in_text = 0
matching_characters = 0
percent_match_jp = 0

# Prompt the user to enter the text to be analysed
text = input("Please enter the text to analyse: ")

# Iterate through text
for i in text:
    # count the total characters
    characters_in_text +=1
    if i in kana:
        #count the characters that match those in our kana list
        matching_characters += 1
        
        
print(f'There are {characters_in_text} characters in the text and {matching_characters} of them are either hiragana or katakana') 
        

# Find the percentage of kana in the text
if matching_characters != 0:
    percent_match_jp = int((matching_characters / characters_in_text) * 100)

# can comment this out later
print(f'{percent_match_jp}% of the text has been identified as either hiragana or katakana')

# Kana makes up 40% of an average Japanese text
# To be safe, we're checking if the figure is above 15%
if percent_match_jp > 15:
    print('The text is Japanese\n')
else:
    print('The language of the text has not been identified (as Japanese)')
    