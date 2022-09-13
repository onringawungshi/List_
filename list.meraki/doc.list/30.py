# Given a list of numbers, write a Python program to count positive and negative numbers in a List.

list1 = [2, -7, 5, -64, -14]
i=0
c=0
m=0
while i<len(list1):
    if list1[i]>0:
        c=c+1
    else:
        m=m+1
    i+=1
print(c,"= positive")
print(m,"= negative")