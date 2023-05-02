lis = [2,3,4,5,1,4,5,6,7,8,23,6,8,9,7,8]
for i in range(0,len(lis),1):
    for j in range(i):
        if lis[j] > lis[j+1]:
            lis[j], lis[j+1]= lis[j+1], lis[j]
print(lis)