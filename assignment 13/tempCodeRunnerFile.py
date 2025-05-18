def math_operations(a,b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return add, sub, mul, div

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
add, sub, mul, div = math_operations(a,b)
print("Addition: ", add)
print("Subtraction: ", sub)
print("Multiplication: ", mul)
print("Divide : ", div)