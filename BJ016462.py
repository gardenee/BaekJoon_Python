scores = []
avg = 0
N = int(input())

for _ in range(N):
    scores.append(str(input()))

for i in range(len(scores)):
    s = scores[i]
    if ('0' in s) or ('6' in s):
        s = s.replace('0', '9')
        s = s.replace('6', '9')
        if int(s) > 100:
            s = 100
        scores[i] = s
    avg += int(s)

if (avg % N)/N >= 0.5:
    print(avg//N + 1)
else:
    print(avg//N)
