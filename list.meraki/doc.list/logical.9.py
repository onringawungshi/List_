# list=["11","33","50"]
# str=" "
# i=0
# while i<len(list):
#     s=str+list[i]
#     i+=1
# print(int(str),end=" ")

# print(type(int(str)))

s=[1,2,3,[4,4],[1,2,3]]
i=0
sum=0
a=[]
while i<len(s):
    if type(s[i])==list:
       s.remove(s[i])
    else:
        a.append(s[i])
    i+=1
print(a)