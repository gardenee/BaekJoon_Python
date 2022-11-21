import bisect

for _ in range(int(input())):
    ipt = list(map(int, input().split()))
    T, kids = ipt[0], ipt[1:]
    answer, line = 0, []

    for i in range(20):
        kid = kids[i]
        idx = bisect.bisect_left(line, kid)
        answer += i - idx
        line = line[:idx] + [kid] + line[idx:]

    print(T, answer)
