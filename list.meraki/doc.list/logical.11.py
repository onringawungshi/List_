# l=[1,2,3,[4,5],[6,7,8,9],10]
# i=0
# a=[]
# while i<len(l):
#     if type(l[i])==type([]):
#         j=0
#         while j<len(l[i]):
#             a.append(l[i][j])
#             j+=1
#     else:
#         a.append(l[i])
#     c=0
#     sum=0
#     while c<len(a):
#         sum=sum+a[c]
#         c+=1
#     i+=1
# print(sum)