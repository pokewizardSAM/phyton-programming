email = input("Enter your email ID: ")
if email.endswith('@edupillar.com'):
    print("This email belongs to the domain @edupillar.com.")
elif '@edupillar.com' in email:
    print("This email is invalid. It contains the domain @edupillar.com but not in the correct format")
else:
    print("This email does not belong to the domain @edupillar.com.")
