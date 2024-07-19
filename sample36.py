#multiplication table
'''
def multiplication_table(number, upto):
    print(f"Multiplication table for {number} up to {upto}:")
    for i in range(1, upto + 1):
        print(f"{number} x {i} = {number * i}")

number = 9
upto = 10
result=multiplication_table(number, upto)
print(result)
'''

#armstrong number
'''
def is_armstrong_number(number):
    digits = str(number)
    num_digits = len(digits)  
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits) 
    return armstrong_sum == number
number = 370
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
'''

#factoria

#iterative
'''
def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


number = 5
print(f"Iterative: Factorial of {number} is {factorial_iterative(number)}")
'''

#recursive
'''
def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


number = 5
print(f"Recursive: Factorial of {number} is {factorial_recursive(number)}")
'''

