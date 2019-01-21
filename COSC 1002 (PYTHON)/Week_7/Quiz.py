def quiz(n):
    count = 0
    for i in range(1,n+1):
        count += 2**i
    return count
