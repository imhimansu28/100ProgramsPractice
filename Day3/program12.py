# Question -12

"""
Write a program, which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number.The numbers obtained should be printed 
in a comma-separated sequence on a single line.

"""

myValue = []

for i in range(1000, 3001):
    flag = 1
    for  j in str(i):
        if ord(j)%2 != 0:
            flag = 0
    if flag == 1:
        myValue.append(str(i))
        
print(",".join(myValue))

