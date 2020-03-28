# Question -11

"""
Write a program which accepts a sequence of comma separated 4 digit binary numbers 
as its input and then check whether they are divisible by 5 or not. The numbers that
are divisible by 5 are to be printed in a comma separated sequence.

! Example:

? 0100,0011,1010,1001
! Then the output should be:

? 1010

"""

def check(x):
    total,pw = 0,1
    reversed(x)
    
    for i in x:
        total += pw*(ord(i)-48) # ord is us for return ASCII value 
        pw*=2
    return total % 5 
data = input("Enter data in binary number : ").split(",")
lst = []

for i in data:
    if check(i) == 0 :
        lst.append(i)

print("," .join(lst))