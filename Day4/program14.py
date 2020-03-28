# Question -14

"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

! Suppose the following input is supplied to the program:

? Hello world!

! Then, the output should be:

? UPPER CASE 1
? LOWER CASE 9

"""

word  = input("Enter word")
upper,lower = 0,0

for i in word:
    if 'a' <=i and i <= 'z':
        lower += 1
    if 'A' <=i and i <= 'Z':
        upper +=1
        
print(f"Upper Case {upper}\n Lower Case {lower}\n")