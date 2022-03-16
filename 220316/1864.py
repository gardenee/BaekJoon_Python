octopus = ['-', '\\', '(', '@','?', '>', '&', '%']
dic = {}
for i, v in enumerate(octopus):
    dic[v] = i
dic['/'] = -1

while True:
    N = input()
    if N == '#':
        break
    else:
        num = []
        for i in N:
            num.append(dic[i])
        ans = 0
        for i in range(len(num)):
            ans += num[i] * 8 ** (len(num)-i-1)
        print(ans)

