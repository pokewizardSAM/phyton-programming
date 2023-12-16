def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def get_fibonacci_term(n):
    print(f"Calculating the {n}th Fibonacci term...")
    result = fib(n)
    print(f"The {n}th Fibonacci term is {result}")

n = int(input("Enter the nth term to calculate: "))
get_fibonacci_term(n)