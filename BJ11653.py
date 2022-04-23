def factorization(n):
    for i in range(2, n + 1):
        if n == 1:
            return
        elif n % i == 0:
            print(i)
            return factorization(n // i)

factorization(int(input()))
