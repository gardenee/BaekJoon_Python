N = int(input())
num = ''
for i in range(1, N+1):
    num += str(i)

print(num.index(str(N))+1)
