# Count unique values inside a list.


lists = [1, 2, 2, 5, 8, 4, 4, 8]
i=0
r=[]
c=0
while i<len(lists):
    if lists[i] not in r:
        r.append(lists[i])
        c+=1
    i+=1
print(c)