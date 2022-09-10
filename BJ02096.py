N = int(input())
sum1 = [0] * 3
sum2 = [0] * 3

for _ in range(N):
    ipt = list(map(int, input().split()))
    temp1 = [0] * 3
    temp1[0] = min(sum1[0], sum1[1])
    temp1[2] = min(sum1[1], sum1[2])
    temp1[1] = min(temp1[0], temp1[2])
    sum1 = temp1

    temp2 = [0] * 3
    temp2[0] = max(sum2[0], sum2[1])
    temp2[2] = max(sum2[1], sum2[2])
    temp2[1] = max(temp2[0], temp2[2])
    sum2 = temp2

    for i in range(3):
        sum1[i] += ipt[i]
        sum2[i] += ipt[i]

print(max(sum2), min(sum1))
