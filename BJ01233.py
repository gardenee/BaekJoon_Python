import itertools

A, B, C = map(int, input().split())

numbers = dict()
for i in range(3, A+B+C+1):
    numbers.setdefault(i, 0)

lst = []
for i in itertools.product(range(1, A+1), range(1,B+1), range(1,C+1)):
    lst.append(list(i))

for n in lst:
    numbers[sum(n)] += 1

X = numbers.values()
x = max(X)
ans = 0

for k, v in numbers.items():
    if v == x:
        ans = k
        break

print(ans)
