# Question -9

"""
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:

Hello world
Practice makes perfect
Then, the output should be:

HELLO WORLD
PRACTICE MAKES PERFECT

"""

mylist = []

while True:
    x = input("Enter the sentence")
    if len(x) == 0:
        break;
    mylist.append(x.upper())
    
for line in mylist:
    print(line)