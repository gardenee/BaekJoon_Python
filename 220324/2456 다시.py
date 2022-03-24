score = {}
num3 = {}
num2 = {}
for i in range(3):
    score[i+1] = 0
    num3[i+1] = 0
    num2[i+1] = 0

for _ in range(int(input())):
    scores = list(map(int, input().split()))
    for i in range(3):
        score[i+1] += scores[i]
        if scores[i] == 3:
            num3[i+1] += 1
        if scores[i] == 2:
            num2[i+1] += 1

M = max(score.values())
if list(score.values()).count(M) == 1:
    for k, v in score.items():
        if v == M:
            print(k, v)
            break
else:
    same = []
    for k, v in score.items():
        if v == M:
            same.append(k)
        else:
            num3[k] = 0
            num2[k] = 0
    if list(num3.values()).count(max(num3.values())) == 1:
        for k, v in num3.items():
            if v == max(num3.values()):
                print(k, M)
                break
    else:
        same = []
        for k, v in num3.items():
            if v == max(num3.values()):
                same.append(k)
            else:
                num2[k] = 0
        if list(num2.values()).count(max(num2.values())) == 1:
            for k, v in num2.items():
                if v == max(num2.values()):
                    print(k, M)
                    break
        else:
            print(0, M)
