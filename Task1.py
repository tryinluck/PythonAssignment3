# Function to calculate factorial
def factorial(n):
    if n<2:
        return 1
    else:
        return n * factorial(n - 1)
num=int(input("Enter a number: "))
print("Factorial of " + str(num) + " is " + str(factorial(num)))

