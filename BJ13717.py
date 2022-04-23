dic = {}
for _ in range(int(input())):
    name = input()
    a, b = map(int, input().split())
    num = 0
    candy = b
    while candy >= a:
        num += candy//a
        candy = candy % a + 2 * (candy//a)
    dic[name] = num

print(sum(list(dic.values())))

M = max(dic.values())
for k, v in dic.items():
    if v == M:
        print(k)
        break
