grades = {'A+':4.3, 'A0':4.0, 'A-':3.7, 'B+':3.3, 'B0':3.0, 'B-':2.7, 'C+':2.3, 'C0':2.0, 'C-':1.7, 'D+':1.3,
          'D0':1.0, 'D-':0.7, 'F':0.0}

score = 0
num = 0
for _ in range(int(input())):
    t, n, g = input().split()
    num += int(n)
    score += int(n) * grades[g]

print('{0:03.2f}'.format(round(score/num + 0.00000001, 2)))
