for _ in range(int(input())):
    N = int(input())
    stock = list(map(int, input().split()))

    answer, max = 0, 0
    for i in range(N-1, -1, -1):
        if max < stock[i]:
            max = stock[i]
        else:
            answer += max - stock[i]

    print(answer)
