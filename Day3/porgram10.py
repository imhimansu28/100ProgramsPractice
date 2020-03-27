# Question -10

"""

Write a program that accepts a sequence of whitespace separated words as input and 
prints the words after removing all duplicate words and sorting them alphanumerically.

? Suppose the following input is supplied to the program:

! hello world and practice makes perfect and hello world again

? Then, the output should be:

! again and hello makes perfect practice world

"""

my_word_list = input("Enter word  in sspearted  whitespace").split()

for i in my_word_list:
    if my_word_list.count(i) >1 :
        my_word_list.remove(i)
        
my_word_list.sort()
print(" ".join(my_word_list))