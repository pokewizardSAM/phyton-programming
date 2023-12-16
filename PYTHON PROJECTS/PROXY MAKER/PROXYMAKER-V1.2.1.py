import csv
import os
import time
import subprocess

all_teachers_list = []
absent_teachers_list = []  
input_list = []
vacancy_list = [0,0,0,0,0,0,0,0]
teacher_availibity_list=[0,0,0,0,0,0,0,0]
class_availibility =[0,0,0,0,0,0,0,0]
selected_teachs = []

def generate_absent_list(teachers, db_reader):
    global absent_teachers_list
    for row in db_reader:
        teacher_name = row[0].replace(" ", "").lower()
        if teacher_name in teachers:
            absent_teachers_list.append(row)
    
    absent_teachers_file = open("PROXY MAKER /Output/teachers-absent.csv", "w+")
    fh = csv.writer(absent_teachers_file)
    fh.writerows(absent_teachers_list)
    return absent_teachers_list

def convrt_str_to_list(l):
    simple_list = list(l.replace(" ","").split(","))
    return simple_list

def refresh_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo()

def enclose_boxes(prin_txt):
    command = f'echo {prin_txt} | boxes -d parchment | lolcat -f'
    try:
        output = subprocess.run(command, shell=True, text=True, capture_output=True)
        print(output.stdout)
    except subprocess.CalledProcessError as e:
        print(f"command failed with error ",{e})

def colorize(prin_txt):
    command = f"echo {prin_txt} |lolcat -a -d 100 -F 10000000000000000000"
    output = subprocess.run(command, shell=True, text=True, capture_output=True)
    print(output.stdout)

def get_all_teachers(db_reader):
    global all_teachers_list 
    Teacher_db.seek(0)
    next(db_reader)
    next(db_reader)

    for row in db_reader:
        teacher_name = row[0].replace(" ","").lower()
        all_teachers_list.append(f"{teacher_name}")
    return all_teachers_list

def absent_teachers(absent_teachers_name, db_reader):
    print("------------------------------")
    for name in absent_teachers_name:
        print(f"   Checking for {name}")
    generate_absent_list(absent_teachers_name, db_reader)
    print("------------------------------")
    create_proxies() 
    return

def i_reduce_redundancy(period_no,other_teacher_in_same_period):
    if teacher_availibity_list[period_no-1] != 0:
        if (teacher_availibity_list[period_no-1].count(other_teacher_in_same_period[0])) > 0:
            None
        else:
            teacher_availibity_list[period_no-1] = teacher_availibity_list[period_no-1] + f",{other_teacher_in_same_period[0]}"

    else:
        teacher_availibity_list[period_no-1] = other_teacher_in_same_period[0]

def create_proxies():
    global db_reader
    for teacher_info in absent_teachers_list:  
        print("==========================================================================")
        print(f"Alloting {teacher_info[0]} proxy classes.......")
        print("Default schedule: ", end="")
        print(f"{teacher_info}\n")
        period_no = 0

        for classes in teacher_info[1:]:
            if classes != "BREAK":
                period_no += 1

            if classes != "FREE" and classes != "BREAK":
                print(f"{period_no} period is in class {classes} ")
                reallocation = True
                vacancy_list[period_no-1] += 1
            else:
                reallocation = False

            # print(f"{classes} , reallocation variable is {reallocation} ")

            if reallocation is True:
                Teacher_db.seek(0)
                print(">>> Free teachers in this period are as follows:")
                for other_teacher_in_same_period in db_reader:

                    if other_teacher_in_same_period[0].replace(" ", "").lower() in input_list:
                        continue

                    if period_no > 3:     # definately blasted my head 

                        if other_teacher_in_same_period[period_no+1] == "FREE":
                            print(f"    {other_teacher_in_same_period[0]}")
                            i_reduce_redundancy(period_no,other_teacher_in_same_period)
                    else:

                        if other_teacher_in_same_period[period_no] == "FREE":
                            print(f"    {other_teacher_in_same_period[0]}")
                            i_reduce_redundancy(period_no,other_teacher_in_same_period)
                        
                    # save_reallocation_data(realloctaed_list)    
                if teacher_availibity_list[period_no-1] == 0:
                    Available_teachers = teacher_availibity_list[period_no-1]   #for later usage 
                    # print(Available_teachers)
                    print("    No, Teachers are available !!")

        period_no = 0
    
    return

