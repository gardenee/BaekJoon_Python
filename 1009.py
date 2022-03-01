a = list(map(int,list(input().split())))
b = a.pop(0)

for i in range(b):
    print((a[2*i]**a[2*i+1])%10)

