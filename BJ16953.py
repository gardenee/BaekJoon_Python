A, B = map(int, input().split())

curr = [B]
cnt = 0
while True:
    cnt += 1
    if not curr or min(curr) < A:
        cnt = -1
        break
    if A in curr:
        break

    temp = list()
    for n in curr:
        if n % 2 == 0 and n//2 >= A:
            temp.append(n//2)
        if (n-1) % 10 == 0 and (n-1)//10 >= A:
            temp.append((n-1)//10)

    curr = temp.copy()

print(cnt)
