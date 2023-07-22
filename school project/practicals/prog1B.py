number = int(input("Enter a number: "))

if number < 2:
    print(number, "is not a prime number")
else:
    is_prime = True

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, "is a prime number")
    else:
        print(number, "is not a prime number")
