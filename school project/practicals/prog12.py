import csv

with open("school project/practicals/prog12.csv", "+a", newline="") as data_file:
    data_writer = csv.writer(data_file)

    record = [["name", "info", "cost"]]
    count = 0
    while True:
        if count > 0:
            if input("continue? (y/n):") == "n":
                data_writer.writerows(record)
                break

        name = input("item name:")

        details = input("item details:")
            
        amount = float(input("item price:"))
        
        record.append([name, details, amount])
        count += 1
