def area_of_circle(radius):
    return 3.14 * radius ** 2

def factorial_of_number(n):
    if n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial
    
def is_perfect_square(n):
    if n < 0:
        return False
    else:
        sqrt = n ** 0.5
        return sqrt == int(sqrt)    