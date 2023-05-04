# # integer = 1212122121212121212433454535
# # integer_str  = str(integer)
# # list_int = list(integer_str)
# # print(list_int)

# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         global k   
#         k=[]
#         c=0
#         n=int(input('enter integer'))
#         l=str(n)
#         for i in l:
#          k.append(i)

#         return k

#     c=0
#     f=hammingWeight()
#     for j in f:
#         if j=='1':
#             c+=1
#     print(c)


def let():
 global k   
 k=[]
 c=0
 n=int(input('enter integer'))
 l=str(n)
 for i in l:
  k.append(i)

 return k



c=0
f=let()
for j in f:
    if j=='1':
        c+=1
print(c)