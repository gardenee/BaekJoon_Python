T = int(input())

for _ in range(T):
    trash = input()
    N, M = map(int, input().split())
    IQ_C = list(map(int,input().split()))
    IQ_E = list(map(int,input().split()))
    sum_C = 0
    sum_E = 0

    for i in range(N):
        sum_C += IQ_C[i]
    for i in range(M):
        sum_E += IQ_E[i]

    ans = 0
    for i in range(N):
        temp_C = sum_C - IQ_C[i]
        temp_E = sum_E + IQ_C[i]
        if (temp_C/(N-1) > sum_C/(N)) & (temp_E/(M+1) > sum_E/(M)):
            ans += 1

    print(ans)
