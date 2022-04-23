for _ in range(3):
    ans = 1
    temp = 1
    N = str(input())
    for i in range(7):
        if N[i] == N[i+1]:
            temp += 1
        else:
            if temp > ans:
                ans = temp
            temp = 1
    if temp > ans:
        ans = temp
    print(ans)
