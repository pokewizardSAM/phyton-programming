# num = [2,3,4,5,1,4,5,6,7,8,23,6,8,9,7,8]

# def sort(num):
#     for i in range(len(num)-1):
#         min_position = i 
#         for j in range(i,len(num)):
#             if num[j] < num[min_position]:
#                 min_position = j 
#         num[i], num[min_position]= num[min_position], num[i]

# print(sort(num))

num = [2,3,4,5,1,4,5,6,7,8,23,6,8,9,7,8]

def selection_sort(num):
    for i in range(len(num)-1):
        min_position = i 
        for j in range(i,len(num)):
            print(i,j)
            if num[j] < num[min_position]:
                min_position = j 
        num[i], num[min_position]= num[min_position], num[i]
    return num

print(selection_sort(num))
