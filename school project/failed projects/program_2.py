interaction = (input("Please enter a 10 didgit mobile no"))
# Legal input is 123-456-7890 
while True :
    interaction = (input("Please enter a 10 digit mobile no"))
    if len(interaction) == 10:
        for i in interaction:
            if type(i) != int:
                print("enter only numbers")
                exit()
            else:
                break
        

        print("number is correct")
        



# while True:
#     for i in interaction:
#         if i == str:
#             please