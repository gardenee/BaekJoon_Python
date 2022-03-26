N = int(input())
if N < 3:
    print(0)
else:
    if N % 2 == 0:
        Max = N//2 - 1
    else:
        Max = N//2

    ans = 0
    for i in range(Max):
        if 3 * (Max - i) >= N:
            if (N - Max + i) % 2 == 0:
                ans += Max - i - (N - Max + i)//2 + 1
            else:
                ans += Max - i - (N - Max + i)//2
        else:
            break

    print(ans)