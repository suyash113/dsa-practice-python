def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
# n = 5
# print(f"Factorial of {n} is",factorial(n))

def fibonacci(n):
    if n <= 1:
        return n 
    return fibonacci(n-1) + fibonacci(n-2)
# n = 5
# result = fibonacci(n)
# print(f"Fibonacci of {n} is {result}")

# for i in range(n):
#     print(fibonacci(i))

def sum_of_digits(n):
    if n ==0:
        return 0 
    return (n%10 +sum_of_digits(int(n/10)))

n = 126
print(f'sum of digits of {n} is', sum_of_digits(n))