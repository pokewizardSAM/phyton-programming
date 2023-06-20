inpt_list = eval(input("Enter a list: "))

def summation(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + summation(lst[1:])

result = summation(inpt_list)
print(f"The sum of the list: {inpt_list} is {result}")
kk