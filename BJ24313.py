a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

answer = 1 if (c > a1 and c * n0 >= a1 * n0 + a0) else 0

print(answer)