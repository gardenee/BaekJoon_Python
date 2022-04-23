def d(N):
    return N + N//10000 + (N%10000)//1000 + ((N%10000)%1000)//100 + (((N%10000)%1000)%100)//10 + \
           (((N%10000)%1000)%100)%10

lst = []
for i in range(1,10001):
    lst.append(i)

for i in range(len(lst)):
    if d(i+1) in lst:
        lst[lst.index(d(i+1))] = '!'
    if lst[i] != '!':
        print(lst[i])

