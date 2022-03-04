import math
import itertools

lst = list(map(int, input().split()))
lcm = []

comb = list(map(list,itertools.combinations([0,1,2,3,4],3)))

for i in comb:
    lcm.append(math.lcm(lst[i[0]], lst[i[1]], lst[i[2]]))


print(min(lcm))