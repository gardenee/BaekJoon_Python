N = int(input())
weights = list(map(int, input().split()))
n = int(input())
marbles = list(map(int, input().split()))

possible = [False] * 15001
possible[0] = True

for w in weights:
    temp = set()
    for i in range(15001):
        if possible[i]:
            temp.add(abs(i-w))
            if i+w < 15001:
                temp.add(i+w)
    for t in temp:
        possible[t] = True

for m in marbles:
    if m < 15001 and possible[m]:
        print("Y", end=" ")
    else:
        print("N", end=" ")
