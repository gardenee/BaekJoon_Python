N = int(input())

for i in range(N):
    print(" " * (N-i-1) + "*", end="")
    for j in range(i):
        print(" *", end="")
    print()
