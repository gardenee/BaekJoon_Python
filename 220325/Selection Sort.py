#Selection Sort
lst = []
N = int(input())
for _ in range(N):
    lst.append(int(input()))

for i in range(N-1):
    j = lst.index(min(lst[i:]))
    lst[j], lst[i] = lst[i], lst[j]

for i in lst:
    print(i)
