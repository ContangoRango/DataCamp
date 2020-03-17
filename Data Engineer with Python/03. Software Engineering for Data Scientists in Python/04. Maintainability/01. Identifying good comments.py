'''
Identifying good comments
We learned about what characteristics make a 'good' comment. In this exercise, you'll apply this knowledge to identify a function that utilizes comment best practices.

Instructions
100 XP
print the text variable that has been pre-loaded into your environment.
print the result of calling the function with more useful commenting on text.
'''
SOLUTION

import re

def extract_0(text):
    # match and extract dollar amounts from the text
    return re.findall(r'\$\d+\.\d\d', text)

def extract_1(text):
    # return all matches to regex pattern
    return re.findall(r'\$\d+\.\d\d', text)

# Print the text
print(text)

# Print the results of the function with better commenting
print(extract_0(text))