import csv
import time


with open("school project/practicals/credentials.csv", "+a" , newline="") as credentials:
    cred_list = csv.reader(credentials)
    cred_write = csv.writer(credentials)

    cred_records = [["Username", "Password", "Root privilage"]]
    if cred_list == []:
        cred_write.writerows(cred_records)

    print("| Welcome to python credential checker |")
    while True:
        usr_choice = input("What do you want to do ? \n 1. Read all the credentials \n 2. write a new credential \n 3. check your credentials \n Enter your choice:")
        if usr_choice == "1":
            credentials.seek(0)
            for i in cred_list:
                print(i)
        elif usr_choice == "2":
            username = input("Enter the username of the new user:")
            passswd  = input("enter the password of the new user:")
            root_acc = input("Do you wan the user to have root access(y/n):")

            write_confirm = input("are you sure you want to write this to thw credential lsit? (y/n):")
            if write_confirm == "y":
                cred_write.writerow([username,passswd, root_acc])
            else:
                continue
        elif usr_choice == "3":
            usrname = input("enter you username:")
            passwrd = input("enter your password:")

            credentials.seek(0)
            for i in cred_list:
                if usrname == i[0] and passwrd == i[1]:
                    print("Login authorised")
                    time.sleep(2)
                    continue
                
            print("Wrong username or password !!!\n")