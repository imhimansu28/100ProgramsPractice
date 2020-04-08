# Question -16


"""
Write a program that computes the net amount of a bank account based a transaction log from console input. 
The transaction log format is shown as following:

"""
total = 0
while True:
    s = input().split()
    if  not s:
        break
    cm, num = map(str, s)
    
    if cm =="D":
        total += int(num)
    if cm =="W":
        total -= int(num)
        
print("$",total)