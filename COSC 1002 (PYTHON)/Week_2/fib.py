def fib (n):
    if n <= 2:
        return 1
    else:
        first = 1
        second = 1
        third = second
        while n > 2:
            third = first + second
            first = second
            second = third
            n -= 1
        return third

print(fib(12))
        
