ref = dict()
ref['black'] = 0
ref['brown'] = 1
ref['red'] = 2
ref['orange'] = 3
ref['yellow'] = 4
ref['green'] = 5
ref['blue'] = 6
ref['violet'] = 7
ref['grey'] = 8
ref['white'] = 9

a = []

for i in range(3):
    a.append(input())

print((10 * ref[a[0]] + ref[a[1]]) * 10 ** ref[a[2]])
