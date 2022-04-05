for _ in range(int(input())):
    N, M = map(int, input().split())
    if N == M:
        print(1)
    else:
        r = M-N
        Arr = [1] * (max(r, N+1)+1)
        for i in range(1, (max(r, N+1)+1)):
            Arr[i] = Arr[i-1] * i
        ans = 0
        i = 0
        while i <= (r-1) and i <= N:
            ans += (Arr[N+1]//(Arr[i+1]*Arr[N-i])) * (Arr[r-1]//(Arr[i]*Arr[r-1-i]))
            i += 1
        print(ans)
