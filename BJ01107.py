target = int(input())
N = int(input())
broken = []
if N != 0:
    broken = list(input().split())

answer = abs(target-100)

for i in range(1000100):
    num, j = str(i), 0

    while j < len(num):
        if num[j] not in broken:
            j += 1
        else:
            break

    if j == len(num):
        answer = min(answer, len(str(i)) + abs(i-target))

print(answer)
