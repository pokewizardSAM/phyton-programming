exchange_rate = 83.50
print("Dollar to Rupee Converter")
while True:

  print("1. Dollar to Rupees")
  print("2. Rupees to Dollars")
  print("3. Exit")
  
  choice = int(input("Enter choice: "))

  if choice == 1:
    dollars = float(input("Enter amount in dollars: "))
    rupees = round(dollars * exchange_rate, 2)
    print(f"{dollars} dollars = {rupees} rupees")

  elif choice == 2:
    rupees = float(input("Enter amount in rupees: "))
    dollars = round(rupees / exchange_rate, 2)
    print(f"{rupees} rupees = {dollars} dollars")

  elif choice == 3:
    break
  
  else:
    print("Invalid choice")

print("Program ended")