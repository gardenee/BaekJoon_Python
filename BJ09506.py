from sys import stdin

while True:
    n = int(stdin.readline())
    if n == -1:
        break

    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)

    if sum(divisors) == n:
        print(str(n) + " = " + " + ".join(list(map(str, divisors))))
    else:
        print(str(n) + " is NOT perfect.")
