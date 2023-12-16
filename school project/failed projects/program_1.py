interaction = (input('please enter a 10 digit number:'))
if len(interaction)==10:
    for i in interaction:
        # bool_value = ""
        # print(i)
        # if type(i) == int:
        #     bool_value = 1
        #     continue
        # else:
        #     bool_value = 0  
        #     print('please enter only numbers!!!')
        #     break
    # if bool_value == 1:

        first_part = str(interaction[0:3])
        mid_part = str(interaction[3:6])
        last_part = str(interaction[6:10])

        print_number = first_part + "-" + mid_part + "-" + last_part
        print(print_number)
    # else:
        print("try again")
else:
    print('please enter a valid 10digit number')
