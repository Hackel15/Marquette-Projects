import math
def is_prime(n):
    y = int(math.ceil(math.sqrt(n)))
    for x in range(2, y+1):
        if (n % x == 0) & (x != n):
            print(n, "is NOT prime")
            return False
    print(n, "is prime")
    return True

is_prime(1)
is_prime(2)
is_prime(3)
is_prime(4)
is_prime(5)
is_prime(7)


def sum_product(n):
    summ = 0.0
    for i in range(n, 100 + 1):
        summ += 1 / i
    print("Sum: ", summ)

sum_product(1)

def sum_product_2(n):
    summ = 0.0
    for i in range(n, 20 + 1):
        summ += i**3
    print("Sum: ", summ)

sum_product_2(1)

def sum_product_3(n):
    summ = 1
    for i in range(n, 10 + 1):
        summ *= (i + 5) / (i**2 + 5)
    print("Sum: ", summ)
        
sum_product_3(1)