def logo():
    logo = """
               _ (`-.  _  .-')              ) (`-.                        _   .-')      ('-.    .-. .-')     ('-.  _  .-')              (`-.                      
              ( (OO  )( \( -O )              ( OO ).                     ( '.( OO )_   ( OO ).-.\  ( OO )  _(  OO)( \( -O )           _(OO  )_                    
             _.`     \ ,------.  .-'),-----.(_/.  \_)-. ,--.   ,--.       ,--.   ,--.) / . --. /,--. ,--. (,------.,------.       ,--(_/   ,. \ .---.   .------.  
            (__...--'' |   /`. '( OO'  .-.  '\  `.'  /   \  `.'  /        |   `.'   |  | \-.  \ |  .'   /  |  .---'|   /`. '      \   \   /(__//_   |   |   ___|  
             |  /  | | |  /  | |/   |  | |  | \     /\ .-')     /         |         |.-'-'  |  ||      /,  |  |    |  /  | |       \   \ /   /  |   |   |  '--.   
             |  |_.' | |  |_.' |\_) |  |\|  |  \   \ |(OO  \   /          |  |'.'|  | \| |_.'  ||     ' _)(|  '--. |  |_.' |        \   '   /,  |   |   `---.  '. 
             |  .___.' |  .  '.'  \ |  | |  | .'    \_)|   /  /\_         |  |   |  |  |  .-.  ||  .   \   |  .--' |  .  '.'         \     /__) |   |   .-   |  | 
             |  |      |  |\  \    `'  '-'  '/  .'.  \ `-./  /.__)        |  |   |  |  |  | |  ||  |\   \  |  `---.|  |\  \           \   /     |   |.-.| `-'   / 
             `--'      `--' '--'     `-----''--'   '--'  `--'             `--'   `--'  `--' `--'`--' '--'  `------'`--' '--'           `-'      `---'`-' `----''  
"""
    colorize(logo)

def main_menu():
    main_menu = """
                                                                +----------------------------------+
                                                                |               Options            |
                                                                +----------------------------------+
                                                                | 1. Genreate Proxies              |
                                                                | Q. Quit                          |
                                                                |                                  |
                                                                +----------------------------------+"""     
    
    print(main_menu)

def sub_menu():
    sub_menu = """
                                                                +----------------------------------+
                                                                |               Options            |
                                                                +----------------------------------+
                                                                | 1. View all Teacher              |
                                                                | 2. Add Teacher                   |
                                                                | 3. Edit Selection                |
                                                                | 4. Generate proxies              |
                                                                | Q. Quit                          |
                                                                |                                  |
                                                                +----------------------------------+"""
    print(sub_menu)
def edit_sub_menu():
    edit_sub_menu = """
                                                                +----------------------------------+
                                                                |               Options            |
                                                                +----------------------------------+
                                                                | 1. Remove Teachers               |
                                                                | 2. Sort in order (A~Z)           |
                                                                | 3. Save Selection                |
                                                                |                                  |
                                                                +----------------------------------+"""
    print(edit_sub_menu)

def editing_selection():
    while True:
        edit_sub_menu()
        print(f">>> Your Selection : {selected_teachs}") 
        user_choice = input('select your options:')
        if user_choice == '1':
            rem_list = list(input("enter the position number of teachers you want to remove:").replace(" ","").split(","))
            for i in rem_list:
                i = int(i)
                del selected_teachs[i-1]
        if user_choice == '2':
            print("yet to be implemented ")
        if user_choice == '3':
            break
def main():
    logo()
    main_menu()
    global db_reader
    global Teacher_db
    global selected_teachs
    while True:
        usr_choice = input("Enter your choice: ")
        if usr_choice == "1":
            refresh_screen()

            while True:
                with open("PROXY MAKE FILE .csv", "r+", newline="") as Teacher_db:
                    db_reader = csv.reader(Teacher_db)
                    # next(db_reader)
                    global input_list
                    sub_menu()
                    if selected_teachs:
                        print(f">>> Your Selection : {selected_teachs}") 
                    sub_user_choice = input("Choose your option:")

                    if sub_user_choice == "1":
                        refresh_screen()
                        enclose_boxes(get_all_teachers(db_reader))
                    elif sub_user_choice == "2":
                        simple_list = input('Enter the names of the teachers separated by "," : ')
                        selected_teachs = convrt_str_to_list(simple_list)
                        refresh_screen()
                    elif sub_user_choice == "3":
                        refresh_screen()    
                        editing_selection()
                    elif sub_user_choice == "4":
                        refresh_screen()
                        absent_teachers(selected_teachs, db_reader)
                    elif sub_user_choice  == "q" or sub_user_choice == "Q":
                        exit()
                    else :
                        print("wrong input !!")
                        time.sleep(1)
                        refresh_screen()


            print("\n\nAll proxies have been alloted successfully...........")
        elif usr_choice == "Q" or usr_choice== "q":
            exit()





main()
print(vacancy_list)
print(teacher_availibity_list)
