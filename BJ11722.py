import bisect

N = int(input())
lst = list(map(int, input().split()))
answer = []

for num in lst[::-1]:
    if not answer or answer[-1] < num:
        answer.append(num)
        continue

    idx = bisect.bisect_left(answer, num)
    answer[idx] = num

print(len(answer))
