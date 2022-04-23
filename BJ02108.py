from sys import stdin
N = int(input())
lst = [0] * N
for i in range(N):
    lst[i] = int(stdin.readline())
lst.sort()

print(int(round((sum(lst)+0.00000001)/N, 0)))
print(lst[N//2])

ref = {}
for i in range(N):
    ref.setdefault(lst[i], 0)
    ref[lst[i]] += 1
nums = list(ref.values())
nums.sort()
temp = []
for k, v in ref.items():
    if v == nums[-1]:
        temp.append(k)
if len(temp) == 1:
    print(temp[0])
else:
    temp.sort()
    print(temp[1])

print(lst[-1]-lst[0])
