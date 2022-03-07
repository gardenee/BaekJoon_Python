T = int(input())

for _ in range(T):
    trash = input()
    N, M = map(int, input().split())
    IQ_C = list(map(int, input().split()))
    IQ_E = list(map(int, input().split()))
    
    avg_C = 0
    avg_E = 0
    for i in range(N):
        avg_C += IQ_C[i]
    for i in range(M):
        avg_E += IQ_E[i]
    avg_C /= N
    avg_E /= M

    ans = 0
    for i in range(N):
        if (IQ_C[i] < avg_C) and (IQ_C[i] > avg_E):
            ans += 1

    print(ans)
