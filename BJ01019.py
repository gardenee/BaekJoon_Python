N = int(input())
num = str(N)
answer = [0] * 10

for i in range(len(num)):
    curr = int(num[i])

    if i == 0:
        for n in range(1, curr):
            answer[n] += 10 ** (len(num)-1)
        answer[curr] += int(num[1:] if len(num) > 1 else 0) + 1
        continue

    for n in range(10):
        if n == 0 and curr == 0:
            answer[0] += 10 ** (len(num) - i - 1) * (int(num[:i])-1) + 1 + (int(num[i+1:]) if i != len(num)-1 else 0)
            continue

        if n != 0 and n == curr:
            answer[n] += (int(num[i+1:])+1) if i != len(num)-1 else 1
        answer[n] += 10 ** (len(num) - i - 1) * (int(num[:i])+1 if n != 0 and n < curr else int(num[:i]))

print(*answer)
