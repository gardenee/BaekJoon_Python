#Insertion Sort
lst = []
N = int(input())
for _ in range(N):
    lst.append(int(input()))

for i in range(N-1):
    j = i+1
    while j > 0:
        if lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j -= 1
        else:
            break

for i in lst:
    print(i)
