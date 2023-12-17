import csv

with open("school project/practicals/prog12.csv", "+a", newline="") as Merchant_Databse:
    merch_db = csv.writer(Merchant_Databse)
    
    item_record = [["Item_Name", "Description", "Price"]]
    n= 0
    while True:
        if n>0:
            if input("want ot continue adding (y/n):") == "n":
                merch_db.writerows(item_record)
                break

        Item_Name = input("Please enter your item code:")
        desc = input("Please enter your item description:")
        price = input("Please enter your item price:")
        item_record.append([Item_Name,desc,price])
        n += 1
        
