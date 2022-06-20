T = int(input())
for _ in range(T):
    N = int(input())
    if N == 0:
        print(0)
        continue

    map = dict()
    for _ in range(N):
        item, body = input().split()
        map.setdefault(body, 0)
        map[body] += 1

    ans = 1
    for val in list(map.values()):
        ans *= val+1

    print(ans-1)
