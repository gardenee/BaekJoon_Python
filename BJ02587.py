lst = []
for _ in range(5):
    lst.append(int(input()))
lst.sort()
print(int(sum(lst)/5))
print(lst[2])
