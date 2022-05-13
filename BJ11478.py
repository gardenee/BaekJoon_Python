str = input().replace('\n', '')
N = len(str)
ans = set()

for i in range(1, N+1):
    for j in range(N+1-i):
        ans.add(str[j:j+i])

print(len(ans))
