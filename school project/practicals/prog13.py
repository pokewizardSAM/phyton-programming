import csv
import time

with open("school project/practicals/credentials.csv", "+a", newline="") as credentials:
    cred_list = csv.reader(credentials)

    print("| Welcome to python credential checker |")

    while True:
        print("1. Read all the credentials")
        print("2. Write a new credential")
        print("3. Check your credentials")

        usr_choice = input("What do you want to do? Enter your choice: ")

        if usr_choice == "1":
            credentials.seek(0)
            for row in cred_list:
                print(row)

        elif usr_choice == "2":
            username = input("Enter the username of the new user: ")
            password = input("Enter the password of the new user: ")
            root_access = input(
                "are you administrator ? (y/n): ")

            write_confirm = input(
                "Are you sure you want to write this to the credential list? (y/n): ")
            if write_confirm == "y":
                cred_list.append([username, password, root_access])

        elif usr_choice == "3":
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            for row in cred_list:
                if username == row[0] and password == row[1]:
                    print("Login authorized")
                    time.sleep(2)
                    break
            else:
                print("Wrong username or password!!!")
