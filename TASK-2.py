import math

n = int(input("Enter a number: "))

def math_operations(n):
    square = math.sqrt(n)
    log = math.log(n)
    sine = math.sin(n)
    
    return square, log, sine

square, log, sine = math_operations(n)


print(f"Square root: {square}")
print(f"Logarithm: {log}")
print(f"Sine: {sine}")