def solution(n, clockwise):
    answer = []
    for i in range(n):
        answer.append([])
        for _ in range(n):
            answer[i].append(0)

    a = 0
    l = 0
    m = n

    if clockwise == True:
        while m > 1:
            for i in range(a, m-1):
                answer[a][i] = l+1
                answer[n-1-i][a] = l+1
                answer[i][n-1-a] = l+1
                answer[n-1-a][n-1-i] = l+1
                l += 1
            m -= 1
            a += 1

    else:
        while m > 1:
            for i in range(a, m-1):
                answer[i][a] = l+1
                answer[a][n-1-i] = l+1
                answer[n-1-a][i] = l+1
                answer[n-1-i][n-1-a] = l+1
                l += 1
            m -= 1
            a += 1

    if n%2 == 1:
        answer[n//2][n//2] = n**2//4 + 1

    return answer
