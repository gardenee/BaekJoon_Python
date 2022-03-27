key = ['TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH', 'HHT', 'HHH']
ref = {}
for i in key:
    ref[i] = 0

for _ in range(int(input())):
    dic = ref.copy()
    result = input()
    for i in range(38):
        dic[result[i]+result[i+1]+result[i+2]] += 1
    print(' '.join(list(map(str, dic.values()))))
