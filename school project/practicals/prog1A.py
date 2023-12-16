number = int(input("Enter a number:"))
inp_num = number
factorial = 1
while number > 0: 
    factorial = factorial*number
    number -= 1 

print(f"The factorial of {inp_num} is {factorial}")
