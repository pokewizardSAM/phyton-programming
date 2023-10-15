import csv


absent_teachers_list = []  
input_list = ["rahulgautam", "vikassir", "shifamomin", "sumanma'am", "kamyama'am","patilsir","sandeepsir"]


def generate_absent_list(teachers, db_reader):
    global absent_teachers_list
    absent_teachers_list = []
    for row in db_reader:
        teacher_name = row[0].replace(" ", "").lower()
        if teacher_name in teachers:
            absent_teachers_list.append(row)
    return absent_teachers_list



def absent_teachers(teachers_name, db_reader):
    print("------------------------------")
    for name in teachers_name:
        print(f"   Checking for {name}")
    generate_absent_list(teachers_name, db_reader)
    print("------------------------------")
    create_proxies() 
    return



def create_proxies():
    global db_reader
    for teacher_info in absent_teachers_list:  
        print("==========================================================================")
        print(f"Alloting {teacher_info[0]} proxy classes.......")
        print("Default schedule: ", end="")
        print(f"{teacher_info}\n")
        period_no = 0
        realloctaed_list = []

        for classes in teacher_info[1:]:
            if classes != "BREAK":
                period_no += 1

            if classes != "FREE" and classes != "BREAK":
                print(f"{period_no} period is in class ", end="")
                reallocation = True
            else:
                reallocation = False

            print(f"{classes} , reallocation variable is {reallocation} ")

            if reallocation is True:
                Teacher_db.seek(0)
                print(">>> Free teachers in this period are as follows: \n")
                for other_teacher_in_same_period in db_reader:
                    # print(other_teacher_in_same_period[0],"dwdwdwdwdwdwdwdwdwdwd")
                    # print(period_no)
                    # print(other_teacher_in_same_period[0].replace(" ", "").lower())
                    # print(input_list)
                    if other_teacher_in_same_period[0].replace(" ", "").lower() in input_list:
                        continue

                    if period_no > 3:     # definately blasted my head 
                        if other_teacher_in_same_period[period_no+1] == "FREE":
                            print(f"{other_teacher_in_same_period[0]}")
                            realloctaed_list.append(other_teacher_in_same_period[0])
                    else:
                        if other_teacher_in_same_period[period_no] == "FREE":
                            print(f"{other_teacher_in_same_period[0]}")
                            realloctaed_list.append(other_teacher_in_same_period[0])
                    
                        
                    # save_reallocation_data(realloctaed_list)    


            print("\n")

        realloctaed_list = []
        period_no = 0
    
    return

# def save_reallocation_data(reallocated_list):
#     reallocation_fh = open("reallocation_data.csv", "a+")
#     reallocation_file = csv.writer(reallocation_fh)
#     reallocation_file.writerow(["Teacher's name", "1st", "2nd", "3rd","BREAK","4th","5th","6th","7th","8th"])
    
#     reallocation_file.writerow(reallocated_list)


def main():
    global db_reader
    global Teacher_db
    with open("PROXY MAKE FILE .csv", "r+", newline="") as Teacher_db:
        db_reader = csv.reader(Teacher_db)
        next(db_reader)
        absent_teachers(input_list, db_reader)

main()
