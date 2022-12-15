N = int(input())

for i in range(N):
    if i % 2 == 0:
        for j in range(N-1):
            print("* ", end="")
        print("*")
    else:
        for j in range(N):
            print(" *", end="")
        print()
