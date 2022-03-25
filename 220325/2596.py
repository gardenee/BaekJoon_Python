abc = list('ABCDEFGH')
num = ['000000', '001111', '010011', '011100', '100110', '101001', '110101', '111010']
ref = dict(zip(num, abc))
dic = {}
T = 0
for i in num:
    dic[i] = []
    for j in i:
        dic[i].append(j)

ans = ''
N = int(input())
password = str(input())
for i in range(N):
    n = password[6*i:6*(i+1)]
    if n in num:
        ans += ref[n]
    else:
        temp = []
        for k in range(len(num)):
            temp.append(0)
            for j in range(6):
                if n[j] == num[k][j]:
                    temp[k] += 1
                if 5 in temp:
                    break
            if 5 in temp:
                break
        if 5 in temp:
            ans += ref[num[temp.index(5)]]
        else:
            T = 1
            print(i+1)
            break

if T == 0:
    print(ans)
