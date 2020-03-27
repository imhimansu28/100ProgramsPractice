# Question -13

"""
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123
Then, the output should be:

LETTERS 10
DIGITS 3

"""
userInput = input("Enter sentence here")
find = {"DIGITS":0, "LETTERS":0}
for c in userInput:
    if c.isdigit():
        find["DIGITS"]+=1
    elif c.isalpha():
        find["LETTERS"]+=1
    else:
        pass
    
print("LETTERS", find["LETTERS"])
print("DIGITS", find["DIGITS"])