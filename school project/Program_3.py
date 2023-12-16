number = input("Enter Phone number: ")
if len(number)==12:
    if number[3]=='-' and number[7]=='-':
        print(number[:3]+ number[4:7]+ number[8:])
        if(number[:3]+number[4:7]+number[8:]).isdigit():
            print('Phone number is valid')
        else : 
            print("Phone number is invalid")
    else : 
        print("Phone number is invalid")
else : 
    print("Phone number is invalid")