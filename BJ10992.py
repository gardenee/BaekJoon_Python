N = int(input())

for i in range(N):
    if i == N-1:
        print("*" * (2*i+1))
    elif i == 0:
        print(" " * (N-1) + "*")
    else:
        print(" " * (N-1-i) + "*" + " " * (2*i-1) + "*")
