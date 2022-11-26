import bisect

N = int(input())
lst = list(map(int, input().split()))
answer = []
index = []

for num in lst:
    if not answer or answer[-1] < num:
        index.append(len(answer))
        answer.append(num)
    else:
        idx = bisect.bisect_left(answer, num)
        answer[idx] = num
        index.append(idx)

print(len(answer))

i = len(answer)-1
out = []
for n in range(N-1, -1, -1):
    if index[n] == i:
        out.append(lst[n])
        i -= 1

print(*out[::-1])
