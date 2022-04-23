abc = 'abcdefghijklmnopqrstuvwxyz'
dic = {}
for i, k in enumerate(abc):
    dic[k] = i + 1
    dic[k.upper()] = i + 27

word = input()
num = 0
for l in word:
    num += dic[l]

arr = [1] * (num + 1)
arr[1] = 0
arr[0] = 0
T = 1
for i in range(2, num+1):
    if arr[num] == 0:
        T = 0
        break
    elif arr[i] == 1:
        for j in range(2*i, num+1, i):
            arr[j] = 0

if T == 0:
    print('It is not a prime word.')
else:
    print('It is a prime word.')
